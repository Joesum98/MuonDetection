class DataFile:

    def __init__(self, fileName):
        self.topScint = []
        self.botScint = []
        self.name = ''.join(filter(str.isdigit, fileName))[6:]
        f = open(fileName, 'r')
        self.ke = float(self.name)
        if self.name == '0001':
            self.ke = 0.1
            self.name = '0.1'
        for line in f:
            self.topScint.append(float(line.split(' ')[3]))
            self.botScint.append(float(line.split(' ')[4]))
