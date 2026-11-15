import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Chaotic sinusoidal interactions with nested structure
        chaotic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic += np.sin(10 * np.pi * x_norm[i] * x_norm[j]) * np.cos(7 * np.pi * x_norm[i]) * np.sin(5 * np.pi * x_norm[j])
        
        # Multiple nested global minima with fractal-like structure
        nested_minima = 0.0
        for i in range(self.dim):
            nested_minima += np.sin(20 * np.pi * x_norm[i]) * np.cos(15 * np.pi * x_norm[i]) * np.sin(10 * np.pi * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Enhanced dimensional coupling through exponential terms
        coupling = 0.0
        for i in range(self.dim):
            coupling += np.exp(-0.5 * (x_norm[i] - 0.2)**2) * np.sin(25 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i])
        
        # Add high-frequency oscillations for increased complexity
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(50 * np.pi * x_norm[i]) * np.cos(30 * np.pi * x_norm[i]) * np.sin(15 * np.pi * x_norm[i])
        
        # Combine all components with carefully tuned weights
        return 2 * quadratic + 3 * chaotic + 2.5 * nested_minima + 0.5 * coupling + 0.2 * high_freq + 50 * np.exp(-0.2 * np.sum(x_norm**2))