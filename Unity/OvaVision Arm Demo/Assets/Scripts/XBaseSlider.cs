using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using static UnityEngine.GraphicsBuffer;

public class XBaseSlider : MonoBehaviour
{
    public float moveSpeed = 2f; 
    public float minX = 1f; 
    public float maxX = 3.5f;

    public float targetExtension = 1f;

    public bool manual = false;


    void Update()
    {

        if (manual)
        {




            float input = Input.GetAxis("Vertical");

            if (Input.GetKey(KeyCode.LeftShift))
            {

                float newX = transform.localPosition.z + input * moveSpeed * Time.deltaTime;


                newX = Mathf.Clamp(newX, minX, maxX);



                transform.localPosition = new Vector3(transform.localPosition.x, transform.localPosition.y, newX);
            }
        }
        else
        {
            float currentX = transform.localPosition.z;
            if (Mathf.Abs(currentX - targetExtension) > moveSpeed * Time.deltaTime)
            {
                float newX = Mathf.MoveTowards(currentX, targetExtension, moveSpeed * Time.deltaTime);
                newX = Mathf.Clamp(newX, minX, maxX);
                transform.localPosition = new Vector3(transform.localPosition.x, transform.localPosition.y, newX);
            }
            else
            {
                transform.localPosition = new Vector3(transform.localPosition.x, transform.localPosition.y, targetExtension);
            }

        }

    }
    public float getExtendedDistance()
    {
        return transform.localPosition.z;
    }
 
}
