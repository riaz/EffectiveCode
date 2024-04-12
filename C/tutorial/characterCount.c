#include <stdio.h>

/* count the number of characters in a input */

int main() {
    long nc = 0;

    // note we are not storing the value
    while (getchar() != EOF){
        nc += 1;
    }
    printf("No of characters : %ld\n", nc);
}