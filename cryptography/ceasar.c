#include <stdio.h>
#include <string.h>
#include <ctype.h>

char * cipher(int k, char * p);

int main(void) {
    int key;
    char *plain;
    const int l = strlen(plain);
    printf("Key: ");
    scanf("%i", &key);
    printf("Plaintext: ");
    scanf("%s", plain);
    printf("Ciphertext: %s", cipher(key, plain));
}

char * cipher(int k, char * p) {
    int l = strlen(p);
    char * cipher;
    for (int i = 0; i < l; i++) {
       cipher[i] = tolower(p[i]) + k;
        if (cipher[i] > 122) {
            cipher[i] -= 26;
        }
    }
    return cipher;
}