import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic harmonic components with exponential decay
        harmonics = []
        for i in range(self.dim):
            freq = 2**(i + 1) * np.pi
            amp = np.exp(-0.1 * i)
            term = amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
            harmonics.append(term)
        f2 = np.sum(harmonics)
        
        # Cross-dimensional coupling with exponential decay
        coupling = []
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                coupling_term = np.exp(-0.05 * (i + j)) * np.sin(np.pi * x_norm[i] * x_norm[j])
                coupling.append(coupling_term)
        f3 = np.sum(coupling)
        
        # Ruggedness modifier based on dimensionality
        ruggedness = 0.5 * np.log(self.dim + 1) * np.sum(np.abs(x_norm)**3)
        
        # Exponentially decaying sinusoidal landscape
        decay_factor = np.exp(-0.2 * self.dim)
        f4 = decay_factor * np.sum(np.sin(5 * x_norm) * np.cos(3 * x_norm))
        
        # Combined function with dynamic weighting
        return 0.3 * f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * ruggedness + 0.05 * f4