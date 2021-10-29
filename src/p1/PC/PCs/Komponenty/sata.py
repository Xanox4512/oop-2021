from dataclasses import dataclass

@dataclass
class SATADevice:
    pass

class SATA:
    __drive: SATADevice

    def insert_drive(self, drive: SATADevice):
        self.__drive = drive

    def get_drive(self) -> SATADevice:
        return self.__drive

    def remove_drive(self):
        self.__drive = None



class ComputerDrive(SATADevice):
    __capacity: int
    __read_write_speed: int

class SeagateHDD(ComputerDrive):
    pass

class AdataSSD(ComputerDrive):
    pass