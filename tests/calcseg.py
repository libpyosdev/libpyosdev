from libpyosdev.math import ra, realmode_physaddr

print(hex(realmode_physaddr(0x100, 0)))
print(hex(realmode_physaddr(0x7E0, 0)))