import numpy as np

class RadialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add radial basis interactions with varying centers and widths
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(min(5, self.dim)):
            for j in range(i+1, min(5, self.dim)):
                dist = np.sqrt((x[i] - centers[i])**2 + (x[j] - centers[j])**2)
                f_val += 0.7 * np.exp(-0.3 * dist**2) * np.cos(3 * np.pi * dist)
        
        # Add multi-scale harmonic oscillations with adaptive frequencies
        for i in range(self.dim):
            freq = 1.5 + 0.3 * np.sin(0.4 * i)
            amp = 1.0 + 0.1 * np.cos(0.5 * i)
            f_val += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2) + \
                     0.4 * np.sin(4 * freq * x[i]) * np.cos(3 * freq * x[i])
        
        # Add adaptive conditioning with dimension-dependent scaling
        for i in range(self.dim):
            scale = 1.2 + 0.3 * np.sin(0.25 * i)
            f_val += 0.15 * scale * x[i]**4 - 0.4 * scale * x[i]**2
        
        # Add cross-dimensional coupling with exponential interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.15 * (x[i]**2 + x[j]**2)) * np.sin(0.7 * (x[i] + x[j]))
                f_val += 0.3 * coupling
        
        # Add global modulation with multi-frequency sine waves
        global_mod = 0.5 * np.sin(np.sum(x) * 0.6) + \
                     0.4 * np.cos(np.sum(x) * 0.9) + \
                     0.3 * np.sin(np.sum(x) * 1.5)
        f_val += global_mod
        
        # Add noise-like perturbations to increase ruggedness
        for i in range(self.dim):
            f_val += 0.08 * np.sin(18 * x[i]) * np.cos(14 * x[i])
            
        return f_val