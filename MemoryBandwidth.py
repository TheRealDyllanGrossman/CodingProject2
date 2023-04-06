import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "myplot_memory_bandwidth.png"

# Create a dictionary with your data
data = {
    "Problem Sizes": [8388608, 16777216, 33554432, 67108864, 134217728, 268435456],
    "sum_direct_%_mem_bw": [0, 0, 0, 0, 0, 0],
    "sum_vector_%_mem_bw": [13.56291391, 13.94679719, 14.30760834, 14.3869162, 14.59924259, 15.17124834],
    "sum_indirect_%_mem_bw": [0.9980202845, 0.8923868789, 0.8149926007, 0.7765826028, 0.7589357575, 0.7499047043]
}

df = pd.DataFrame(data)
print(df)

var_names = list(df.columns)

print("var names =", var_names)

problem_sizes = df[var_names[0]].values.tolist()
code1_bw = df[var_names[1]].values.tolist()
code2_bw = df[var_names[2]].values.tolist()
code3_bw = df[var_names[3]].values.tolist()

plt.figure()

plt.title("Comparison of 3 Codes: % Memory Bandwidth Utilized")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

plt.plot(code1_bw, "r-o")
plt.plot(code2_bw, "b-x")
plt.plot(code3_bw, "g-^")

plt.xlabel("Problem Sizes")
plt.ylabel("% Memory Bandwidth Utilized")

varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

# save the figure before trying to show the plot
plt.savefig(plot_fname, dpi=300)

plt.show()
