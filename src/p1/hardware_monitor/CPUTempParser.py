import re


class CPUTempParser:

    def __init__(self, filename):
        self.fiiledata = open(filename).read()

    def cpu_temp(self):

        intel_temp_pattern = re.compile(r'Core\s\d*:\s*\+(\d*.\d*).*')
        amd_temp_pattern = re.compile(r'Tdie:\s*.(\d*\.\d*).*')

        temp = 0.0

        temp_matches = amd_temp_pattern.findall(self.filedata) or intel_temp_pattern.findall(self.filedata)

        #print(bool(amd_temp_pattern.findall(self.filedata)))

        for match in temp_matches:
            temp += float(match) / len(temp_matches)

        return temp


parser1 = CPUTempParser("reader_examples/logs_cpu_temp/AMDTemp.txt")
print(parser1.cpu_temp())

parser2 = CPUTempParser("reader_examples/logs_cpu_temp/IntelTemp.txt")
print(parser2.cpu_temp())

#https://docs.python.org/3/howto/regex.html

