"""----------This is a basic code to plot your resaults in pythjon for better represent----------"""

from matplotlib import pyplot as plt

FILE_NAME = ".............\\SFM_AMS_SDP_Press__NO_restrict.txt"   # Change this according to your file location "C:\\user\\data.txt"

r_f = []
FLOW_SFM = []
FLOW_SDP = []
AMS_PRESS = []

try:
    File = open(FILE_NAME, 'r')
    if File.readable():
        while True:
            line_read = File.readline()
            while line_read == "\n":
                line_read = File.readline()
            if line_read == "":
                print("I am at end")
                break
            line_list = line_read.split()
            # print(line)
            r_f.append(float(line_list[1]))
            FLOW_SDP.append(float(line_list[7]))
            FLOW_SFM.append(float(line_list[5]))
            AMS_PRESS.append(float(line_list[9]))
        print(len(r_f), len(FLOW_SFM), len(FLOW_SDP), len(AMS_PRESS))
        File.close()
    else:
        print("Not readable content")
except FileNotFoundError:
    print("File Not Found::")


"""Modify the below according to your requirement as graph you want
    For more detail how to use matplotlib visit:: https://matplotlib.org/
    For more detail hoe to code python vist:: https://www.python.org/"""

# plt.plot(AMS_PRESS, FLOW_SDP, '.')
# # plt.plot(AMS_PRESS, FLOW_SDP, '.', AMS_PRESS, FLOW_SFM, '.',)
# plt.xlabel("AMS_PRESS")
# # plt.xlabel("FLOW SDP and FLOW SFM")
# plt.ylabel("FLOW SDP(BLUE)")
# plt.title("AMS PRESS vs FLOW SDP for NO in 30cm")
# plt.show()
