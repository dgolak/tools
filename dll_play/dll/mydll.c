#include <windows.h>

BOOL WINAPI DllMain(HINSTANCE instance, DWORD reason, LPVOID reserved)
{
    switch(reason)
    {
    case DLL_PROCESS_ATTACH:
	MessageBox(0,"DLL zaladowana","komunikat",0);
    break;

    case DLL_PROCESS_DETACH:
	MessageBox(0,"DLL wyrzucona z pamieci","komunikat",0);
    break;
    }
    return TRUE;
}