import java.util.*;
import java.io.*;
import java.math.*;

class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int nbFloors = in.nextInt(); 
        int width = in.nextInt(); 
        int nbRounds = in.nextInt(); 
        int exitFloor = in.nextInt(); 
        int exitPos = in.nextInt(); 
        int nbTotalClones = in.nextInt(); 
        int nbAdditionalElevators = in.nextInt(); 
        int nbElevators = in.nextInt();
        int elevators[] = new int[nbFloors];
        in.nextLine();

        for(int i = 0; i < nbFloors; i++)
            elevators[i] = 0;

        for (int i = 0; i < nbElevators; i++) {
            int elevatorFloor = in.nextInt(); 
            int elevatorPos = in.nextInt(); 
            elevators[elevatorFloor] = elevatorPos;
            in.nextLine();
        }

        while (true) {
            int cloneFloor = in.nextInt(); 
            int clonePos = in.nextInt(); 
            String direction = in.next(); 
            in.nextLine();
            
            String cmd = "WAIT";

            if(cloneFloor == -1)
            {
                cmd = "WAIT";
            }
            else if(cloneFloor == exitFloor)
            {
                cmd = exitChecks(direction, clonePos, exitPos);

            } else {
                cmd =  elevatorChecks(direction, clonePos, elevators[cloneFloor]);
            }

            cmd = safetyChecks(cmd, direction, clonePos, width);
            System.out.println(cmd);
        }

    }
    static String exitChecks(String direction, int clonePos, int exitPos)
    {
        String cmd = "WAIT";
        if("RIGHT".equals(direction) && clonePos > exitPos)
        {
            cmd = "BLOCK";
        } else if("LEFT".equals(direction) && clonePos < exitPos)
        {
            cmd = "BLOCK";
        }
        return cmd;
    }

    static String elevatorChecks(String direction, int clonePos, int elevatorPos)
    {
        String cmd = "WAIT";
        if("RIGHT".equals(direction) && clonePos > elevatorPos)
        {
            cmd = "BLOCK";
        } else if("LEFT".equals(direction) && clonePos < elevatorPos)
        {
            cmd = "BLOCK";
        }
        return cmd;
    }

    static String safetyChecks(String cmd, String direction, int clonePos, int width)
    {
        if("WAIT".equals(cmd))
        {
            if("RIGHT".equals(direction) && clonePos == width -1)
            {
                cmd = "BLOCK";
            }
            else if("LEFT".equals(direction) && clonePos == 0)
            {
                cmd = "BLOCK";
            }
        }
        return cmd;
    }
}