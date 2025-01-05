#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%  DATA READING  %%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


import pandas as pd
import csv


def production_cross_sections(production_process):

    production_processes = ["tr+tr0", "tr+tr-", "tr-tr0"]

    reader = pd.read_csv(f'data/{production_processes[production_process]}.csv')

    return [[i for i in reader['mass']],[i for i in reader['cross_pb']],[i for i in reader['unc_pb']]]


def partial_decay_widths(charge,decay_boson_channel,case_no):

    reader = pd.read_csv(f'data/decays/tr{charge}_{decay_boson_channel}_decay_case{case_no}.csv')

    return [[i for i in reader['mass']],[i for i in reader['width']],[i for i in reader['unc_gev']]]


def total_decay_widths(charge,case_no):

    decay_boson_channels = ["z", "h", "w"]

    partial_decay_widths_list = [partial_decay_widths(charge,decay_boson_channel,case_no)[1] for decay_boson_channel in decay_boson_channels]

    if charge == "+":  # "tr+ > mu+ z", "tr+ > mu+ h", "tr+ > v w+"

        total_decay_width = [int(case_no)*i + int(case_no)*j + k for i, j, k in zip(partial_decay_widths_list[0],partial_decay_widths_list[1],partial_decay_widths_list[2])]

    elif charge == "0":  # "tr0 > v z", "tr0 > v h", "tr0 > mu+ w-"

        total_decay_width = [i + j + int(case_no)*2*k for i, j, k in zip(partial_decay_widths_list[0],partial_decay_widths_list[1],partial_decay_widths_list[2])]

    return total_decay_width


def branching_ratios(charge,decay_boson_channel,case_no):

    if charge == "+":

        branching_ratio = [i/j for i, j in zip(partial_decay_widths(charge,decay_boson_channel,case_no)[1],total_decay_widths(charge,case_no))]

    elif charge == "0":

        if decay_boson_channel == "w":

            branching_ratio = [2*i/j for i, j in zip(partial_decay_widths(charge,decay_boson_channel,case_no)[1],total_decay_widths(charge,case_no))]

        else:

            branching_ratio = [i/j for i, j in zip(partial_decay_widths(charge,decay_boson_channel,case_no)[1],total_decay_widths(charge,case_no))]

    return branching_ratio


def intermediate_states_cross_sections(production_process,ch1,ch2,case_no):

    if production_process == 0:

        intermediate_states_cross_section = [i * j * k for i, j, k in zip(production_cross_sections(production_process)[1],branching_ratios("+", ch1, case_no),branching_ratios("0", ch2, case_no))]

    if production_process == 1 or production_process == 2:

        intermediate_states_cross_section = [i * j * k for i, j, k in zip(production_cross_sections(production_process)[1],branching_ratios("+", ch1, case_no),branching_ratios("+", ch2, case_no))]

    return intermediate_states_cross_section

