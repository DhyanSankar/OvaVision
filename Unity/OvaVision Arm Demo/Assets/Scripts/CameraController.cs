using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{

    public float moveSpeed = 10f;
    public float rotationSpeed = 2f;
    public float mouseSensitivity = 2f;

    private float xRotation = 0f;
    private float yRotation = 0f;

    void Update()
    {
  
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");
        Vector3 movement = new Vector3(horizontalInput, 0, verticalInput) * moveSpeed * Time.deltaTime;
        transform.Translate(movement);

 
        float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity;
        float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity;

        yRotation += mouseX;
        xRotation -= mouseY;
      
        transform.rotation = Quaternion.Euler(xRotation, yRotation, 0);
    }
}
