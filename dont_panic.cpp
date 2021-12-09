#include <iostream>
#include <string>
using namespace std;
string R = "RIGHT", L = "LEFT", W = "WAIT", B = "BLOCK", direction, cmd;

int main()
{
    int nb_floors,width, nb_rounds,exit_floor,exit_pos,nb_total_clones,nb_additional_elevators,nb_elevators, clone_floor,clone_pos,elevator_floor, elevator_pos;
    cin >> nb_floors >> width >> nb_rounds >> exit_floor >> exit_pos >> nb_total_clones >> nb_additional_elevators >> nb_elevators;
    cin.ignore();

    int elevators[nb_floors];

    for (int i = 0; i < nb_elevators; i++)
    {
        cin >> elevator_floor >> elevator_pos;
        cin.ignore();
        elevators[elevator_floor] = elevator_pos;
    }

    while (1)
    {
        cmd=W;
        cin >> clone_floor >> clone_pos >> direction;
        cin.ignore();

        if (clone_floor == -1)
            ;
        else if (clone_floor == exit_floor)
        {
            if ((direction == R && clone_pos > exit_pos) || (direction == L && clone_pos < exit_pos))
                cmd = B;
        }
        else if ((direction == R && clone_pos > elevators[clone_floor]) || (direction == L && clone_pos < elevators[clone_floor]))
            cmd = B;

        if (cmd == W)
            if ((direction == R && clone_pos == width - 1) || (direction == L && clone_pos == 0))
                cmd = B;

        cout << cmd << endl;
    }
}
