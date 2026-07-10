#include <iostream>
using namespace std;

int main() {
    int n, sum = 0;
    
    cout << "Enter number of data segments: ";
    cin >> n;

    int data[n];
    cout << "Enter " << n << " data segments: ";
    for (int i = 0; i < n; i++) {
        cin >> data[i];
        sum += data[i];
    }

    int checksum = ~sum; 
    
    cout << "\n--- SENDER SIDE ---" << endl;
    cout << "Sum: " << sum << endl;
    cout << "Generated Checksum: " << checksum << endl;

    cout << "\n--- RECEIVER SIDE ---" << endl;
    int received_sum = 0;
    
    cout << "Enter received data segments: ";
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        received_sum += temp;
    }
    
    int received_checksum;
    cout << "Enter received checksum: ";
    cin >> received_checksum;

    int final_sum = received_sum + received_checksum;
    
    int final_result = ~final_sum;

    cout << "\nFinal Result after 1's complement: " << final_result << endl;

    if (final_result == 0) {
        cout << "Status: Data accepted. No error detected." << endl;
    } else {
        cout << "Status: Data rejected. Error detected!" << endl;
    }

    return 0;
}