import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "myplot_memory_latency.png"

# Create a dictionary with your data
data = {
    "Problem Sizes": [8388608, 16777216, 33554432, 67108864, 134217728, 268435456],
    "sum_direct_latency": [0, 0, 0, 0, 0, 0],
    "sum_vector_latency": [1.44e-10, 1.40e-10, 1.36e-10, 1.36e-10, 1.34e-10, 1.29e-10],
    "sum_indirect_latency": [1.96e-09, 2.19e-09, 2.40e-09, 2.51e-09, 2.57e-09, 2.60e-09]
}

df = pd.DataFrame(data)
print(df)

var_names = list(df.columns)

print("var names =", var_names)

problem_sizes = df[var_names[0]].values.tolist()
code1_latency = df[var_names[1]].values.tolist()
code2_latency = df[var_names[2]].values.tolist()
code3_latency = df[var_names[3]].values.tolist()

plt.figure()

plt.title("Comparison of 3 Codes: Memory Latency")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

plt.plot(code1_latency, "r-o")
plt.plot(code2_latency, "b-x")
plt.plot(code3_latency, "g-^")

plt.xlabel("Problem Sizes")
plt.ylabel("Memory Latency")

varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

# save the figure before trying to show the plot
plt.savefig(plot_fname, dpi=300)

plt.show()
