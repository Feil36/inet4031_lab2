#include <stdio.h>

int main() {
    int a = 2;
    int b = 2;
    int c = a + b;

    printf("C says: Hello, World!\n");
    printf("%d + %d = %d\n", a, b, c);

    // Create an array 
    char* listOfUsers[] = {"User1", "User2", "User3"};
    int size = sizeof(listOfUsers) / sizeof(listOfUsers[0]);

    // For loop 
    for (int i = 0; i < size; i++) {
        printf("%s\n", listOfUsers[i]);
    }

    return 0;
}

