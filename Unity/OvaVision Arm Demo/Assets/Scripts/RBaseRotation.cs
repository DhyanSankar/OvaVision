using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class RBaseRotation : MonoBehaviour
{
    public float rotationSpeed = 50f; // Speed at which the base rotates

    void Update()
    {
        // Get input from the user (Left/Right Arrow keys or A/D keys)
        float input = Input.GetAxis("Horizontal");

        // Rotate the base around the Y-axis
        transform.Rotate(Vector3.up * input * rotationSpeed * Time.deltaTime);
    }
}