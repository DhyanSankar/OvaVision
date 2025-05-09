using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EggGenerator : MonoBehaviour
{
    public GameObject eggPrefab;
    public GameObject maleEggPrefab;
    public GameObject femaleEggPrefab;



    public int numberOfLayers = 4;
    public int[] hasEgg;
    private List<GameObject> eggs;

   

        void Start()
    {
        eggs = new List<GameObject>();
        setEggs(hasEgg);
    }

    public void clearEggs()
    {
        foreach (GameObject egg in eggs)
        {
            Destroy(egg);
        }
        eggs.Clear();
    }

    public void setEggs(int[] eggTypes)
    {
        for (int i = 0; i < numberOfLayers;i++)
        {
            hasEgg[i] = eggTypes[i]; 
        }
        numberOfLayers = hasEgg.Length;



        for (int i = 0; i < numberOfLayers; i++)
        {

            if (hasEgg[i] == 1)
            {
                GameObject egg = Instantiate(eggPrefab);
                egg.transform.position = new Vector3(transform.position.x, 5 + transform.position.y + 10 * i, transform.position.z);
                eggs.Add(egg);
                Debug.Log(egg);
            }
            if (hasEgg[i] == 2)
            {
                GameObject egg = Instantiate(maleEggPrefab);
                egg.transform.position = new Vector3(transform.position.x, 5 + transform.position.y + 10 * i, transform.position.z);
                eggs.Add(egg);
            }
            if (hasEgg[i] == 3)
            {
                GameObject egg = Instantiate(femaleEggPrefab);
                egg.transform.position = new Vector3(transform.position.x, 5 + transform.position.y + 10 * i, transform.position.z);
                eggs.Add(egg);
            }
        }
    }


}
