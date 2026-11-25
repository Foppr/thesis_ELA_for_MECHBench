import numpy as np

class MultiModalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add chaotic sine-wave interactions with non-uniform frequencies
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.0 + 0.5 * np.cos(0.3 * i)
            f_val += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**3) + \
                     0.4 * np.sin(5 * freq * x[i]) * np.cos(4 * freq * x[i]**2)
        
        # Add adaptive polynomial conditioning with varying exponents
        for i in range(self.dim):
            exp = 2.0 + 1.5 * np.sin(0.4 * i)
            scale = 1.0 + 0.3 * np.cos(0.6 * i)
            f_val += 0.2 * scale * x[i]**exp - 0.4 * scale * x[i]**2
        
        # Add cross-dimensional exponential penalties with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.2 * (x[i]**2 + x[j]**2)) * np.sin(0.7 * (x[i] + x[j])) * \
                          np.cos(0.3 * (x[i] - x[j]))
                f_val += 0.3 * coupling
        
        # Add highly non-separable radial interactions with multi-scale basis
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(min(7, self.dim)):
            for j in range(i+1, min(7, self.dim)):
                dist = np.sqrt((x[i] - centers[i])**2 + (x[j] - centers[j])**2)
                f_val += 0.6 * np.exp(-0.3 * dist**2) * np.sin(3 * np.pi * dist) * \
                         np.cos(2 * np.pi * dist)
        
        # Add global modulation with multi-frequency chaotic waves
        global_mod = 0.5 * np.sin(np.sum(x) * 0.7) + \
                     0.4 * np.cos(np.sum(x) * 1.1) + \
                     0.3 * np.sin(np.sum(x) * 1.8) + \
                     0.2 * np.cos(np.sum(x) * 2.5)
        f_val += global_mod
        
        # Add noise-like perturbations with chaotic frequency components
        for i in range(self.dim):
            f_val += 0.1 * np.sin(20 * x[i]) * np.cos(17 * x[i]) + \
                     0.08 * np.sin(25 * x[i]**2) * np.cos(22 * x[i])
        
        # Add sharp gradient changes through piecewise polynomial terms
        for i in range(self.dim):
            if x[i] < 0:
                f_val += 0.15 * x[i]**5
            else:
                f_val += 0.12 * x[i]**6
        
        return f_val