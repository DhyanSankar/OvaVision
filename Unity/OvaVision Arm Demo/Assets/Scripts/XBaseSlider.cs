using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class XBaseSlider : MonoBehaviour
{
    public float moveSpeed = 2f; 
    public float minX = 1f; 
    public float maxX = 3.5f;


    void Update()
    {

        

        float input = Input.GetAxis("Vertical");

        if (Input.GetKey(KeyCode.LeftShift))
        {
    // Ignore the silly naming oops

            float newX = transform.localPosition.z + input * moveSpeed * Time.deltaTime;


            newX = Mathf.Clamp(newX, minX, maxX);


           
            transform.localPosition = new Vector3(transform.localPosition.x, transform.localPosition.y, newX);
        }

    }
 
}
