#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
#include<string.h>

int main() {
    int fd = open("foo.txt", O_RDONLY);
    char data[20];
    if(fd < 0) {
        perror("error");
    }

    read(fd, data, 20);

    printf("I read this from the file: %s\n", data);
    close(fd);

    int file = open("def.txt", O_WRONLY | O_CREAT);
    char message[] = "Hello, World!";
    write(file, message, sizeof(message));
    close(file);
    printf("Message written to file!\n");
    return 0;
}