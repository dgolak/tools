#include <windows.h>

#include<stdio.h>



/* **********************
We change value of variable in the memory
usage: ./base [PID]
********************** */

//fun1(){
//	printf("Jestem w fun1");
//}



void main(int argc, char**argv){ 
	int adres=0x22fe0c; // variable address to change
	int wartosc=5;


	DWORD pid = (DWORD) atoi(argv[1]);

	HANDLE hproc = OpenProcess( PROCESS_CREATE_THREAD |PROCESS_QUERY_INFORMATION |PROCESS_VM_OPERATION |PROCESS_VM_WRITE | PROCESS_VM_READ,FALSE,pid);


	WriteProcessMemory(hproc, (LPVOID) adres, &wartosc, sizeof(int), 0);


	CloseHandle(hproc);

//	__asm(
//".globl _fun1"
//);
}





