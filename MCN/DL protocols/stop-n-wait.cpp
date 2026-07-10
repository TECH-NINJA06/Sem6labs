#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    int total_frames;
    cout << "Enter total number of frames to send: ";
    cin >> total_frames;

    srand(time(0));
    int current_frame = 1;

    while (current_frame <= total_frames) {
        cout << "Sending Frame " << current_frame << "..." << endl;
        
        int ack = rand() % 5; 
        
        if (ack == 0) {
            cout << "ACK lost for Frame " << current_frame << ". Retransmitting..." << endl << endl;
        } else {
            cout << "ACK received for Frame " << current_frame << "." << endl << endl;
            current_frame++;
        }
    }

    cout << "All frames sent successfully!" << endl;
    return 0;
}