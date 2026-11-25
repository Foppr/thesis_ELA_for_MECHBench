import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay modulation with sinusoidal perturbations
        exp_modulation = 0
        for i in range(self.dim):
            exp_modulation += np.exp(-0.1 * x[i]**2) * np.sin(2 * np.pi * x[i] + self.dim * 0.5)
        
        # Sine-wave coupling between dimensions with dynamic frequency
        sine_coupling = 0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(0.5 * x[i] + self.dim * 0.2)
            for j in range(i+1, min(i+3, self.dim)):
                sine_coupling += np.sin(freq * (x[i] - x[j])) * np.cos(freq * (x[i] + x[j]))
        
        # Polynomial ridge structures with varying degrees
        poly_ridge = 0
        for i in range(self.dim):
            degree = 2 + int(3 * np.sin(0.4 * x[i] + self.dim * 0.3))
            poly_ridge += (x[i]**degree) * np.exp(-0.05 * x[i]**2)
        
        # Dynamic scaling based on dimension
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.1)
        
        # Combined landscape with weighted components
        return scale_factor * (0.3 * exp_modulation + 0.4 * sine_coupling + 0.3 * poly_ridge)