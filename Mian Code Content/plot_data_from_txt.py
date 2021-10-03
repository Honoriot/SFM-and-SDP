"""----------This is a basic code to plot your resaults in pythjon for better represent----------"""
import matplotlib.pyplot as plt

r_f = []
FLOW_SFM = []
FLOW_SDP = []
AMS_PRESS = []

CANNULA_MODE = ["00", "0", "1", "2", "GREEN CPAP", "NO","ORANGE CPAP", "RED CPAP"]
FILE_MODE = ["00", "0", "1", "2", "GREEN_CPAP", "NO","ORANGE_CPAP", "RED_CPAP"]


def graph_plotter_2(data_1, data_2, data_3, data_4, xl, yl, CM):
    plt.plot(data_1, data_2, '.', data_3, data_4, '.')
    plt.xlabel(xl)
    plt.ylabel(yl)
    title = xl + " vs " + yl + CM
    plt.title(title)
    plt.savefig(GRAPH_FLODER_PATH + "\\" + title + ".png")
    plt.show()
    print("I had saved " + title)

def graph_plotter_1(data_1, data_2, xl, yl, CM):
    plt.plot(data_1, data_2, '.')
    plt.xlabel(xl)
    plt.ylabel(yl)
    title = xl + " vs " + yl + " " + CM
    plt.title(title)
    plt.savefig(GRAPH_FLODER_PATH + "\\" + title + ".png")
    plt.show()
    print("I had saved " + title)

def data_recoder():
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


for j in range(0, len(FILE_MODE)):
    FILE_NAME = "D:\\Kyron office\\AMS pressure data\\AMS pressure data\\Collected Data for Direct Connection of cannula to SFM output\\SFM_AMS_SDP_Press__" + FILE_MODE[j] +"_restrict.txt"
    GRAPH_FLODER_PATH = "D:\\Kyron office\\AMS pressure data\\AMS pressure data\\Collected Data for Direct Connection of cannula to SFM output\\Graphs\\" + CANNULA_MODE[j]
    GRAPH_MODE = {"GRAPH 1" : [r_f, FLOW_SDP, "R_F", "FLOW SDP", CANNULA_MODE[j]],                                                  # R_F vs FLOW SDP
              "GRAPH 2" : [r_f, FLOW_SFM, "R_F", "FLOW SFM", CANNULA_MODE[j]],                                                  # R_F vs FLOW SFM 
              "GRAPH 3" : [r_f, FLOW_SFM, r_f, FLOW_SDP, "R_F", "FLOW SFM(BLUE) SDP(ORANGE)", CANNULA_MODE[j]],                 # R_F vs FLOW SFM(BLUE) SDP(ORANGE),
              "GRAPH 4" : [AMS_PRESS, FLOW_SFM, "AMS PRESS", "FLOW SFM", CANNULA_MODE[j]],                                      # AMS PRESS vs FLOW SFM
              "GRAPH 5" : [AMS_PRESS, FLOW_SDP, "AMS PRESS", "FLOW SDP", CANNULA_MODE[j]],                                      # AMS PRESS vs FLOW SDP
              "GRAPH 6" : [AMS_PRESS, FLOW_SFM, AMS_PRESS, FLOW_SDP, "AMS PRESS", "FLOW SFM(BLUE) SDP(ORANGE)", CANNULA_MODE[j]],     # AMS PRESS vs FLOW SFM(BLUE) SDP(ORANGE)
              "GRAPH 7" : [r_f, AMS_PRESS, "R_F", "AMS PRESS", CANNULA_MODE[j]]}                                                # R_F PRESS vs AMS PRESS
    data_recoder()
    for i in GRAPH_MODE:
        if len(GRAPH_MODE[i])==5:
            graph_plotter_1(GRAPH_MODE[i][0], GRAPH_MODE[i][1], GRAPH_MODE[i][2], GRAPH_MODE[i][3], GRAPH_MODE[i][4])
        else:
            graph_plotter_2(GRAPH_MODE[i][0], GRAPH_MODE[i][1], GRAPH_MODE[i][2], GRAPH_MODE[i][3], GRAPH_MODE[i][4], GRAPH_MODE[i][5], GRAPH_MODE[i][6])
    

    r_f.clear()
    FLOW_SDP.clear()
    FLOW_SFM.clear()
    AMS_PRESS.clear()
