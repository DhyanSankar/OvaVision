using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EggGrabber : MonoBehaviour
{

    public GameObject heldEgg = null;      // Reference to the egg being held

    // When an object enters the trigger collider

    private void OnTriggerEnter(Collider other)
    {
        Debug.Log("collided");
        // Check if the object is an egg and we are not already holding one
        if (heldEgg == null && other.CompareTag("Egg") && !Input.GetKey(KeyCode.P))
        {
            // Grab the egg
            heldEgg = other.gameObject;
            // Parent the egg to the gripper so it follows the arm's movement

            
            // Save the egg's current scale
            Vector3 originalScale = heldEgg.transform.lossyScale;

            // Parent the egg to the gripper while preserving its world position
            heldEgg.transform.SetParent(transform, true);

            // Reapply the original scale to counter any inherited scale changes
           

            // Optionally disable physics on the egg for stability
            Rigidbody eggRb = heldEgg.GetComponent<Rigidbody>();
            if (eggRb != null)
            {
               eggRb.isKinematic = true;
            }
            heldEgg.transform.rotation = Quaternion.identity;
            heldEgg.transform.localScale = Vector3.one;
            heldEgg.transform.localScale = new Vector3(originalScale.x / transform.lossyScale.x, originalScale.y / transform.lossyScale.y, originalScale.z / transform.lossyScale.z);

            Debug.Log("Egg grabbed!");
        }
    }

    // Check for release input every frame
    private void Update()
    {
        if (heldEgg != null && Input.GetKey(KeyCode.P))
        {
            // Release the egg: Unparent it and re-enable physics

            heldEgg.transform.SetParent(null);

            Rigidbody eggRb = heldEgg.GetComponent<Rigidbody>();
            if (eggRb != null)
            {
               eggRb.isKinematic = false;
            }
            Debug.Log("Egg released!");
            heldEgg = null;
        }
    }
}
