#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

char * cipher(int k, char p[]);

int main(void) {
    int key;
    char plain[1024];
    const int l = strlen(plain);
    printf("Key: ");
    scanf(" %i", &key);
    while (getchar() != '\n');
    printf("Plaintext: ");
    fgets(plain, 1024, stdin);
    printf("Ciphertext: %s", cipher(key, plain));
}

char * cipher(int k, char p[]) {
    const int l = strlen(p);
    char *cipher_text = malloc((l + 1) * sizeof(char));
    for (int i = 0; i < l; i++) {
       if (isalpha(p[i]) == 0){
        cipher_text[i] = p[i];
       }
       else {
            if (islower(p[i]) > 0) {
                cipher_text[i] = tolower(p[i]) + k;
                if (cipher_text[i] > 122) {
                    cipher_text[i] -= 26;
                }
            }
            else {
                cipher_text[i] = toupper(p[i]) + k;
                if (cipher_text[i] > 90) {
                    cipher_text[i] -= 26;
                }                
            }
       }
    }
    cipher_text[l] = '\0';
    return cipher_text;
    free(cipher_text);
}