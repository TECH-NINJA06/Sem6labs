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
    int acked[50] = {0}; 

    for (int i = 1; i <= total_frames; ) {
        for (int j = i; j < i + window_size && j <= total_frames; j++) {
            if (acked[j] == 0) {
                cout << "Sending Frame " << j << endl;
            }
        }

        for (int j = i; j < i + window_size && j <= total_frames; j++) {
            if (acked[j] == 0) {
                int ack = rand() % 4; 
                if (ack != 0) {
                    cout << "ACK received for Frame " << j << endl;
                    acked[j] = 1;
                } else {
                    cout << "ACK lost for Frame " << j << ". Will selectively repeat." << endl;
                }
            }
        }
        cout << endl;

        while (acked[i] == 1 && i <= total_frames) {
            i++;
        }
    }

    return 0;
}