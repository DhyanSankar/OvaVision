using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using static UnityEngine.GraphicsBuffer;

public class CameraController : MonoBehaviour
{

    public float moveSpeed = 10f;
    public float rotationSpeed = 20f;
    public float zoomSpeed = 10f;
 
    public Transform center;

    public float minDistance = 2f;
    public float maxDistance = 20f;

    void Update()
    {




        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        transform.RotateAround(center.position, Vector3.up, -horizontalInput * rotationSpeed * Time.deltaTime);

        Vector3 direction = (transform.position - center.position).normalized;
        float distance = Vector3.Distance(transform.position, center.position);

        float zoomAmount = -verticalInput * zoomSpeed * Time.deltaTime;

      
        if ((distance + zoomAmount >= minDistance) && (distance + zoomAmount <= maxDistance))
        {
            transform.position += direction * zoomAmount;
        }

        transform.LookAt(center);

        // Vector3 movement = new Vector3(horizontalInput, 0, verticalInput) * moveSpeed * Time.deltaTime;
        // transform.Translate(movement);


        // float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity;
        // float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity;

        // yRotation += mouseX;
        // xRotation -= mouseY;

        // transform.rotation = Quaternion.Euler(xRotation, yRotation, 0);
    }
}
