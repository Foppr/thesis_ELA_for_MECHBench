import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced polynomial base with mixed powers for conditioning
        polynomial = np.sum(x_scaled**2) + 0.5 * np.sum(x_scaled**4) + 0.1 * np.sum(x_scaled**6)
        
        # Sinusoidal components with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi * (1.5 + 0.5 * np.sin(i * 0.8))
            amplitude = 1.0 / (1.0 + 0.3 * i**1.8)
            sinusoidal += amplitude * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Asymmetric saddle points with exponential decay and enhanced interaction
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x_scaled[i] - x_scaled[j]
                prod = x_scaled[i] * x_scaled[j]
                saddle += np.exp(-0.5 * (diff**2)) * np.sin(6 * prod) * (1.0 + 0.2 * np.abs(prod))
        
        # Cross-terms with cubic and quartic interactions, enhanced non-separability
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (x_scaled[i]**4 + x_scaled[j]**4) * np.sin(3.0 * x_scaled[i] * x_scaled[j]) * (1.0 + 0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Logarithmic penalty for distance from origin with adjusted scaling
        distance_penalty = 0.5 * np.log(1.0 + 0.7 * np.sum(x_scaled**2))
        
        # Additional harmonic terms to increase landscape complexity
        harmonic = 0.0
        for i in range(self.dim):
            harmonic += 0.7 * np.sin(6 * x_scaled[i]) * np.cos(9 * x_scaled[i])
        
        # Additional high-frequency oscillatory component
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 0.3 * np.sin(15 * x_scaled[i]) * np.cos(12 * x_scaled[i])
        
        # Global scaling and combination
        return 3.0 * polynomial + 2.2 * sinusoidal + 1.5 * saddle + 1.0 * cross_terms + 0.5 * distance_penalty + 0.4 * harmonic + 0.2 * high_freq