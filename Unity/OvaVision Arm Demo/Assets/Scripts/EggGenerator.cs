using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EggGenerator : MonoBehaviour
{
    public GameObject eggPrefab;



    public int numberOfLayers = 4;
    public bool[] hasEgg;

   

        void Start()
    {
        numberOfLayers = hasEgg.Length;
       


        for (int i = 0; i < numberOfLayers; i++)
        {

            if (hasEgg[i])
            {
                GameObject egg = Instantiate(eggPrefab);
                egg.transform.position = new Vector3(transform.position.x, 5 + transform.position.y + 10 * i, transform.position.z);
            }
        }
    }

}
