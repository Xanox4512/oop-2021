import re


class NVMeParser:
    def __init__(self, filename: str):
        self.data = open(filename).read()

    def parse(self):
        nvme_parameters_pattern = re.compile(r'(\w*)\s*:\s(.*)')
        parameters = nvme_parameters_pattern.findall(self.data)

        with open("NVMe_interesting_parameters", "r") as f:
            interesting_parameters = f.read().splitlines()

        final_result = {}
        for k, v in parameters:
            if k in interesting_parameters:
                final_result[k] = v

        return final_result


parser1 = NVMeParser("reader_examples/logs_nvme/nvme.txt")
print(parser1.parse())
