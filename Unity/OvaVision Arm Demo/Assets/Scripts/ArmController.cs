using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using static UnityEditor.Experimental.GraphView.GraphView;

public class ArmController : MonoBehaviour
{
    // Start is called before the first frame update

    public RBaseRotation rBase;
    public ZBaseUpward zBase;
    public XBaseSlider[] xBases;

    public EggGrabber eggGrabber;

    public float rBaseRotation;
    public float zBaseHeight;
    public float[] xBasesExtensions;

    

    public bool settingCoordinates = false;
    public bool manual = false;


    public LayerController[] incubators;

    public int startIncubator = 0;
    public int startLayer = 0 ;
    public int endIncubator = 0;
    public int endLayer = 0;


    public bool keyboard = true;
    public bool movingEgg = false;
    public bool startMoving = false;
    private float eggMoveState = 0;
    public string commands = "";

    private readonly string validKeys = "0123456789rxzq";

    // Update is called once per frame
    void Update()
    {

        foreach (char c in validKeys)
        {
           
            KeyCode key = c switch
            {
                '0' => KeyCode.Alpha0,
                '1' => KeyCode.Alpha1,
                '2' => KeyCode.Alpha2,
                '3' => KeyCode.Alpha3,
                '4' => KeyCode.Alpha4,
                '5' => KeyCode.Alpha5,
                '6' => KeyCode.Alpha6,
                '7' => KeyCode.Alpha7,
                '8' => KeyCode.Alpha8,
                '9' => KeyCode.Alpha9,
                'r' => KeyCode.R,
                'x' => KeyCode.X,
                'z' => KeyCode.Z,
                'q' => KeyCode.Q,
                _ => KeyCode.None
            };

            if (key != KeyCode.None && Input.GetKeyDown(key))
            {
                commands += c;
            }
            if (Input.GetKeyDown(KeyCode.P))
            {
                commands = "";
            }
        }

        if (settingCoordinates)
        {
            rBase.targetRotationY = rBaseRotation;
            zBase.targetHeight = zBaseHeight;
            for (int i = 0; i < xBases.Length; i++)
            {
                xBases[i].targetExtension = xBasesExtensions[i];
            }
        }
        rBase.manual = manual;
        zBase.manual = manual;
        for (int i = 0; i < xBases.Length; i++)
        {
            xBases[i].manual = manual;
        }

        if (movingEgg)
        {
            MoveEgg(startIncubator,startLayer,endIncubator,endLayer);
        }


    }

   
    // returns (rotation, height)
    Vector2 LayerToCoordinates(int incubatorNumber, int layer)

    {
        float newRotation = 0;

        if (incubatorNumber == 0)
        {
            newRotation = 270;
        }
        if (incubatorNumber == 1)
        {
            newRotation = 90;
        }
        float newHeight = (layer+1) * 10;



        return new Vector2(newRotation,newHeight);
    }
    void GrabEgg(int incubator, int layer)

    {
        Vector2 targetPosition = LayerToCoordinates(incubator, layer);
       
        if (eggGrabber.heldEgg == null)
        {
            zBase.targetHeight = targetPosition.y - 4;
        }
        else
        {
            zBase.targetHeight = targetPosition.y;
        }
    }

    void DropEgg(int incubator, int layer)

    {
        Vector2 targetPosition = LayerToCoordinates(incubator, layer);

        if (eggGrabber.heldEgg == null)
        {
            zBase.targetHeight = targetPosition.y;
        }
        else
        {
            zBase.targetHeight = targetPosition.y - 4;
            if (zBase.getHeight() == targetPosition.y - 4)
            {
                eggGrabber.dropping = true;
            }
        }
    }

    // Move egg process
    // 0 - Done
    // 1 - Going to first egg
    // 2 - Grabbing egg
    // 3 - Retracting incubator
    // 4 - Going to target location
    // 5 - Dropping egg
    // 6 - Resetting

