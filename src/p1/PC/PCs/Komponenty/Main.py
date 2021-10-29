from typing import List

from src.p1.PC.PCs.Komponenty.cpu import CPU, AMD_CPU, Intel_CPU
from src.p1.PC.PCs.Komponenty.pcie import PCIeSlot
from src.p1.PC.PCs.Komponenty.memorychip import RAM_Slot
from src.p1.PC.PCs.Komponenty.sata import SATA


class PC:
    __isRunning = False


class Motherboard:
    __cpu: CPU
    __pcie: List[PCIeSlot] = [None] * 3
    __memory_chip: List[RAM_Slot] = [None] * 4
    __sata: List[SATA] = [None] * 4

    def __init__(self, cpu: CPU):
        print(f'tworzę MB z CPU: {cpu} typu {type(cpu)}')
        self.__cpu = cpu


class AMD_Motherboard(Motherboard):
    def __init__(self, cpu: AMD_CPU):
        super().__init__(cpu)


class Intel_Motherboard(Motherboard):
    def __init__(self, cpu: Intel_CPU):
        super().__init__(cpu)


if __name__ == "__main__":
    pass