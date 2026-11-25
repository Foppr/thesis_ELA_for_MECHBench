import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with varying frequency and amplitude
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.sin(3 * np.pi * r) * np.exp(-r**2)
        
        # Nested sinusoidal terms with increasing complexity
        nested = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.5 * np.sin(i))
            nested += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Cross-terms with exponential decay and sinusoidal modulation
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt(x_scaled[i]**2 + x_scaled[j]**2)
                cross += np.exp(-dist) * np.sin(4 * x_scaled[i] * x_scaled[j])
        
        # Polynomial shaping with adaptive conditioning
        poly = 0.0
        for i in range(self.dim):
            poly += (x_scaled[i]**4 + 0.5 * x_scaled[i]**6)
        
        # Global minimum at origin with additional penalty for distance
        penalty = 0.1 * r**2
        
        return 3.0 * radial + 2.0 * nested + 1.5 * cross + 1.0 * poly + penalty