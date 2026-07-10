#include <iostream>
using namespace std;

int main() {
    int ip[4], mask[4] = {0, 0, 0, 0}, net[4], brd[4];
    int cidr;
    char dot; 

    cout << "Enter IP address (e.g., 192.168.1.10): ";
    cin >> ip[0] >> dot >> ip[1] >> dot >> ip[2] >> dot >> ip[3];
    
    cout << "Enter CIDR notation (e.g., 26 for /26): ";
    cin >> cidr;

    int cidr_vals[] = {0, 128, 192, 224, 240, 248, 252, 254, 255};

    for (int i = 0; i < 4; i++) {
        if (cidr >= 8) {
            mask[i] = 255;
            cidr -= 8;
        } else {
            mask[i] = cidr_vals[cidr];
            cidr = 0;
        }
    }

    for (int i = 0; i < 4; i++) {
        net[i] = ip[i] & mask[i]; 
        
        brd[i] = net[i] | (255 - mask[i]); 
    }

    cout << "\n--- Subnet Details ---" << endl;
    cout << "Subnet Mask:       " 
         << mask[0] << "." << mask[1] << "." << mask[2] << "." << mask[3] << endl;
         
    cout << "Network Address:   " 
         << net[0] << "." << net[1] << "." << net[2] << "." << net[3] << endl;
         
    cout << "Broadcast Address: " 
         << brd[0] << "." << brd[1] << "." << brd[2] << "." << brd[3] << endl;

    return 0;
}