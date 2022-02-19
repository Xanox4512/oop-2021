import re
from dataclasses import dataclass
from typing import List


@dataclass
class CpuMetric:
    temp: float
    vendor: str
    temp_high: float = 0


class CPUTempParser:

    @staticmethod
    def cpu_temp(filename) -> CpuMetric:
        with open(filename) as f:
            filedata = f.read()

        vendor = 'not recognized'
        temp = 0.0

        if CPUTempParser.is_intel(filedata):
            vendor = 'Intel'
            intel_temp_pattern = re.compile(r'Core\s\d*:\s*\+(\d*.\d*).*')
            temp = CPUTempParser.get_temperatures_from_string(filedata, intel_temp_pattern)

        if CPUTempParser.is_amd(filedata):
            vendor = 'AMD'
            for module_text in CPUTempParser.split_filedata_to_modules(filedata):
                if 'k10temp-pci-00c3' in module_text:
                    amd_temp_pattern = re.compile(r'.*\:\s*.(\d*\.\d*).*\s\(high\.*')
                    temp = CPUTempParser.get_temperatures_from_string(module_text, amd_temp_pattern)

        return CpuMetric(temp, vendor=vendor)

    @staticmethod
    def is_intel(content: str) -> bool:
        return 'coretemp-isa' in content

    @staticmethod
    def is_amd(content: str) -> bool:
        return 'k10temp-pci-00c3' in content

    @staticmethod
    def get_temperatures_from_string(filedata, pattern) -> float:
        temp_matches = [float(s) for s in pattern.findall(filedata)]
        temp = sum(temp_matches) / len(temp_matches)
        return temp

    @staticmethod
    def split_filedata_to_modules(filedata) -> List[str]:
        modules = filedata.split('\n\n')
        return modules




if __name__ == '__main__':
    parser = CPUTempParser()

    print(parser.cpu_temp('logs_cpu_temp/ex1.txt'))
    print(parser.cpu_temp('logs_cpu_temp/ex2.txt'))
    print(parser.cpu_temp('logs_cpu_temp/exX.txt'))

# https://docs.python.org/3/howto/regex.html
