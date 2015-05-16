#include <windows.h>


#include <stdio.h>

/* ****************
we run method adressed 0x00401560 with param
gcc -c mydll2.c
gcc -shared mydll2.o -Wall -L c:\gcc\lib -o mydll2.dll
**************** */
typedef void(__stdcall* pointer2method)(int);
pointer2method loadMethod = (pointer2method)0x00401560;


BOOL WINAPI DllMain(HINSTANCE instance, DWORD reason, LPVOID reserved)
{


	switch(reason)
{
		case DLL_PROCESS_ATTACH: //dll attached
	
		// MessageBox(0,"DLL loaded","Message",0);

			printf("DLL loaded to memory");
			loadMethod(2); // call method
			break;



		case DLL_PROCESS_DETACH:
 // process detached
//			MessageBox(0,"DLL removed","Message",0);

			printf("DLL removed");
			break;

	}
	return TRUE;

}
