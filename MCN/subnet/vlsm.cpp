#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>

using namespace std;

uint32_t ipToUInt(const string& ipStr) {
    uint32_t ip = 0;
    int octet;
    char dot;
    stringstream ss(ipStr);
    
    for (int i = 0; i < 4; ++i) {
        ss >> octet;
        ip = (ip << 8) | octet;
        if (i < 3) ss >> dot;
    }
    return ip;
}

string uintToIp(uint32_t ip) {
    stringstream ss;
    ss << ((ip >> 24) & 0xFF) << "."
       << ((ip >> 16) & 0xFF) << "."
       << ((ip >> 8) & 0xFF) << "."
       << (ip & 0xFF);
    return ss.str();
}

int main() {
    string baseIp;
    int baseCidr, numSubnets;

    cout << "Enter Base Network IP (e.g., 192.168.0.0): ";
    cin >> baseIp;
    cout << "Enter Base CIDR (e.g., 16): ";
    cin >> baseCidr;

    cout << "Enter number of subnets: ";
    cin >> numSubnets;

    vector<int> hosts(numSubnets);
    cout << "Enter required hosts for each subnet (space separated): ";
    for (int i = 0; i < numSubnets; ++i) {
        cin >> hosts[i];
    }

    sort(hosts.rbegin(), hosts.rend());

    uint32_t currentIp = ipToUInt(baseIp);

    cout << "\n--- VLSM Allocation Table ---\n";

    for (int i = 0; i < numSubnets; ++i) {
        int reqHosts = hosts[i];

        int blockSize = 1;
        while (blockSize < reqHosts + 2) {
            blockSize *= 2;
        }

        int subnetCidr = 32 - log2(blockSize);
        
        uint32_t subnetMask = 0xFFFFFFFF << (32 - subnetCidr);
        
        uint32_t broadcastIp = currentIp + blockSize - 1;

        cout << "Subnet " << i + 1 << " (Req: " << reqHosts << " hosts):" << endl;
        cout << "  Network:   " << uintToIp(currentIp) << " /" << subnetCidr << endl;
        cout << "  Mask:      " << uintToIp(subnetMask) << endl;
        cout << "  First IP:  " << uintToIp(currentIp + 1) << endl;
        cout << "  Last IP:   " << uintToIp(broadcastIp - 1) << endl;
        cout << "  Broadcast: " << uintToIp(broadcastIp) << endl;
        cout << "-------------------------------------------\n";

        currentIp += blockSize;
    }

    return 0;
}