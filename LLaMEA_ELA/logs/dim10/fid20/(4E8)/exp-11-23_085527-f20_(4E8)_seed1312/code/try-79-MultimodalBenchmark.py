import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial base with mixed powers for conditioning
        polynomial = np.sum(x_scaled**2) + 0.3 * np.sum(x_scaled**4) + 0.05 * np.sum(x_scaled**6)
        
        # Enhanced sinusoidal components with dynamic frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.5 + 0.5 * np.sin(i * 0.3))
            amplitude = 1.0 / (1.0 + 0.2 * i**1.5)
            sinusoidal += amplitude * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Asymmetric saddle points with modified exponential decay
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x_scaled[i] - x_scaled[j]
                prod = x_scaled[i] * x_scaled[j]
                saddle += np.exp(-0.3 * (diff**2)) * np.sin(4 * prod) * (1.0 + 0.2 * np.abs(prod))
        
        # Cross-terms with enhanced interaction and nonlinearity
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (x_scaled[i]**2 + x_scaled[j]**2) * np.sin(3 * x_scaled[i] * x_scaled[j]) * np.cos(x_scaled[i] + x_scaled[j])
        
        # Logarithmic penalty with adjusted scaling
        distance_penalty = 0.3 * np.log(1.0 + 0.5 * np.sum(x_scaled**2))
        
        # Additional cubic interaction terms for increased complexity
        cubic_interaction = 0.0
        for i in range(self.dim):
            cubic_interaction += x_scaled[i]**3 * np.sin(2 * x_scaled[i])
        
        # Global scaling and combination
        return 2.5 * polynomial + 1.8 * sinusoidal + 1.2 * saddle + 0.8 * cross_terms + 0.4 * distance_penalty + 0.6 * cubic_interaction