using UnityEngine;
using UnityEngine.InputSystem;

public sealed class RestoreTarget : MonoBehaviour
{
    [SerializeField] private Transform player;
    [SerializeField] private float interactionDistance = 1f;

    private SpriteRenderer spriteRenderer;
    private bool restored;

    private void Awake()
    {
        spriteRenderer = GetComponent<SpriteRenderer>();
    }

    private void Update()
    {
        if (restored || player == null)
        {
            return;
        }

        var keyboard = Keyboard.current;
        if (keyboard == null || !keyboard.eKey.wasPressedThisFrame)
        {
            return;
        }

        if (Vector2.Distance(player.position, transform.position) > interactionDistance)
        {
            return;
        }

        restored = true;
        spriteRenderer.enabled = false;
    }
}
