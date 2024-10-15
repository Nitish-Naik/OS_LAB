#include<fcntl.h>
#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<sys/mount.h>
#include<string.h>



// make dir
void example_mkdir() {
    if(mkdir("testdir", 0755) == -1) {
        perror("mkdir");
    }
    else {
        printf("Directory created successfully\n");
    }
}

// link and unlink 
void example_link_unlink() {
    if(link("oldfile", "newfile") == -1) {
        perror("link");
    }
    else {
        printf("Hard link created successfully\n");
    }

    if(unlink("newfile") == -1) {
        perror("unlink");

    }
    else {
        printf("file unlinked successfully");
    }
}

// mount and unmount

void example_mount_unmount() {
    if(mount("/workspaces/OS_LAB/filerelatedcalls/testdir/def", "/workspaces/OS_LAB/filerelatedcalls/yesdir", ".txt", 0, NULL) == -1) {
        perror("mount");
    }
    else {
        printf("Filesystem mounted successfully\n");
    }

    if (umount("/workspaces/OS_LAB/filerelatedcalls/yesdir") == -1) {
        perror("umount");
    } else {
        printf("Filesystem unmounted successfully\n");
    }
}

void example_chown_chmod() {
    if (chown("myfile", 1000, 1000) == -1) {
        perror("chown");
    } else {
        printf("Ownership changed successfully\n");
    }

    if (chmod("myfile", S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH) == -1) {
        perror("chmod");
    } else {
        printf("Permissions changed successfully\n");
    }
}


// 5. open, close, read, write, and lseek
void example_file_operations() {
    int fd = open("testfile", O_CREAT | O_RDWR, 0644);
    if (fd == -1) {
        perror("open");
        return;
    }

    char *data = "Hello, World!";
    if (write(fd, data, strlen(data)) == -1) {
        perror("write");
    }

    if (lseek(fd, 0, SEEK_SET) == -1) {
        perror("lseek");
    }

    char buffer[100];
    ssize_t bytes_read = read(fd, buffer, sizeof(buffer) - 1);
    if (bytes_read == -1) {
        perror("read");
    } else {
        buffer[bytes_read] = '\0';
        printf("Read from file: %s\n", buffer);
    }

    if (close(fd) == -1) {
        perror("close");
    }
}

void example_stat() {
    struct stat file_stat;
    if (stat("testfile", &file_stat) == -1) {
        perror("stat");
    } else {
        printf("File size: %ld bytes\n", file_stat.st_size);
        printf("File permissions: %o\n", file_stat.st_mode & 0777);
    }
}

// 7. sync
void example_sync() {
    sync();
    printf("File system synced\n");
}


// open 
void example_open() {
    int fd = open("foo.txt", O_RDONLY | O_CREAT);
    printf("file opened");
    printf("fd = %d\n ", fd);
    if(fd == -1) {
        printf("error occured");
    }
}
int main() {
     example_mkdir();
    example_link_unlink();
    example_mount_unmount();
    example_chown_chmod();
    example_file_operations();
    example_stat();
    example_sync();
    return 0;
}