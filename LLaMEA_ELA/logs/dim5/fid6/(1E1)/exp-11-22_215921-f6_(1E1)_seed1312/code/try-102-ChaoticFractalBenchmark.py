import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Logistic map chaotic component with varying r parameters
        logistic = 0.0
        r_values = np.linspace(3.5, 4.0, self.dim)
        for i in range(self.dim):
            if i == 0:
                logistic += 0.5 * (r_values[i] * x_norm[i] * (1 - x_norm[i]))
            else:
                logistic += 0.5 * (r_values[i] * x_norm[i] * (1 - x_norm[i])) + \
                           0.2 * np.sin(3 * x_norm[i-1]) * np.cos(2 * x_norm[i])
        
        # Fractal noise component using fractional Brownian motion-like structure
        fractal = 0.0
        for i in range(self.dim):
            fractal += (np.sin(10 * x_norm[i]) + np.cos(7 * x_norm[i])) * \
                      np.exp(-0.1 * x_norm[i]**2) * \
                      np.sin(5 * np.pi * x_norm[i])
        
        # Cross-dimensional coupling with asymmetric interaction
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i]**3 + x_norm[i+1]**3) * \
                       np.exp(-0.2 * (x_norm[i]**2 + x_norm[i+1]**2)) * \
                       np.cos(2 * np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Multi-scale periodic modulation with dynamic frequency
        modulated = 0.0
        for i in range(self.dim):
            freq = 2 + 3 * np.sin(x_norm[i])
            modulated += np.sin(freq * x_norm[i]) * \
                        np.cos(0.5 * x_norm[i]) * \
                        np.exp(-0.1 * x_norm[i]**2)
        
        # Asymmetric saddle points with exponential weighting
        saddle = 0.0
        for i in range(self.dim - 1):
            saddle += (x_norm[i]**2 - x_norm[i+1]**2) * \
                     np.exp(-0.3 * (x_norm[i]**2 + x_norm[i+1]**2)) * \
                     np.tanh(2 * x_norm[i] * x_norm[i+1])
        
        # Dimension-dependent conditioning and scaling
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all components
        return condition_factor * (logistic + fractal + coupling + modulated + saddle)