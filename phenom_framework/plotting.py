#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%   PLOTTING  %%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

from analysis import *
import matplotlib.pyplot as plt


def production_cross_sections_plot():
    
    colors = ["red", "green", "blue"]

    labels = [r"$N^+ N^0$", r"$N^+ N^-$", r"$N^- N^0$"]

    mass = production_cross_sections(0)[0]

    plt.figure(figsize=(9, 6))

    for production_process, color, label in zip([0,1,2], colors, labels):

        plt.errorbar(mass, production_cross_sections(production_process)[1], yerr=production_cross_sections(production_process)[2], 
            label=label, color=color,linestyle="-", marker="o", markersize=3)
    
    plt.xlabel(r"$M_N$ [GeV]",fontsize=16)
    plt.ylabel(r"$\sigma(pp \rightarrow NN) \, [\mathrm{fb}]$",fontsize=16)
    plt.yscale("log")
    plt.legend(loc='lower left', fontsize=16,frameon=False)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.tight_layout()

    inset_axes = plt.axes([0.55, 0.55, 0.42, 0.40])

    for production_process, color, label in zip([0,1,2], colors, labels):

        inset_axes.plot(mass[4:], production_cross_sections(production_process)[1][4:], label=label, color=color)

    inset_axes.set_xlabel(r"$M_N$ [GeV]", fontsize=11)
    inset_axes.set_ylabel(r"$\sigma [\mathrm{fb}]$", fontsize=11)
    inset_axes.tick_params(axis='both', which='major', labelsize=9)

    plt.savefig("plots/triplet_production_cross_sections.pdf", dpi=300)


def cross_sections_ratio_plot():

    mass = production_cross_sections(0)[0]

    plt.figure(figsize=(8, 6))

    plt.plot(mass, [i/j for i, j in zip(production_cross_sections(0)[1],production_cross_sections(1)[1])], label=r"$N^+N^-$", color="red")

    plt.plot(mass, [i/j for i, j in zip(production_cross_sections(0)[1],production_cross_sections(2)[1])], label=r"$N^-N^0$", color="blue")

    plt.xlabel(r"$M_N$ (GeV)", fontsize=16)

    plt.ylabel(r"$\frac{\sigma\left(pp\rightarrow N^+N^0\right)}{\sigma\left(pp\rightarrow N N\right)}$", fontsize=22)

    plt.legend(loc="best", fontsize=16, framealpha=1) # framealpha=1 makes the legend opaque

    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.axhline(y=1.4475, color="green", linestyle=":", linewidth=1.2)
    plt.text(1450,1.5, "Average = 1.4475", color="green", fontsize=12)

    plt.axhline(y=2.4024 , color="green", linestyle=":", linewidth=1.2)
    plt.text(1450,2.45, "Average = 2.4024", color="green", fontsize=12)

    plt.axhline(y=1.6728, color="purple", linestyle=":", linewidth=1.2)
    plt.text(1350,1.73, "Current Max = 1.6728", color="purple", fontsize=12)

    plt.axhline(y=3.4354, color="purple", linestyle=":", linewidth=1.2)
    plt.text(1350,3.47, "Current Max = 3.4354", color="purple", fontsize=12)

    plt.tight_layout()

    plt.savefig("plots/cross_section_ratios.pdf", dpi=300)


