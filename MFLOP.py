import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "myplot_mflops.png"

# Create a dictionary with your data
data = {
    "Problem Sizes": [8388608, 16777216, 33554432, 67108864, 134217728, 268435456],
    "sum_direct_MFLOPs": [14074.84564, 13718.0834, 14068.94423, 14054.21236, 14045.38803, 14057.89243],
    "sum_vector_MFLOPs": [3472.10596, 3570.380081, 3662.747735, 3683.050546, 3737.406104, 3883.839574],
    "sum_indirect_MFLOPs": [255.4931928, 228.451041, 208.6381058, 198.8051463, 194.2875539, 191.9756043]
}

df = pd.DataFrame(data)
print(df)

var_names = list(df.columns)

print("var names =", var_names)

problem_sizes = df[var_names[0]].values.tolist()
code1_mflops = df[var_names[1]].values.tolist()
code2_mflops = df[var_names[2]].values.tolist()
code3_mflops = df[var_names[3]].values.tolist()

plt.figure()

plt.title("Comparison of 3 Codes: MFLOP/s")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

plt.plot(code1_mflops, "r-o")
plt.plot(code2_mflops, "b-x")
plt.plot(code3_mflops, "g-^")

plt.xlabel("Problem Sizes")
plt.ylabel("MFLOP/s")

varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

# save the figure before trying to show the plot
plt.savefig(plot_fname, dpi=300)

plt.show()
