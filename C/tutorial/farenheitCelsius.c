#include <stdio.h>

/* this program print a table to convert fahrenheit to celcius between 0 and 300 */

int main() {

    int fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20; // we will step every 20 values

    fahr = lower;
    printf("Farenheit\tCelsius\n");
    while (fahr <= upper) {
        // using the conversion formulae here
        celsius = 5 * (fahr-32) / 9;
        printf("%d\t\t%d\n", fahr, celsius);
        fahr += step;
    }

}