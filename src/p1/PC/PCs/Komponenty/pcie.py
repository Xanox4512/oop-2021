from dataclasses import dataclass


@dataclass
class PCIeDevice:
    __gen: int = 4


class PCIeSlot:
    __gen: int = 4
    __device: PCIeDevice

    def insert_device(self, device: PCIeDevice):
        self.__device = device

    def get_device(self) -> PCIeDevice:
        return self.__device

    def remove_device(self):
        self.__device = None


class GraphicsCard(PCIeDevice):
    __cores: int
    __frequency: int
    __memory_gb: int


class NvidiaGraphicsCard(GraphicsCard):
    pass
