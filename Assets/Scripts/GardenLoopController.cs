using UnityEngine;

public sealed class GardenLoopController : MonoBehaviour
{
    private RestoreTarget[] targets;

    public bool IsComplete { get; private set; }

    private void Awake()
    {
        targets = GetComponentsInChildren<RestoreTarget>();
    }

    private void Update()
    {
        if (IsComplete || targets.Length == 0)
        {
            return;
        }

        for (var i = 0; i < targets.Length; i++)
        {
            if (!targets[i].IsRestored)
            {
                return;
            }
        }

        IsComplete = true;
    }

    private void OnGUI()
    {
        if (!IsComplete)
        {
            return;
        }

        var style = new GUIStyle(GUI.skin.label)
        {
            alignment = TextAnchor.UpperCenter,
            fontSize = 32,
            fontStyle = FontStyle.Bold
        };
        style.normal.textColor = Color.white;

        GUI.Label(new Rect(0f, 24f, Screen.width, 48f), "Garden Restored", style);
    }
}
