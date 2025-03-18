# import ctypes, utility
# from ctypes import wintypes
# from consts import *

# kernel32 = ctypes.windll.kernel32

# pid = utility.GetProcId("ac_client.exe")
# handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, 0, ctypes.wintypes.DWORD(pid))
# base_address = utility.GetModuleBaseAdress(pid, "ac_client.exe")

# ammo_decrement = base_address + 0xC73EF
# utility.nopBytes(handle, ammo_decrement, 2)

# current_ammo_base = base_address + 0x0016F338
# current_ammo_address = utility.FindDMAAddy(handle, current_ammo_base, [0x0, 0xB8, 0x140], 32)
# kernel32.WriteProcessMemory(handle, current_ammo_address, ctypes.byref(ctypes.c_int(1337)), ctypes.sizeof(ctypes.c_int), None)
# kernel32.CloseHandle(handle)

# sets ammo to 1337
import pymem, utility
# pulls the process by name.
process = pymem.Pymem("ac_client.exe")
# Gets the base address of the process and adds that to the address of the ammo base
current_ammo_base = process.base_address + 0x0016F338
# Gets the base address of the process and adds that to the address of the ammo that decrements when shooting
ammo_decrement = process.base_address + 0xC73EF
# gets the current ammo
current_ammo = utility.FindDMAAddy(process.process_handle, current_ammo_base, [0x0, 0xB8, 0x140], 32)
# changes how the ammo decrements 
process.write_bytes(ammo_decrement, b"\x90\x90", 2)
# sets the ammo to 1337
process.write_int(current_ammo, 1337)