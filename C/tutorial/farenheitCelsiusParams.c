#include <stdio.h>
#include <stdlib.h>

#define LOWER 0
#define UPPER 300
#define STEP 20

/* this program print a table to convert fahrenheit to celcius between 0 and 300 */
// depending on the number of arguments we will set lower upper step in that order

int main(int argc, char** argv) {

    float fahr, celsius;
    int lower, upper, step;

    // we can make use of a switch statement to make it easier
    // note we dont we dont use break for 4,3,2 as we will need all of them to be filled
    // this is a syntactic sugar 
    
    switch(argc) {
        case 4:
            step = atoi(argv[3]);           
        case 3:
            upper = atoi(argv[2]);  
        case 2:            
            lower = atoi(argv[1]); 
            break;
        default:
            lower = LOWER;
            upper = UPPER;
            step = STEP;
    }

    // printf("%d\t%d\t%d\n", lower, upper, step);
    fahr = lower;
    printf("Farenheit\tCelsius\n");
    
    while (fahr <= upper) {
        // using the conversion formulae here
        celsius = (5.0 / 9.0) * (fahr-32.0);
        printf("%3.0f\t\t%6.1f\n", fahr, celsius);
        fahr += step;
    }

}