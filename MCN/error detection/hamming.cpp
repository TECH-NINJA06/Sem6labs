#include <iostream>

using namespace std;

int main() {
    int d[4], h[7];
    
    cout << "Enter 4 data bits (space separated): ";
    cin >> d[0] >> d[1] >> d[2] >> d[3];

    h[2] = d[0]; 
    h[4] = d[1];
    h[5] = d[2]; 
    h[6] = d[3];

    h[0] = h[2] ^ h[4] ^ h[6];
    h[1] = h[2] ^ h[5] ^ h[6]; 
    h[3] = h[4] ^ h[5] ^ h[6]; 

    cout << "7-bit Hamming Code: ";
    for(int i = 0; i < 7; i++) {
        cout << h[i] << " ";
    }
    cout << endl;

    return 0;
}