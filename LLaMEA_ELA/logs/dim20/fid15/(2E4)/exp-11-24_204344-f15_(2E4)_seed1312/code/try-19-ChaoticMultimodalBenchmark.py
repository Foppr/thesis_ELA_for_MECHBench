import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial potential terms with varying degrees
        poly_potential = np.sum(np.abs(x) ** 3) + 0.5 * np.sum(np.abs(x) ** 4)
        
        # Sinusoidal oscillations with chaotic frequency modulation
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 3 + 1)  # Varying frequencies
            sin_term += np.sin(freq * x[i]) * np.cos(freq * x[i] ** 2)
        
        # Cross-dimensional coupling with exponential interaction
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.exp(-np.abs(x[i] - x[j])) * np.sin(np.pi * (x[i] + x[j]))
        
        # Chaotic basin with multiple local minima
        chaotic_basin = 0.0
        for i in range(self.dim):
            chaotic_basin += (x[i] ** 2 - 2 * np.cos(5 * np.pi * x[i])) ** 2
        
        # Add noise-like perturbations
        noise = 0.1 * np.sum(np.sin(100 * x) ** 2)
        
        return poly_potential + sin_term + cross_coupling + chaotic_basin + noise