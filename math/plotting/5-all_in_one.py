#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

x0 = np.arange(0, 11)


fig, axs = plt.subplots(3, 2, figsize=(10, 10))


# Plot 1
axs[0, 0].plot(x0, y0, color="red")
axs[0, 0].set_title("", fontsize="x-small")

# Plot 2
axs[0, 1].scatter(x1, y1, s=8, c="purple")
axs[0, 1].set_title("Men's Height vs Weight", fontsize="x-small")

# Plot 3
axs[1, 0].plot(x2, y2)
axs[1, 0].set_yscale("log")
axs[1, 0].set_title("Exponential Decay of C-14", fontsize="x-small")

# Plot 4
axs[1, 1].plot(x3, y31, c="red", linestyle="--", label="C-14")
axs[1, 1].plot(x3, y32, c="green", label="Ra-226")
axs[1, 1].set_xlim(0, 20000)
axs[1, 1].set_ylim(0, 1)
axs[1, 1].legend()
axs[1, 1].set_title("Exponential Decay of Radioactive Elements", fontsize="x-small")

# Plot 5
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
axs[2, 0].hist(student_grades, bins=bins, edgecolor="black")
axs[2, 0].set_xlim(0, 100)
axs[2, 0].set_ylim(0, 30)
axs[2, 0].set_xticks(bins)
axs[2, 0].set_title("Project A", fontsize="x-small")

# Hide empty subplot
axs[2, 1].axis('off')


plt.tight_layout()


plt.suptitle("All in One", fontsize="x-small")


plt.show()