import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial base with mixed powers for conditioning
        polynomial = np.sum(x_scaled**2) + 0.5 * np.sum(x_scaled**4) + 0.1 * np.sum(x_scaled**6)
        
        # Sinusoidal components with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.5 + 0.3 * np.sin(i * 0.7))
            amplitude = 1.0 / (1.0 + 0.5 * i**2)
            sinusoidal += amplitude * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Asymmetric saddle points with exponential decay and shift
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x_scaled[i] - x_scaled[j] + 0.1 * (i - j)
                prod = x_scaled[i] * x_scaled[j]
                saddle += np.exp(-0.3 * (diff**2)) * np.sin(4 * prod)
        
        # Cross-terms with cubic and quartic interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (x_scaled[i]**3 + x_scaled[j]**3) * np.sin(2.5 * x_scaled[i] * x_scaled[j]) + 0.5 * (x_scaled[i]**4 + x_scaled[j]**4) * np.cos(x_scaled[i] + x_scaled[j])
        
        # Logarithmic penalty for distance from origin
        distance_penalty = 0.5 * np.log(1.0 + np.sum(x_scaled**2))
        
        # Global scaling and combination
        return 3.5 * polynomial + 2.5 * sinusoidal + 1.8 * saddle + 1.2 * cross_terms + 0.6 * distance_penalty