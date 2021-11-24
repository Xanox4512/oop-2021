import re


class CPUMhzParser:

    def __init__(self, filename, freq_idle, freq_boosted):
        self.filedata = open(filename).read()

        self.freq_idle = freq_idle
        self.freq_boosted = freq_boosted

    def cpu_mhz(self):
        cpu_mhz_pattern = re.compile(r'cpu MHz\s*:\s(\d*.\d*)')
        mhz_match = cpu_mhz_pattern.findall(self.filedata)

        counter = {"idle": 0, "normal": 0, "boosted": 0}

        for match in mhz_match:
            if float(match) <= self.freq_idle:
                counter["idle"] += 1
            elif float(match) >= self.freq_boosted:
                counter["boosted"] += 1
            else:
                counter["normal"] += 1

        return {i: counter[i] / len(mhz_match) * 100 for i in ["idle", "boosted", "normal"]}


parser1 = CPUMhzParser("reader_examples/logs_cpu_mhz/ex1.txt", 800.017, 800.058)

print(parser1.cpu_mhz())