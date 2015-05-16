#include <windows.h>

#include<stdio.h>



/* ******************************************
Load dll into process memory 
gcc change_fun.c -o change_fun
usage: change_fun [PID]
(need scanf.c/scanf as example)
****************************************** */



void main(int argc, char**argv){ 
	DWORD pid = (DWORD) atoi(argv[1]);
	char *buffer="c:\\Users\\IEUSER\\Downloads\\soft\\wirusy\\test\\dll\\mydll2.dll";

	HANDLE hproc = OpenProcess( PROCESS_CREATE_THREAD |PROCESS_QUERY_INFORMATION | PROCESS_VM_OPERATION |PROCESS_VM_WRITE | PROCESS_VM_READ,FALSE,pid);

	LPVOID addr = (LPVOID)GetProcAddress(GetModuleHandle("kernel32.dll"), "LoadLibraryA");
 
	if(addr == NULL){

		printf("Nie udalo sie ustalic adresu kernel32.LoadLibrabryA");
		exit(0);
	}

	LPVOID arg = (LPVOID)VirtualAllocEx(hproc, NULL, strlen(buffer), MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE);
	if(arg == NULL) {

		printf("Nie udalo sie zaalokowac pamieci w procesie %d", pid);
		exit(0);
	}

	int n = WriteProcessMemory(hproc, arg, buffer, strlen(buffer), NULL);
	if(n == 0) {

		printf("Nie udalo sie zaladowac dll %d", pid);
		exit(0);
	}

	HANDLE threadID = CreateRemoteThread(hproc, NULL, 0, (LPTHREAD_START_ROUTINE)addr, arg, 0, NULL);

	if(threadID ==NULL){
		printf("Nie udalo sie odpalic nowego watku");
		exit(0);
	}else{
		printf("Dll zaladowana!");
	}









	CloseHandle(hproc);




}





