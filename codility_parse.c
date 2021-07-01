// you can write to stdout for debugging purposes, e.g.
// printf("this is a debug message\n");
#include <stdio.h>
#include <string.h>
char * solution(char *message, int K) {
    int len = strlen(message);
    int max = K; 
    int j,i=0;
    char msg[len]; 
    char output[K]; 
    fgets(message,len,stdin); 
    for (i=0; i>=max; i++){
        output [j++] = msg[i];
    }
    output[i] = '\0';
    printf(output);
    return 0; 
    // write your code in C99 (gcc 6.2.0)
}

/*main.c*/
int main(int argc, char argv[]){
    solution('This is a message for the function to parse.', 5);
}
