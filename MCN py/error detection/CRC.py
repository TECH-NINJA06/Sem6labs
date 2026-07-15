#include <iostream>
#include <string>

using namespace std;

int main() {
    string data, gen;
    cout << "Enter Data bits: "; 
    cin >> data;
    cout << "Enter Generator bits: "; 
    cin >> gen;

    string div = data;
    for(int i = 0; i < gen.length() - 1; i++) {
        div += '0';
    }

    for(int i = 0; i <= div.length() - gen.length(); ) {
        for(int j = 0; j < gen.length(); j++) {
            div[i+j] = (div[i+j] == gen[j]) ? '0' : '1';
        }
        while(i < div.length() && div[i] != '1') {
            i++;
        }
    }

    string crc = div.substr(data.length());
    cout << "Generated CRC: " << crc << endl;
    cout << "Transmitted Data: " << data + crc << endl;
    
    return 0;
}