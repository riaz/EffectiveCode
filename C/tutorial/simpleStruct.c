#include <stdio.h>

struct SimpleStruct {
    int myNum;
    char myLetter;
};

int main() {
    // create a structure variable
    struct SimpleStruct s1;

    // assign values to members
    s1.myNum = 19;
    s1.myLetter = 'A';

    // printing the values
    printf("My number: %d\n", s1.myNum);
    printf("My letter: %c\n", s1.myLetter);
}