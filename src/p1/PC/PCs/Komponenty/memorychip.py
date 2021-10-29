from dataclasses import dataclass


@dataclass
class RAM_MEM:
    pass


class RAM_Slot:
    __ram: RAM_MEM

    def insert_ram(self, ram: RAM_MEM):
        self.__ram = ram

    def get_ram(self) -> RAM_MEM:
        return self.__ram

    def remove_ram(self):
        self.__ram = None