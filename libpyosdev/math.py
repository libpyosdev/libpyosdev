def realmode_physaddr(offset: int, segment: int):
    return offset * 16 + segment