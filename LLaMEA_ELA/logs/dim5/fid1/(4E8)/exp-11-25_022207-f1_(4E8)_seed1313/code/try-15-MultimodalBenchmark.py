import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic base term with conditioning
        quadratic_term = np.sum(x_normalized**2)
        
        # Multiple sinusoidal components with different frequencies and amplitudes
        freqs = [2, 3, 5, 7, 11]
        sinusoidal_term = 0
        for freq in freqs:
            sinusoidal_term += np.sum(np.sin(freq * np.pi * x_normalized)**2)
        
        # Chaotic interaction term using logistic map-like behavior
        chaotic_term = 0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic_term += (x_normalized[i]**2 + x_normalized[i+1]**2) * np.sin(10 * np.pi * x_normalized[i] * x_normalized[i+1])
        
        # Multiple overlapping basins with different depths
        basin_term = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                basin_term += (x_normalized[i]**2 + x_normalized[i+1]**2) * np.exp(-0.5 * (x_normalized[i]**2 + x_normalized[i+1]**2))
        
        # Complex penalty with exponential scaling
        penalty_term = 0.5 * np.sum(np.exp(2 * np.abs(x_normalized)) - 1)
        
        # Add a small noise component to increase complexity
        noise = 0.01 * np.random.random()
        
        # Combine all terms
        return quadratic_term + sinusoidal_term + chaotic_term + basin_term + penalty_term + noise