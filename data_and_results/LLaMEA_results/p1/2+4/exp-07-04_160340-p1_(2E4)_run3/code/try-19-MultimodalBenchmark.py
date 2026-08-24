import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Chaotic sinusoidal perturbations with exponential decay
        harmonic = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 3)  # Varying frequencies
            amp = np.exp(-i / (self.dim + 1))  # Exponentially decaying amplitudes
            harmonic += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Add nested harmonic structure with varying scales
        nested = 0.0
        for i in range(self.dim):
            scale = 10.0 ** (i % 4)
            nested += np.sin(scale * x[i]) * np.cos(scale * x[i])
        
        # Saddle point structure
        saddle = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                saddle += (x[i]**2 - x[i+1]**2) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
        
        # Combine all components
        result = quadratic + 0.5 * harmonic + 0.3 * nested + 0.1 * saddle
        
        return result