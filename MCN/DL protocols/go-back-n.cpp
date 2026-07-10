#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    int total_frames, window_size;
    cout << "Enter total frames: ";
    cin >> total_frames;
    cout << "Enter window size: ";
    cin >> window_size;

    srand(time(0));
    int i = 1;

    while (i <= total_frames) {
        int x = 0;
        for (int j = i; j < i + window_size && j <= total_frames; j++) {
            cout << "Sending Frame " << j << endl;
        }

        for (int j = i; j < i + window_size && j <= total_frames; j++) {
            int ack = rand() % 4; 
            if (ack == 0) {
                cout << "ACK lost for Frame " << j << ". Going back to " << j << "..." << endl << endl;
                x = j;
                break; 
            } else {
                cout << "ACK received for Frame " << j << endl;
            }
        }

        if (x == 0) { 
            i += window_size;
            cout << endl;
        } else { 
            i = x; 
        }
    }
    
    return 0;
}