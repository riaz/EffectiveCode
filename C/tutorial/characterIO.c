#include <stdio.h>

/* We want to read a text file from cli and print its contents */
// make characterIO 
// ./obj/characterIO < files/sample1.txt

int main() {
    int c; // this can table more than just ascii keys
    while ((c = getchar()) != EOF) {
        putchar(c);    
    }
    putchar('\n');

    // Printing the value of EOF
    printf("%d\n", EOF);
}