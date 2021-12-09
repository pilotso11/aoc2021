#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string exitChecks(string direction, int clonePos, int exitPos)
{
    string cmd = "WAIT";
    if(direction == "RIGHT" && clonePos > exitPos)
    {
        cmd = "BLOCK";
    } else if(direction == "LEFT" && clonePos < exitPos)
    {
        cmd = "BLOCK";
    }
    return cmd;
}

string elevatorChecks(string direction, int clonePos, int elevatorPos)
{
    string cmd = "WAIT";
    if(direction == "RIGHT" && clonePos > elevatorPos)
    {
        cmd = "BLOCK";
    } else if(direction == "LEFT" && clonePos < elevatorPos)
    {
        cmd = "BLOCK";
    }
    return cmd;
}

string safetyChecks(string cmd, string direction, int clonePos, int width)
{
    if( cmd == "WAIT")
    {
        if(direction == "RIGHT" && clonePos == width -1)
        {
            cmd = "BLOCK";
        }
        else if(direction == "LEFT" && clonePos == 0)
        {
            cmd = "BLOCK";
        }
    }
    return cmd;
}
int main()
{
    int nb_floors; // number of floors
    int width; // width of the area
    int nb_rounds; // maximum number of rounds
    int exit_floor; // floor on which the exit is found
    int exit_pos; // position of the exit on its floor
    int nb_total_clones; // number of generated clones
    int nb_additional_elevators; // ignore (always zero)
    int nb_elevators; // number of elevators
    cin >> nb_floors >> width >> nb_rounds >> exit_floor >> exit_pos >> nb_total_clones >> nb_additional_elevators >> nb_elevators; cin.ignore();
    
    int elevators[nb_floors];

    for (int i = 0; i < nb_elevators; i++) 
    {
        int elevator_floor; // floor on which this elevator is found
        int elevator_pos; // position of the elevator on its floor
        cin >> elevator_floor >> elevator_pos; cin.ignore();
        elevators[elevator_floor] = elevator_pos;
    }

    // game loop
    while (1) {
        int clone_floor; // floor of the leading clone
        int clone_pos; // position of the leading clone on its floor
        string direction; // direction of the leading clone: LEFT or RIGHT
        cin >> clone_floor >> clone_pos >> direction; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;
        string cmd = "WAIT";
            if(clone_floor == -1)
            {
                cmd = "WAIT";
            }
            else if(clone_floor == exit_floor)
            {
                cmd = exitChecks(direction, clone_pos, exit_pos);

            } else {
                cmd =  elevatorChecks(direction, clone_pos, elevators[clone_floor]);
            }

            cmd = safetyChecks(cmd, direction, clone_pos, width);


        cout << cmd << endl; // action: WAIT or BLOCK
    }
    
}