    void MoveEgg(int incubator1, int layer1, int incubator2, int layer2)

    {
        Vector2 startPosition = LayerToCoordinates(incubator1, layer1);
        Vector2 endPosition = LayerToCoordinates(incubator2, layer2);

        Debug.Log(eggMoveState);
        if (eggMoveState==0 && startMoving)
        {
            startMoving = false;
            eggMoveState = 1;
        }

        if (eggMoveState == 1)
        {
            if (rBase.getRotation() != startPosition.x)
            {
                rBase.targetRotationY = startPosition.x;
            }
            else if (zBase.getHeight() != startPosition.y)
            {

                zBase.targetHeight = startPosition.y;

            }
            else if (xBases[0].getExtendedDistance() != xBases[0].maxX)
            {
                // Debug.Log(" " + xBases[0].getExtendedDistance() + " " + xBases[0].maxX);
                xBases[0].targetExtension = xBases[0].maxX;

            }
            else
            {
                eggMoveState = 2;
            }
        }
        else if (eggMoveState == 2)
        {

            // Make incubator extend
            incubators[incubator1].extended[layer1] = true;


            if (incubators[incubator1].layerArray[layer1].transform.position.x == incubators[incubator1].transform.position.x + incubators[incubator1].extensionDistance)
            {
                GrabEgg(incubator1, layer1);
                if (zBase.getHeight() == startPosition.y && eggGrabber.heldEgg != null)
                {
                    eggMoveState = 3;




                }
            }

        }
        else if (eggMoveState == 3)
        {
            incubators[incubator1].extended[layer1] = false;
            if (incubators[incubator1].layerArray[layer1].transform.position.x == incubators[incubator1].transform.position.x)
            {
                if (xBases[0].getExtendedDistance() != xBases[0].minX)
                {
                    Debug.Log(" " + xBases[0].getExtendedDistance() + " " + xBases[0].maxX);
                    xBases[0].targetExtension = xBases[0].minX;

                }
                else
                {
                    eggMoveState = 4;
                }

            }
        }
        else if (eggMoveState == 4)
        {
            if (rBase.getRotation() != endPosition.x)
            {
                rBase.targetRotationY = endPosition.x;
            }
            else if (zBase.getHeight() != endPosition.y)
            {

                zBase.targetHeight = endPosition.y;

            }
            else if (xBases[0].getExtendedDistance() != xBases[0].maxX)
            {

                xBases[0].targetExtension = xBases[0].maxX;

            }
            else
            {
                eggMoveState = 5;
            }

        }
        else if (eggMoveState == 5)
        {
            incubators[incubator2].extended[layer2] = true;

            if (incubators[incubator2].layerArray[layer2].transform.position.x == incubators[incubator2].transform.position.x + incubators[incubator2].extensionDistance)
            {
                DropEgg(incubator2, layer2);
                if (zBase.getHeight() == endPosition.y && eggGrabber.heldEgg == null)
                {
                    eggGrabber.dropping = false;
                    eggMoveState = 6;

                }
            }
        }
        else if (eggMoveState == 6)
        {
            incubators[incubator2].extended[layer2] = false;
            if (incubators[incubator2].layerArray[layer2].transform.position.x == incubators[incubator2].transform.position.x)
            {
                if (xBases[0].getExtendedDistance() != xBases[0].minX)
                {
                    Debug.Log(" " + xBases[0].getExtendedDistance() + " " + xBases[0].maxX);
                    xBases[0].targetExtension = xBases[0].minX;

                }
                else if (rBase.getRotation() != 0)
                {
                    rBase.targetRotationY = 0;
                }
                else if (zBase.getHeight() != zBase.minY)
                {

                    zBase.targetHeight = zBase.minY;

                }
                else if (xBases[0].getExtendedDistance() != xBases[0].minX)
                {

                    xBases[0].targetExtension = xBases[0].minX;

                }
                else
                {
                    eggMoveState = 0;
                }
            }
        }

        }
    }
    
