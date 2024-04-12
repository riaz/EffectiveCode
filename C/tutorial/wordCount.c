#include <stdio.h>

#define IN  1    // outside a word
#define OUT 0    // inside a word

/* count lines, words and characters in input */
int main() {
    int c, nl, nw, nc, state; 

    state = OUT; // outide a word
    nl =  nw = nc = 0; // no line, word and character

    while((c = getchar()) != EOF) {
        ++nc;
        if (c == '\n') // this will increase the line count
            ++nl;
        if ( c == ' ' ||  c == '\n' ||  c == '\t' ) // this says out of word state
            state  = OUT;
        else if (state == OUT) { // this means we just encountered a word so we set state to IN.
            state = IN; // setting this prevents incrementing no words
            ++ nw;
        }
    }

    printf("No of lines: %d \nNo of words: %d \nNo of characters: %d \n", nl, nw, nc);
}