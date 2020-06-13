import glob
from dataFile import DataFile
import matplotlib.pyplot as plt
import statistics
import numpy as np
from scipy import stats


def clearZeros(arr):
    arr[:] = (value for value in arr if value != 0.0)
    return arr


def listAverage(ent, tob):
    return sum(dict[ent][tob]) / len(dict[ent][tob])


folderPath = 'C:/Users/JoeSum98/Documents/Code/Python/PycharmProjects/MuonDetectors/DetectorData/Mu-/1-100MeV/*.txt'
filePath = 'C:/Users/JoeSum98/Documents/Code/Python/PycharmProjects/MuonDetectors/DetectorData/Mu+/1-100GeV/1Gev.txt'
dict = {}
topData = []
botData = []
topEr = []
botEr = []


# # 1.) CREATE SCATTER PLOTS OF AVERAGE ENERGY DEPOSITED VS INCIDENT ENERGY
# plt.title("Mu- (1-100MeV)")
# plt.xlabel("Incident Energy (MeV)")
# plt.ylabel("Mean Energy Deposit (MeV)")
# plt.ylim(0, 12)
#
# for fileName in glob.glob(folderPath, recursive=True):
#     temp = DataFile(fileName)
#     dict.update({temp.name: [clearZeros(temp.topScint), clearZeros(temp.botScint)]})
#
# # topData.append((0, 0))
# # botData.append((0, 0))
# # topEr.append((0, 0))
# # botEr.append((0, 0))
#
# for entry in dict:
#     avgTop = listAverage(entry, 0)
#     avgBot = listAverage(entry, 1)
#     stdErrTop = statistics.pstdev(dict[entry][0])/2
#     stdErrBot = statistics.pstdev(dict[entry][1])/2
#     topData.append((float(entry), avgTop))
#     topEr.append((float(entry), stdErrTop))
#     botData.append((float(entry), avgBot))
#     botEr.append((float(entry), stdErrBot))
#
# topData.sort(key=lambda x: x[0])
# botData.sort(key=lambda x: x[0])
#
# plt.scatter(*zip(*topData), label="Top Scintillator", color='C0')
# plt.scatter(*zip(*botData), label="Bottom Scintillator", color='C1', alpha=.7)
# for i in range(0, len(topData)):
#     plt.errorbar(topData[i][0], topData[i][1], yerr=topEr[i][1], color='C3', alpha=.7)
# for i in range(0, len(botData)):
#     plt.errorbar(botData[i][0], botData[i][1], yerr=botEr[i][1], color='C3', alpha=.7)
#
# plt.legend()
# plt.show()


# 2.) CREATE BAR GRAPHS FOR # OF TRIGGERS VS Energy Deposited
plt.title("Energy Deposit for 1.0 Gev Mu+")
plt.xlabel("Energy Deposit (MeV)")
plt.ylabel("# of Events")

topTriggers = {}
botTriggers = {}

data = DataFile(filePath)
data.topScint = clearZeros(data.topScint)
data.botScint = clearZeros(data.botScint)
for event in data.topScint:
    event = round(event, 2)
    if event in topTriggers:
        topTriggers[event] = topTriggers[event]+1
    else:
        topTriggers.update({event: 1})

for event in data.botScint:
    event = round(event, 2)
    if event in botTriggers:
        botTriggers[event] = botTriggers[event]+1
    else:
        botTriggers.update({event: 1})

topData = sorted(topTriggers.items())
botData = sorted(botTriggers.items())

plt.bar(*zip(*topData), width=0.02, label="Top Scintillator", align='center')
plt.bar(*zip(*botData), width=0.02, label="Bottom Scintillator", align='center', alpha=0.7)
plt.yscale("log")
l1 = list(zip(*topData))
l2 = list(zip(*botData))
topString = "Avg. Upper Energy Deposit: " + str(round(sum(l1[0])/len(topData), 4)) + "MeV"
botString = "Avg. Lower Energy Deposit: " + str(round(sum(l2[0])/len(botData), 4)) + "MeV"
plt.annotate(topString, xy=(4, 10), xytext=(3.7, 10))
plt.annotate(botString, xy=(4, 8), xytext=(3.7, 8))
plt.legend()
plt.show()

# 3.) CREATE ENERGY DISTRIBUTION PLOTS FOR DIFFERENT ENERGY LEVELS
# plt.title("Mu- 47GeV Energy Distribution")
# plt.xlabel("Incident Energy (MeV)")
# plt.ylabel("Density")
#
# for fileName in glob.glob(filePath):
#     temp = DataFile(fileName)
#     for m in temp.topScint:
#         topData.append(m)
#     for n in temp.botScint:
#         botData.append(n)
#
# topData = clearZeros(topData)
# botData = clearZeros(botData)
#
# topSample = np.hstack(topData)
# botSample = np.hstack(botData)
# topDensity = stats.kde.gaussian_kde(topSample)
# botDensity = stats.kde.gaussian_kde(botSample)
# x = np.arange(0, 15, 0.1)
#
# plt.plot(x, topDensity(x), color='C0')
# plt.plot(topSample, [0.01]*len(topSample), '|', color='C0')
# plt.plot(x, botDensity(x), color='C1')
# plt.plot(botSample, [0.01]*len(botSample), '|', color='C1')
#
# plt.show()

plt.close()
