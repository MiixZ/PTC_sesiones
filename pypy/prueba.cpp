#include <iostream>
#include <chrono>

using namespace std;
using namespace chrono;

int main() {
    auto t1 = high_resolution_clock::now();
    int sum = 0;
    for (int k = 0; k < 1000; k++) {
        sum += k;
    }
    auto t2 = high_resolution_clock::now();
    double t = duration<double>(t2 - t1).count();
    cout << "Sum of 1000 numbers is: " << sum << endl;
    cout << "Elapsed time is: " << t << " seconds" << endl;
    
    return 0;
}
