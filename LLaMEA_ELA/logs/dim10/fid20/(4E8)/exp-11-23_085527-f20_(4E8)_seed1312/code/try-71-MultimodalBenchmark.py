import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with varying frequency and amplitude
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.sin(4 * np.pi * r) * np.exp(-r**2)
        
        # Nested sinusoidal terms with increasing complexity and dynamic frequencies
        nested = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.0 + 0.3 * np.sin(i * 0.5))
            nested += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Cross-terms with adaptive interaction and asymmetric modulation
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt(x_scaled[i]**2 + x_scaled[j]**2)
                interaction = np.sin(3 * x_scaled[i] * x_scaled[j]) * np.exp(-dist * 0.5)
                cross += interaction
        
        # Polynomial shaping with mixed powers and adaptive conditioning
        poly = 0.0
        for i in range(self.dim):
            poly += (x_scaled[i]**4 + 0.3 * x_scaled[i]**8 + 0.1 * x_scaled[i]**10)
        
        # Additional global minimum enhancement with asymmetric penalty
        penalty = 0.15 * r**2 + 0.05 * np.sin(5 * r)
        
        # Combine all components with optimized weights
        return 2.5 * radial + 2.0 * nested + 1.8 * cross + 1.2 * poly + penalty