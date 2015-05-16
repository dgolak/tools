#include <windows.h>

#include<stdio.h>



INT WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
LPSTR lpCmdLine, int nCmdShow)
{

	char *buffer="c:\\Users\\IEUSER\\Downloads\\\soft\\wirusy\\test\\dll\\mydll.exe";

	DWORD processId;

	HWND hSaper = FindWindow("scanf",NULL);



	if(hSaper) //jezeli gra jest uruchomiona
    {

		GetWindowThreadProcessId(hSaper,&processId);
		HANDLE saper = OpenProcess( PROCESS_CREATE_THREAD |PROCESS_QUERY_INFORMATION |PROCESS_VM_OPERATION |PROCESS_VM_WRITE | PROCESS_VM_READ,FALSE,processId);

	if(saper){
		//	printf("sadasdsad");

		LPVOID addr = (LPVOID)GetProcAddress(GetModuleHandle("kernel32.dll"), "LoadLibraryA");

		if(addr == NULL) {

			MessageBox(NULL, "Cos", "Some", 0);

		}

		
LPVOID arg = (LPVOID)VirtualAllocEx(saper, NULL, strlen(buffer), MEM_RESERVE | MEM_COMMIT, PAGE_READWRITE);
 
		if(arg == NULL) {

			MessageBox(NULL, "Nie udalo sie zaalokowac pamieci", "Some", 0);

		}

		
/*
*Write the argument to LoadLibraryA to the process's newly allocated memory region.
*/

		int n = WriteProcessMemory(saper, arg, buffer, strlen(buffer), NULL);

		if(n == 0) {

			MessageBox(NULL, "Nie udalo sie zapisac do pamieci", "Some", 0);
		}
		HANDLE threadID = CreateRemoteThread(saper, NULL, 0, (LPTHREAD_START_ROUTINE)addr, arg, NULL, NULL);

		if(threadID == NULL) {

			MessageBox(NULL, "Nie udalo sie", "Some", 0);
			}else {
				MessageBox(NULL, "Sukces", "Some", 0);
			}
			MessageBox(NULL, "processId", "Some", 0);

		}else{
			MessageBox(NULL, "Nie mam procesu\n", "Some", 0);
		}

		MessageBox(NULL, "Gra jest uruchomiona\n", "Some", 0);

	}else{

		MessageBox(NULL, "Gra nie dziala\n", "Some", 0);

	}







	




/*	
HWND hSaper = FindWindow("Minesweeper",NULL);

	if(hSaper) //jezeli gra jest uruchomiona

	{

	GetWindowThreadProcessId(hSaper,&processId);


	MessageBox(NULL, "Gra jest uruchomiona\n", "Some", 0);

	}else{

	MessageBox(NULL, "Gra nie dziala\n", "Some", 0);

	}
*/



}




