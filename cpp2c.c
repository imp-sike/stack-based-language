#include<stdio.h>
#include<stdlib.h>

void checkArgs(int argc) {
  if(argc < 2 ) {
    printf("Error: Please enter valid no of args\n\n");
    printf("USAGE:\n a.out filename.cpp");
    exit(1);
  }
}

int main(int argc, char **argv) {
  checkArgs(argc);

  char *filename = argv[1];

  FILE  *sourceFile = fopen(filename, "r");

  char word[1024]; // max word length static 
  while(fscanf(sourceFile, "%1023s", word)  == 1) {
    puts(word);
  }

}
