#include<windows.h>
#include<stdio.h>

//22fe0c - adres wartosci myint;

fun1(int ile){
int myint=12+ile;
char name[128];
printf("\nJestem w fun fun1.\nWartosc myint=%d adres: %x\n",myint,&myint);

scanf("%s",name);
printf("\nJestem w fun fun1.\nWartosc myint=%d adres: %x\n", myint,&myint);

}


main(){
char name[128];
int i=10;
printf("\nWpisz stringa:");
fun1(i);


}