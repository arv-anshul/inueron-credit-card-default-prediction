import matplotlib.pyplot as plt

plt.style.use("ggplot")

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
# Axes Level Customization
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
plt.rcParams["axes.facecolor"] = "white"
plt.rcParams['axes.edgecolor'] = 'lightgray'
plt.rcParams["axes.linewidth"] = 1
plt.rcParams["xtick.color"] = "black"
plt.rcParams["ytick.color"] = "black"
plt.rcParams["grid.color"] = "lightgray"

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
# Figure Level Customization
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
# plt.rcParams['font.family'] = 'operator mono lig'
plt.rcParams["font.size"] = 12
plt.rcParams["figure.titlesize"] = 25
plt.rcParams["figure.titleweight"] = 700
plt.rcParams["figure.dpi"] = 100

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
# Others
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- #
plt.rcParams['savefig.bbox'] = 'tight'
