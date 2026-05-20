using System;
using System.Threading;
using UnityEditor;
using UnityEngine;

[InitializeOnLoad]
internal static class M1PlayModeSmokeTest
{
    private const string MenuPath = "Tools/Codex/M1/Run Play Mode Smoke Test";
    private const string InProgressKey = "Codex.M1PlayModeSmoke.InProgress";
    private const string TokenKey = "Codex.M1PlayModeSmoke.Token";
    private const string EnteredPlayModeKey = "Codex.M1PlayModeSmoke.EnteredPlayMode";
    private const string ExitRequestedKey = "Codex.M1PlayModeSmoke.ExitRequested";
    private const string LogPrefix = "[M1 PlayMode Smoke]";

    private static SynchronizationContext editorContext;

    static M1PlayModeSmokeTest()
    {
        editorContext = SynchronizationContext.Current ?? editorContext;
        EditorApplication.playModeStateChanged -= OnPlayModeStateChanged;
        EditorApplication.playModeStateChanged += OnPlayModeStateChanged;
        EditorApplication.delayCall += ResumePendingSmokeTest;
    }

    [MenuItem(MenuPath, false, 2100)]
    private static void Run()
    {
        PostToEditor(StartSmokeTest);
    }

    private static void StartSmokeTest()
    {
        var token = DateTime.UtcNow.ToString("yyyyMMddTHHmmssfffZ");
        EditorPrefs.SetBool(InProgressKey, true);
        EditorPrefs.SetString(TokenKey, token);
        EditorPrefs.SetBool(EnteredPlayModeKey, false);
        EditorPrefs.SetBool(ExitRequestedKey, false);

        Debug.Log($"{LogPrefix} requested token={token}");
        EnterPlayMode();
    }

    private static void EnterPlayMode()
    {
        if (!IsInProgress())
        {
            return;
        }

        if (EditorApplication.isPlaying)
        {
            MarkEnteredAndRequestExit();
            return;
        }

        Debug.Log($"{LogPrefix} entering Play Mode token={Token()}");
        EditorApplication.isPlaying = true;
    }

    private static void OnPlayModeStateChanged(PlayModeStateChange state)
    {
        if (!IsInProgress())
        {
            return;
        }

        switch (state)
        {
            case PlayModeStateChange.ExitingEditMode:
                Debug.Log($"{LogPrefix} exiting Edit Mode token={Token()}");
                break;
            case PlayModeStateChange.EnteredPlayMode:
                MarkEnteredAndRequestExit();
                break;
            case PlayModeStateChange.ExitingPlayMode:
                Debug.Log($"{LogPrefix} exiting Play Mode token={Token()}");
                Complete();
                break;
            case PlayModeStateChange.EnteredEditMode:
                Complete();
                break;
        }
    }

    private static void ResumePendingSmokeTest()
    {
        if (!IsInProgress())
        {
            return;
        }

        if (EditorApplication.isPlaying)
        {
            MarkEnteredAndRequestExit();
            return;
        }

        if (EditorPrefs.GetBool(EnteredPlayModeKey, false))
        {
            Complete();
        }
    }

    private static void MarkEnteredAndRequestExit()
    {
        if (!EditorPrefs.GetBool(EnteredPlayModeKey, false))
        {
            EditorPrefs.SetBool(EnteredPlayModeKey, true);
            Debug.Log($"{LogPrefix} entered Play Mode token={Token()}");
        }

        if (EditorPrefs.GetBool(ExitRequestedKey, false))
        {
            return;
        }

        EditorPrefs.SetBool(ExitRequestedKey, true);
        PostToEditor(ExitPlayMode);
    }

    private static void ExitPlayMode()
    {
        if (!IsInProgress() || !EditorApplication.isPlaying)
        {
            return;
        }

        Debug.Log($"{LogPrefix} requesting Edit Mode token={Token()}");
        EditorApplication.isPlaying = false;
    }

    private static void Complete()
    {
        if (EditorPrefs.GetBool(EnteredPlayModeKey, false))
        {
            Debug.Log($"{LogPrefix} entered Play Mode token={Token()} (recorded)");
            Debug.Log($"{LogPrefix} completed token={Token()}");
        }
        else
        {
            Debug.LogWarning($"{LogPrefix} ended before entering Play Mode token={Token()}");
        }

        Clear();
    }

    private static bool IsInProgress()
    {
        return EditorPrefs.GetBool(InProgressKey, false);
    }

    private static string Token()
    {
        return EditorPrefs.GetString(TokenKey, "unknown");
    }

    private static void Clear()
    {
        EditorPrefs.DeleteKey(InProgressKey);
        EditorPrefs.DeleteKey(TokenKey);
        EditorPrefs.DeleteKey(EnteredPlayModeKey);
        EditorPrefs.DeleteKey(ExitRequestedKey);
    }

    private static void PostToEditor(Action action)
    {
        if (editorContext != null)
        {
            editorContext.Post(_ => action(), null);
            return;
        }

        EditorApplication.delayCall += () => action();
    }
}
