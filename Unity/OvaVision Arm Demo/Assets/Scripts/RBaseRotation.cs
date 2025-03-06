using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class RBaseRotation : MonoBehaviour
{
    public float rotationSpeed = 50f; // Speed at which the base rotates

    public float targetRotationY = 0;

    public bool manual = false;
    void Update()
    {
        // Get input from the user (Left/Right Arrow keys or A/D keys)
        if (manual)
        {
            float input = Input.GetAxis("Horizontal");

            // Rotate the base around the Y-axis
            transform.Rotate(Vector3.up * input * rotationSpeed * Time.deltaTime);
        }

        else
        {


            // Rotate the base around the Y-axis

            float currentY = transform.eulerAngles.y;

            if (Mathf.Abs(currentY - targetRotationY) > rotationSpeed * Time.deltaTime)
            {
                float newY = Mathf.MoveTowardsAngle(currentY, targetRotationY, rotationSpeed * Time.deltaTime);
                transform.eulerAngles = new Vector3(transform.eulerAngles.x, newY, transform.eulerAngles.z);
            }
            else
            {
                transform.eulerAngles = new Vector3(transform.eulerAngles.x, targetRotationY, transform.eulerAngles.z);
            }
        }

    }
    public float getRotation()
    {
        return transform.eulerAngles.y;
    }
}