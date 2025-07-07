#include <iostream>

using namespace std;

int main(int c, char **argv){
    int x, y;
    cout << "Please enter two numbers" << endl;
    cin >> x >> y;
    int sum = x + y;
    cout << "Their sum is: " << sum << endl;
    return EXIT_SUCCESS;
}