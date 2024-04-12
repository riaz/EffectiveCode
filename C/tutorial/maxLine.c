#include <stdio.h>

#define MAXLINE 1000 // max size of a line

int getLine(char[], int);
void copy(char[], char[]);

/* print the longest line */
int main() {
    int len;
    int max;
    char line[MAXLINE];    // save the current line
    char longest[MAXLINE];  // save the longest line

    max = 0; 
    while ((len = getLine(line, MAXLINE)) > 0)
        if (len > max) {
            max = len;
            copy(line, longest);                        
        }   

    if (max > 0) // there was a line, print the longest
        printf("%s", longest);        
    
}


/* getline: read a line in s, return length */
int getLine(char s[], int lim) {
    
    int c, i;

    for(i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; i++)
        s[i] = c;
    // we will further check if the final character was \n
    // and incorporate that in the output
    if (c == '\n'){
        s[i] =  c;
        i++;
    }
    
    s[i] = '\0';
    return i;    
}

/* copy from a to array */
void copy(char from[], char to[]) {
    int i = 0;
    while((to[i] = from[i]) != '\0')
        ++i;
}