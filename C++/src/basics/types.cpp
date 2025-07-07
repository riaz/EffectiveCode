#include <iostream>
#include <string>

using namespace std;

enum MealType {NO_PREF, VEG, VEGAN};

struct Passenger {
    string name;
    MealType mealPref;
    bool isFreqFlyer;
    string freqFlyerNum;
};

/* display a passenger type */
/* using pass by reference */
void displayPassenger(Passenger* pass) {
    cout << "Displaying Passenger Information" << endl;
    cout << "Name: " << pass->name << endl;
    cout << "Meal Type" << pass->mealPref << endl;
    cout << "Is Freq Flyer" << pass->isFreqFlyer << endl;
    cout << "Freq Flyer No" << pass->freqFlyerNum << endl;
}

int main(int c, char **argv) {
    short n;
    int octNumber = 0400;
    char newline = '\n';
    long bigNumber = 233L;

    // using enumerations
    enum Day{SUN, MON, TUE, WED, THU, FRI, SAT};

    Day today = SUN;
    
    cout << n << endl; // check the default value of n as 0
    cout << octNumber << endl;
    cout << newline << endl;
    cout << bigNumber << endl;

    // todays data
    cout << "Todays date: " << today << endl; // 0

    // pointer arithmetic 
    char ch = 'Q';
    char* a_ch = &ch; // a_ch holds the address of ch
    char v_ch = *a_ch; // v_ch holds the value of ch

    cout << ch << endl; // getting the original value
    cout << v_ch << endl; // this is the dereferenced value

    // replacing the value at address
    *a_ch = 'Z';
    cout << ch << endl; 

    // When using  pointer make sure to define each variable individually
    // int* a,b,c; -> int *a, int b, int c;
    // void* can be used to refer to pointer of any type but is not typesafe

    
    // Arrays
    // the size of the array is not mutable once declated this way
    double d_arr[5];
    int m[10];
    d_arr[0] = 19;
    m[2] = 0;

    cout << d_arr[m[2]] << endl; // should return 19

    // Declaring arrays
    int int_arr[] = {1,2,3};
    bool bool_arr[] = {true, false};
    char char_arr[] = {'r', 'i', 'a', 'z'};

    // array pointers
    char* char_pt = char_arr;
    char* q = &char_arr[0]; // address of the first element in the array

    cout << char_pt[2] << endl;
    // C++ assigns memory in sequence, so having the address to first element
    // makes it convenient to point to the next element.
    cout << q[2] << endl; 

    // using stl string
    string s = "hello world";
    string t = s + ", from C++";
    cout << t << endl;
    
    // using structs
    Passenger pass = {"John Smith", VEG, true, "1212"};

    // cout << pass << endl; - note this will not work
    displayPassenger(&pass);

    return 0;
}