def branching_ratios_plot(charge,case_no):

    decay_boson_channels = ["z", "h", "w"]

    mass = partial_decay_widths(charge,"z",case_no)[0]

    colors = ["red", "green", "blue"]

    if charge == "+":

        if case_no == 1:

            labels = [r"$\mathrm{Br}\left(N^+ \rightarrow Z + \mu^+ \right)$", r"$\mathrm{Br}\left(N^+ \rightarrow H + \mu^+ \right)$", r"$\mathrm{Br}\left(N^+ \rightarrow \nu + W^+ \right)$"]

        elif case_no == 2:

            labels = [r"$\mathrm{Br}\left(N^+ \rightarrow Z + \ell^+ \right)$", r"$\mathrm{Br}\left(N^+ \rightarrow H + \ell^+ \right)$", r"$\mathrm{Br}\left(N^+ \rightarrow \nu + W^+ \right)$"]

    if charge == "0":

        if case_no == 1:

            labels = [r"$\mathrm{Br}\left(N^0 \rightarrow Z + \nu \right)$", r"$\mathrm{Br}\left(N^0 \rightarrow H + \nu\right)$", r"$\mathrm{Br}\left(N^0 \rightarrow W + \mu \right)$"]

        elif case_no == 2:

            labels = [r"$\mathrm{Br}\left(N^0 \rightarrow Z + \nu \right)$", r"$\mathrm{Br}\left(N^0 \rightarrow H + \nu\right)$", r"$\mathrm{Br}\left(N^0 \rightarrow W + \ell \right)$"]

    plt.figure(figsize=(12, 8))

    for decay_boson_channel, color, label in zip(decay_boson_channels, colors, labels):

        if charge == "+":

            plt.plot(mass[1:], branching_ratios(charge,decay_boson_channel,case_no)[1:], label=label, color=color,linestyle="-", marker="o", linewidth=3 ,markersize=6)

        elif charge == "0":

            plt.plot(mass, branching_ratios(charge,decay_boson_channel,case_no), label=label, color=color,linestyle="-", marker="o", linewidth=3 ,markersize=6)

    plt.xlabel(r"$M_N$ (GeV)", fontsize=25, labelpad=10)
    plt.ylabel(r"Branching Ratio", fontsize=25, labelpad=10)
    plt.legend(loc="upper right", fontsize=30, frameon=False)
    plt.tick_params(axis='both', which='major', labelsize=25, direction='in', length=6)
    plt.ylim(0, 1)

    if case_no == 1:

        plt.text(960,0.58, r"$V_e=V_\tau=0, V_\mu = 6.3\times 10^{-2}$", color="black", fontsize=26)

    elif case_no == 2:

        plt.text(960,0.58, r"$V_e=V_\mu = 4.1\times 10^{-4}, V_\tau=0$", color="black", fontsize=26)

    plt.tight_layout()
    plt.savefig(f'plots/branching_tr{charge}_case{case_no}.pdf', dpi=300)


def intermediate_states_cross_sections_plot(production_process,case_no):

    mass = production_cross_sections(0)[0]

    decay_boson_channels = ["z", "h", "w"]

    combinantations = [[c1,c2] for c1 in decay_boson_channels for c2 in decay_boson_channels]

    if production_process == 0:

        labels = [r"$Z\ell^+ Z\nu$",r"$Z\ell^+ H\nu$",r"$Z\ell^+ W^\pm \ell^\mp$",  
                                r"$H\ell^+ Z\nu$",r"$H\ell^+ H\nu$",r"$H\ell^+ W^\pm \ell^\mp$",  
                                            r"$W^+ \nu Z\nu$",r"$W^+ \nu H\nu$",r"$W^+ \nu W^\pm \ell^\mp$"]
        title = "N^+ N^0"

    elif production_process == 1:

        labels = [r"$Z\ell^+ Z\ell^-$",r"$Z\ell^+ H\ell^-$",r"$Z\ell^+ W^- \nu$",  
                                r"$H\ell^+ Z\ell^-$",r"$H\ell^+ H\ell^-$",r"$H\ell^+ W^- \nu$", 
                                            r"$W^+ \nu Z\ell^-$",r"$W^+ \nu H\ell^-$",r"$W^+ \nu W^- \nu$"]
        title = "N^+ N^-"

        colors = [] 

    plt.figure(figsize=(10, 6))

    start = 20

    for combinantation, label in zip(combinantations,labels):

        plt.plot(mass[start:],intermediate_states_cross_sections(production_process,combinantation[0],combinantation[1],case_no)[start:],label=label, linestyle='-',linewidth=2, marker="o", markersize=3)

        legend = plt.legend(loc="best", fontsize=15, frameon=False, ncol=3)


    plt.xlabel(r"$M_N$ (GeV)", fontsize=20, labelpad=10)
    plt.ylabel(rf"$ \sigma \left( pp \rightarrow {title} \rightarrow VfVf \right)$ [fb]", fontsize=20, labelpad=10)
    plt.yscale("log")

    #if case_no == 1:

     #   plt.text(1200,13, r"$V_e=V_\tau=0, V_\mu = 6.3\times 10^{-2}$", color="black", fontsize=16)

    #elif case_no == 2:

     #   plt.text(1200,9, r"$V_e=V_\mu = 4.1\times 10^{-4}, V_\tau=0$", color="black", fontsize=16)

    plt.tick_params(axis='both', which='major', labelsize=18, direction='in', length=6)
    plt.tick_params(axis='both', which='minor', direction='in', length=4)

    plt.tight_layout()
    plt.savefig(f"plots/intermediate_proc{production_process}_case{case_no}.pdf", dpi=300)

