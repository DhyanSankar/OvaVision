using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ZBaseUpward : MonoBehaviour
{

    public float moveSpeed = 2f; 
    public float minY = 6.0f; 
    public float maxY = 40.0f;
    public float targetHeight = 0f;
    public bool manual = false;


    void Update()
    {



        float input = Input.GetAxis("Vertical");

        if (manual)
        {
            if (!Input.GetKey(KeyCode.LeftShift))
            {
                float newY = transform.position.y + input * moveSpeed * Time.deltaTime;




                newY = Mathf.Clamp(newY, minY, maxY);




                transform.position = new Vector3(transform.position.x, newY, transform.position.z);
            }
        }

        else
        {
            float currentY = transform.position.y;
            if (Mathf.Abs(currentY - targetHeight) > moveSpeed * Time.deltaTime) // Prevent jitter
            {
                float newY = Mathf.MoveTowards(currentY, targetHeight, moveSpeed * Time.deltaTime);
                newY = Mathf.Clamp(newY, minY, maxY);

                transform.position = new Vector3(transform.position.x, newY, transform.position.z);
            }
            else
            {
                transform.position = new Vector3(transform.position.x, targetHeight, transform.position.z);
            }
        }
        
        

    }

    public float getHeight()
    {
        return transform.position.y;
    }

}
