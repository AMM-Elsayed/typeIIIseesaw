#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%  DATA PRINTING  %%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


from analysis import *
import math


def sep_exp(num):

    exponent_base10 = math.floor(math.log10(abs(float(num))))
    mantissa_base10 = float(num) / (10**exponent_base10)
    return [format(mantissa_base10,'.3f'),int(exponent_base10)]


def output_cross_sections_data(process,data_type):

    process_names = ["tr+tr0", "tr+tr-", "tr-tr0"]

    reader = pd.read_csv(f'data/{process_names[process]}.csv')

    mass = reader["mass"].to_numpy()[:, None]

    cross_pb = reader["cross_pb"].to_numpy()[:, None]

    unc_pb = reader["unc_pb"].to_numpy()[:, None]

    if data_type == "cross":
        for i in zip(cross_pb):
            print(float(i[0]))

    elif data_type == "cross+unc":
        for j,k in zip(cross_pb,unc_pb):
            print("& $ \\left(",sep_exp(j[0])[0],"\\pm",sep_exp(k[0])[0]," \\times 10^{",sep_exp(k[0])[1]-sep_exp(j[0])[1],"}\\right)\\times 10^{",sep_exp(j[0])[1],"} $ \\\\")

    elif data_type == "mass+cross+unc":
        for i,j,k in zip(mass,cross_pb,unc_pb):
            print("$",int(i[0]),"$ & $ \\left(",sep_exp(j[0])[0],"\\pm",sep_exp(k[0])[0]," \\times 10^{",sep_exp(k[0])[1]-sep_exp(j[0])[1],"}\\right)\\times 10^{",sep_exp(j[0])[1],"} $")


def output_dranching_ratios_data(charge,case_no,data_type,decay_channel):

    processes_names = [f'tr{charge}_z_decay_case{case_no}', f'tr{charge}_h_decay_case{case_no}', f'tr{charge}_w_decay_case{case_no}']

    reader_z = pd.read_csv(f'data/decays/{processes_names[0]}.csv')

    reader_h = pd.read_csv(f'data/decays/{processes_names[1]}.csv')

    reader_w = pd.read_csv(f'data/decays/{processes_names[2]}.csv')

    partial_width_z = reader_z["width"].to_numpy()[:, None]

    partial_width_h = reader_h["width"].to_numpy()[:, None]

    partial_width_w = reader_w["width"].to_numpy()[:, None]

    mass = reader_z["mass"].to_numpy()[:, None]

    if charge == "+":

        total_decay_width = [int(case_no)*float(i)+int(case_no)*float(j)+float(k) for i, j, k in zip(partial_width_z,partial_width_h,partial_width_w)]

        branching_ratios=[]

        for processes in processes_names:
            reader = pd.read_csv(f'data/decays/{processes}.csv')
            partial_width = reader["width"].to_numpy()[:, None]
            branching_ratios.append([format(round(float(i)/float(j)*100,4),'.4f') for i, j in zip(partial_width,total_decay_width)])

    elif charge == "0":

        total_decay_width = [float(i)+float(j)+int(case_no)*2*float(k) for i, j, k in zip(partial_width_z,partial_width_h,partial_width_w)]

        branching_ratios=[]

        for decay_proc in processes_names:
            reader = pd.read_csv(f'data/decays/{decay_proc}.csv')
            partial_width = reader["width"].to_numpy()[:, None]
            if decay_proc == processes_names[2]:
                branching_ratios.append([format(round(2*float(i)/float(j)*100 ,4),'.4f')for i, j in zip(partial_width,total_decay_width)])
            else:
                branching_ratios.append([format(round(float(i)/float(j)*100 ,4),'.4f') for i, j in zip(partial_width,total_decay_width)])

    if data_type == "total_width" and decay_channel == None:
        for i, j in zip(mass,total_decay_width):
            print(i,":",round(j*1000,3))
    elif data_type == "branching" and decay_channel == "z":
        for i, j in zip(mass,branching_ratios[0]):
            print(i,":",j)
    elif data_type == "branching" and decay_channel == "h":
        for i, j in zip(mass,branching_ratios[1]):
            print(i,":",j)
    elif data_type == "branching" and decay_channel == "w":
        for i, j in zip(mass,branching_ratios[2]):
            print(i,":",j)
    elif data_type == "branching" and decay_channel == "all_latex":
        for i,j,k,l in zip(mass,branching_ratios[0],branching_ratios[1],branching_ratios[2]):
            print("$",i[0],"$ & $",j,"\\% $ & $",k,"\\% $ & $",l,"\\% $ &")
    elif data_type == "branching" and decay_channel == "all_latex_without_mass":
        for j,k,l in zip(branching_ratios[0],branching_ratios[1],branching_ratios[2]):
            print("$",j,"\\% $ & $",k,"\\% $ & $",l,"\\% $ \\\\")

