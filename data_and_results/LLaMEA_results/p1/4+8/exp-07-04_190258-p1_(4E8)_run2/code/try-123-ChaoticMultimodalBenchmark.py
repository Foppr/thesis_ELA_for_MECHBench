import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component
        spherical = np.sum(x**2)
        
        # Sinusoidal modulation with varying frequencies
        sinusoidal = 0
        for i in range(self.dim):
            sinusoidal += np.sin((i + 1) * x[i]) * np.cos((i + 1) * x[i] / 2)
        
        # Gaussian mixture with adaptive scaling
        gaussian = 0
        centers = np.linspace(-3, 3, 5)
        for i in range(self.dim):
            for center in centers:
                gaussian += np.exp(-0.5 * ((x[i] - center) / (0.5 * (i + 1)))**2) * np.sin(0.3 * x[i])
        
        # Cross-dimensional interaction with adaptive coupling
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                coupling += (x[i] * x[j]) / (1 + np.exp(-0.1 * (x[i] - x[j])**2))
        
        # Adaptive conditioning based on dimension
        conditioning = 0
        for i in range(self.dim):
            conditioning += (i + 1) * np.sin(x[i]**2) * np.cos(x[i])
        
        # Asymmetric saddle with polynomial terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**4 - 2 * x[i]**2 + 0.5 * x[i]) * np.sin(0.2 * x[i])
        
        # Multi-scale periodic component
        periodic = 0
        for i in range(self.dim):
            periodic += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.tan(0.1 * x[i])
        
        # Combined fitness with adaptive weights
        return spherical + 0.5 * sinusoidal + 0.3 * gaussian + 0.2 * coupling + 0.1 * conditioning + 0.4 * saddle + 0.2 * periodic