#include <stdio.h>

int main() {
    int vetor[100];
    
    for (int i = 0; i < 100; i++) {
        vetor[i] = i + 1;
    }
    
    for (int i = 99; i >= 0; i--) {
        printf("%d ", vetor[i]);
    }
    
    printf("\n");
    return 0;
}
