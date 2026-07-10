#include <iostream>
#include <string>

using namespace std;

int main() {
    string data, stuffed = "";
    int count = 0;

    cout << "Enter binary data: ";
    cin >> data;

    for (int i = 0; i < data.length(); i++) {
        stuffed += data[i];
        
        if (data[i] == '1') {
            count++;
            if (count == 5) {
                stuffed += '0';
                count = 0; 
            }
        } else {
            count = 0;
        }
    }

    cout << "Framed Data: 01111110 " << stuffed << " 01111110" << endl;

    return 0;
}