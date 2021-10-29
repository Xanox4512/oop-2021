from dataclasses import dataclass


@dataclass
class CPU:
    __frequency: int = 4000
    __cores: int = 16
    __cache: int = 128


class AMD_CPU(CPU):
    pass


class Intel_CPU(CPU):
    pass
