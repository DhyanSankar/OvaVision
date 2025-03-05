using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Windows;
using static UnityEditor.Experimental.GraphView.GraphView;

public class LayerController : MonoBehaviour
{
    // Start is called before the first frame update

    public GameObject layerPrefab;

    public GameObject[] layerArray;
    public bool[] extended;
    public int numberOfLayers = 4;

    public float extensionDistance = 10;
    public float extensionSpeed = 10;
    void Start()
    {
        layerArray = new GameObject[numberOfLayers];
        extended = new bool[numberOfLayers];
        

        for (int i=0;i<numberOfLayers; i++)
        {
            if (extensionDistance < 0)
            {
                extended[i] = true; 
            }

            layerArray[i] = Instantiate(layerPrefab,transform);
            layerArray[i].transform.position = new Vector3(transform.position.x, transform.position.y+10*i, transform.position.z); 
        }
    }

    // Update is called once per frame
    public int KeyToNumber()
    {
        // https://discussions.unity.com/t/setting-an-integer-to-a-number-pressed/686967/3
        for (int number = 0; number <= 9; number++)
        {
            if (UnityEngine.Input.GetKeyDown(number.ToString()))
                return number;
        }

        return -1;
    }

    void Update()
    {


        int n = KeyToNumber();
        if (n != -1)
        {
            Debug.Log(n);
            extended[n] = !extended[n];
        }

        for (int i = 0; i < layerArray.Length; i++)
        {
            
            if (layerArray[i] != null)
            {

                Vector3 currentPos = layerArray[i].transform.position;

                float newX;


                if (extended[i])
                {
                    newX = currentPos.x + extensionSpeed * Time.deltaTime;
                }
                else
                {
                    newX = currentPos.x - extensionSpeed * Time.deltaTime;
                }

               


                newX = Mathf.Clamp(newX, Mathf.Min(transform.position.x, transform.position.x + extensionDistance) , Mathf.Max(transform.position.x, transform.position.x + extensionDistance));

                layerArray[i].transform.position = new Vector3(newX, currentPos.y, currentPos.z); ; 
            }
        }
    }


}
