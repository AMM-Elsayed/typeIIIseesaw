#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Author A.M.M. Elsayed
# Affilation: Department of Modern Physics, 
#              University of Science and Technology of China,
#              Hefei, China.

# Last update date: 2024/12/26

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# run " pip install -r requirements.txt " in terminal
# before start to ensure all required packages are installed

from plotting import *
from simulation import *
from analysis  import *


def all_plots():

    #production_cross_sections_plot()

    #cross_sections_ratio_plot()

    #branching_ratios_plot("+",1)

    #branching_ratios_plot("0",1)

    #branching_ratios_plot("+",2)

    #branching_ratios_plot("0",2)

    intermediate_states_cross_sections_plot(0,1)

    intermediate_states_cross_sections_plot(0,2)

    intermediate_states_cross_sections_plot(1,1)

    intermediate_states_cross_sections_plot(1,2)


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def main():

	# Step 1: generate and save simulation data

	# cross_section_calculations_run()

    # decay_width_calculations_run(0,0.063,0,1)

    #decay_width_calculations_run(0.00041,0.00041,0,2)

	# Step 2: Create relvant plots
    all_plots()

    # Step 3 (Optional): Ouput data 

    # first input : "+" for charged triplet, "0" for neutral triplet
    # second input: 1 for case 1, 2 for case 2 mixing
    # third and fourth input: "total_width" and "None" for total decay width, 
    #               "branching" and in forth input "z", or "h", or "w" for corresponding branching ratio
    #                                              "all_latex" for all branching rations in latex output
    #                                               "all_latex_without_mass" without mass

    # output_dranching_ratios_data("0",2,"branching","all_latex_without_mass")


    # input 0 for tr+ tr0, 1 for tr+ tr- and 2 for tr- tr0

    #output_cross_sections_data(2,"cross+unc")



if __name__ == "__main__":
    main()

    # 0 for tr+tr0, 1 for tr+tr-, 2 for tr-tr0 production cross sections data
    # this function is a list, [0] element is masses, [1] elements is cross sections, [2] is madgraph5 uncertanities 
    #print(production_cross_sections(0)[1])

    # print(partial_decay_widths("+","z",1)[1])

    #print(total_decay_widths("+",1))

    # print(branching_ratios("+","z",1))

    # 0 for tr+tr0 cross sections data
    # "z" for tr+ decay and "z" for tr0 decay
    # 1 for mixig case number
    #intermediate_states_cross_section(0,"z","z",1)
