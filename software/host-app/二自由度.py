import numpy as np
import matplotlib.pyplot as plt

def plot_range(L1, L2, θ1_min, θ1_max, θ2_min, θ2_max):
        θ1_range = np.linspace(np.radians(θ1_min), np.radians(θ1_max), 100)
        θ2_range = np.linspace(np.radians(θ2_min), np.radians(θ2_max), 100)

        X = []
        Y = []

        for θ1 in θ1_range:
            for θ2 in θ2_range:
                x = L1 * np.cos(θ1) + L2 * np.cos(θ1 + θ2)
                y = L1 * np.sin(θ1) + L2 * np.sin(θ1 + θ2)
                X.append(x)
                Y.append(y)

        plt.figure()
        plt.plot(X, Y, 'o', markersize=1)
        plt.title("二自由度机械臂运动范围")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()

L1=10
L2=10
θ1_min=0
θ1_max=45
θ2_min=0
θ2_max=θ1_min+180
plot_range(L1, L2, θ1_min, θ1_max, θ2_min, θ2_max)