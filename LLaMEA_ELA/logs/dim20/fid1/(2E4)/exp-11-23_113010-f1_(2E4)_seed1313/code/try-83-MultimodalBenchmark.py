import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential basin terms with logistic map modulation
        exp_basin = np.sum(np.exp(3 * x_norm**2) - 1)
        
        # Sinusoidal modulations with chaotic frequency ratios based on golden ratio
        sin_mod = np.sum(np.sin(1.618 * np.pi * x_norm) * np.cos(2.618 * np.pi * x_norm))
        sin_mod2 = np.sum(np.sin(4.236 * np.pi * x_norm**2) * np.cos(6.854 * np.pi * x_norm**2))
        
        # Cross-dimensional coupling with exponential interaction terms
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.exp(0.5 * (x_norm[i]**3 + x_norm[j]**3)) * np.sin(1.618 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Fractal-like terrain using logistic map iterations
        fractal = 0.0
        for i in range(self.dim):
            logistic_val = 3.8 * x_norm[i] * (1 - x_norm[i])
            fractal += logistic_val**2
        
        # Asymmetric saddle with polynomial and exponential components
        saddle = np.sum(x_norm**6 * np.exp(-x_norm**2) + 0.5 * x_norm**4 * np.sin(3 * np.pi * x_norm))
        
        # Additional chaotic noise component
        noise = 0.01 * np.random.random()
        
        return 1.5 * exp_basin + 0.7 * sin_mod + 0.6 * sin_mod2 + 0.8 * cross_interaction + 0.4 * fractal + 0.3 * saddle + noise