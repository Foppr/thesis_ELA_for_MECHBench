import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # High-frequency trigonometric terms creating many local minima
        trig_term = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm))
        
        # Radial basin with exponential decay and multiple peaks
        r = np.sqrt(np.sum(x_norm**2))
        radial_basin = np.exp(-r**2) * (1 + 0.5 * np.sin(5 * r) * np.cos(3 * r))
        
        # Cross-dimensional coupling with varying interaction strength
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(3 * np.pi * (x_norm[i] - x_norm[i+1]))
        
        # Multi-scale fractal-like structure with shifted centers
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2**i * np.pi * (x_norm[i] + 0.1)) * np.cos(2**(i//2) * np.pi * (x_norm[i] - 0.2))
        
        # Adaptive conditioning based on dimensionality
        condition = 1.0 + 0.2 * (self.dim - 1)
        
        # Combine all components with appropriate scaling
        return condition * (trig_term + radial_basin + coupling + fractal)