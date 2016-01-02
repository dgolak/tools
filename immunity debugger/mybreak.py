import immlib
from immlib import *
import getopt
DESC = """Set breakpoint on some functions..."""

def usage():
  imm.log("!mybreak, no args")

def main(args):
 if args:
  usage()
 else:
  imm = Debugger()

  # debugger detect
  imm.setBreakpointOnName("Kernel32.IsDebuggerPresent")
  imm.setBreakpointOnName("Kernel32.CheckRemoteDebuggerPresent")
  imm.setBreakpointOnName("Kernel32.GetTickCount")

  # memory operation
  imm.setBreakpointOnName("kernel32.ReadProcessMemory")
  imm.setBreakpointOnName("kernel32.WriteProcessMemory")
  imm.setBreakpointOnName("kernel32.MapViewOfFile")
  imm.setBreakpointOnName("kernel32.VirtualProtect")
  imm.setBreakpointOnName("kernel32.VirtualProtectEx")
  imm.setBreakpointOnName("kernel32.VirtualQuery")
  imm.setBreakpointOnName("kernel32.VirtualQueryEx")
  imm.setBreakpointOnName("kernel32.LocalAlloc")
  imm.setBreakpointOnName("msvcrt.malloc")
  imm.setBreakpointOnName("msvcrt.memcpy")
  imm.setBreakpointOnName("ntdll.memcpy")

  # return handle to resource which args
  imm.setBreakpointOnName("Kernel32.FindResourceA")
  imm.setBreakpointOnName("Kernel32.FindResourceW")
  imm.setBreakpointOnName("kernel32.CreateRemoteThread")
  imm.setBreakpointOnName("kernel32.TerminateProcess")
  imm.setBreakpointOnName("kernel32.CreateProcessA")
  imm.setBreakpointOnName("kernel32.CreateProcessW")
  imm.setBreakpointOnName("msvcrt.exit")
  imm.setBreakpointOnName("kernel32.CreateThread")
  imm.setBreakpointOnName("kernel32.TerminateThread")
  imm.setBreakpointOnName("kernel32.ResumeThread")
  imm.setBreakpointOnName("kernel32.SuspendThread")
  imm.setBreakpointOnName("kernel32.Sleep")  #sleep stuff
  imm.setBreakpointOnName("kernel32.SleepEx")

  #file operation
  imm.setBreakpointOnName("kernel32.CreateFileA")
  imm.setBreakpointOnName("kernel32.CreateFileW")
  imm.setBreakpointOnName("kernel32.WriteFileEx")
  imm.setBreakpointOnName("kernel32.WriteFile")
  imm.setBreakpointOnName("kernel32.MoveFileA")
  imm.setBreakpointOnName("kernel32.MoveFileW")
  imm.setBreakpointOnName("kernel32.MoveFileExA")
  imm.setBreakpointOnName("kernel32.MoveFileExW")
  imm.setBreakpointOnName("kernel32.CopyFileA")
  imm.setBreakpointOnName("kernel32.CopyFileW")        

  #process
  imm.setBreakpointOnName("kernel32.ExitProcess")
  imm.setBreakpointOnName("kernel32.GetProcAddress")

  #loadLibrary
  imm.setBreakpointOnName("kernel32.LoadLibraryA")
  imm.setBreakpointOnName("kernel32.LoadLibraryW")
  imm.setBreakpointOnName("kernel32.DebugBreak")
  imm.setBreakpointOnName("kernel32.OutputDebugStringA")
  imm.setBreakpointOnName("kernel32.OutputDebugStringW")

  #registry
  imm.setBreakpointOnName("advapi32.RegCloseKey")
  imm.setBreakpointOnName("advapi32.RegCreateKeyExW")
  imm.setBreakpointOnName("advapi32.RegCreateKeyExA")
  imm.setBreakpointOnName("advapi32.RegDeleteKeyW")
  imm.setBreakpointOnName("advapi32.RegDeleteKeyA")
  imm.setBreakpointOnName("advapi32.RegDeleteValueW")
  imm.setBreakpointOnName("advapi32.RegDeleteValueA")
  imm.setBreakpointOnName("advapi32.RegEnumValueW")
  imm.setBreakpointOnName("advapi32.RegEnumValueA")
  imm.setBreakpointOnName("advapi32.RegOpenKeyExA")
  imm.setBreakpointOnName("advapi32.RegOpenKeyExW")
  imm.setBreakpointOnName("advapi32.RegQueryInfoKeyW")
  imm.setBreakpointOnName("advapi32.RegQueryInfoKeyA")
  imm.setBreakpointOnName("advapi32.RegQueryValueExW")
  imm.setBreakpointOnName("advapi32.RegQueryValueExA")
  imm.setBreakpointOnName("advapi32.RegQueryValueW")
  imm.setBreakpointOnName("advapi32.RegQueryValueA")
  imm.setBreakpointOnName("advapi32.RegSetKeySecurity")
  imm.setBreakpointOnName("advapi32.RegSetValueExW")
  imm.setBreakpointOnName("advapi32.RegSetValueExA")
  imm.setBreakpointOnName("advapi32.RegSetValueW")
  imm.setBreakpointOnName("advapi32.RegSetValueA")

  return "Set mybreakpoints..."
