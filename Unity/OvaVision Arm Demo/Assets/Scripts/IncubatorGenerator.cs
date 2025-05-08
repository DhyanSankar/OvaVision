using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class IncubatorController : MonoBehaviour
{
    [Header("Incubator Settings")]
    public GameObject incubatorPrefab;  // Assign your prefab in Inspector
    public int numberOfIncubators = 1;  // Number to spawn
    private int curIncubators = 0;
    public float radius = 30f;           // Distance from center

    [Header("Central Target")]
    public Transform centerPoint;       // The point all incubators face

    private GameObject[] incubators;

    void Start()
    {
        SpawnIncubators();
    }

    void Update()
    {
        // Automatically refresh in editor when variables change
        if (curIncubators!= numberOfIncubators)
        {
            ClearIncubators();
            SpawnIncubators();
        }
    }

    void SpawnIncubators()
    {

        incubators = new GameObject[numberOfIncubators];

        float angleStep = 360f / numberOfIncubators;

        for (int i = 0; i < numberOfIncubators; i++)
        {
            float angle = i * angleStep * Mathf.Deg2Rad;
            Vector3 position = new Vector3(
                Mathf.Cos(angle) * radius,
                0,
                Mathf.Sin(angle) * radius
            ) + centerPoint.position;

            GameObject incubator = Instantiate(incubatorPrefab, position, Quaternion.identity, transform);
            incubator.transform.LookAt(centerPoint.position);  // Make it face the center
            incubator.transform.Rotate(0, 90, 0);
            incubators[i] = incubator;
        }
        curIncubators = numberOfIncubators;
    }

    void ClearIncubators()
    {
        if (incubators == null) return;

        foreach (var obj in incubators)
        {
            if (obj != null)
                Destroy(obj);
        }
    }
}