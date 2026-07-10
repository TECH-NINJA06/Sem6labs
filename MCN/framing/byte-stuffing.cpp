#include <iostream>
#include <string>

using namespace std;

int main() {
    string data, stuffed = "";
    char flag = 'F'; 
    char esc = 'E';  

    cout << "Enter data string: ";
    cin >> data;

    stuffed += flag; 

    for (int i = 0; i < data.length(); i++) {
        if (data[i] == flag || data[i] == esc) {
            stuffed += esc;
        }
        stuffed += data[i];
    }

    stuffed += flag; 

    cout << "Framed Data: " << stuffed << endl;

    return 0;
}