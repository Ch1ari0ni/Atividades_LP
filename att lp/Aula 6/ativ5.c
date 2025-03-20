#include <stdio.h>
#include <string.h>

int main () {
    char original[] = "Cyber SENAI 2025"; // string 
    char extraida [6]; // Vetor para "SENAI" + '\0'

    int j = 0;
    for (int i = 6; i < 11; i++) { // copiando apenas "SENAI"
        extraida[j] = original[i];
        j++;
    }
    extraida[j] = '\0'; // add o caractere nulo no final

    printf("%s\n", extraida); // exibe "SENAI"

    return 0;
}