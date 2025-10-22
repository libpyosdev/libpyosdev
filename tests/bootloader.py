from libpyosdev.presets.x86_8086.bootloader import x86_8086_Bootloader

bl = x86_8086_Bootloader(output="tests/output/bootloader.asm")
bl.run()