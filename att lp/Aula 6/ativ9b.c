#include <stdio.h>

double circCirculo(int raio) {
    if (raio <= 0) {
        printf("Erro: O raio deve ser um valor positivo maior que zero.\n");
        return -1; 
    }
    return 2 * 3.14 * raio;  // Fórmula da circunferência
}

int main() {
    int raio = 3;
    double resultado = circCirculo(raio);
    
    printf("A circunferência do círculo com raio %d é: %.2f\n", raio, resultado);


}