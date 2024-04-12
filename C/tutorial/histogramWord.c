#include <stdio.h>

/*
    Write a program to read a stream of text and print a histogram for alphabets only
*/

void render(int idx, int value) {
    printf("%c :", idx+97);
    for(int i=0;i < value; i++){
        printf("#");
    }
    printf("\n");
}

int main() {
    int c;

    int freq[26] = {0}; // all the 26 values will be set to 0 
    
    while((c = getchar()) != EOF) {
        //printf("%c\t%d", c, c);

        if(c >= 65 && c <= 90) // the character is uppercase
            c = c + 32;
        else if (c < 97 || c > 122)
            continue;        
        freq[c - 97] += 1;
    }



    // we need to print the graph next:
    for (int i=0;i<26;i++) {
        render(i, freq[i]);
        //printf("%d\n",freq[i]);
    }
}