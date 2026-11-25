import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with varying frequency and amplitude
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.sin(5 * np.pi * r) * np.exp(-r**2)
        
        # Nested sinusoidal terms with increasing complexity and dynamic frequencies
        nested = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.3 * np.sin(i * 0.5))
            nested += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Cross-terms with exponential decay and sinusoidal modulation
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt(x_scaled[i]**2 + x_scaled[j]**2)
                cross += np.exp(-dist * 0.5) * np.sin(3 * x_scaled[i] * x_scaled[j]) * np.cos(2 * x_scaled[i] + x_scaled[j])
        
        # Polynomial shaping with adaptive conditioning and higher-order terms
        poly = 0.0
        for i in range(self.dim):
            poly += (x_scaled[i]**4 + 0.3 * x_scaled[i]**6 + 0.1 * x_scaled[i]**8)
        
        # Additional non-separable component with trigonometric interaction
        nonsep = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                nonsep += np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j])
        
        # Global minimum at origin with additional penalty for distance and non-separability
        penalty = 0.05 * r**2 + 0.02 * nonsep**2
        
        return 2.5 * radial + 1.8 * nested + 1.2 * cross + 1.0 * poly + 0.5 * nonsep + penalty