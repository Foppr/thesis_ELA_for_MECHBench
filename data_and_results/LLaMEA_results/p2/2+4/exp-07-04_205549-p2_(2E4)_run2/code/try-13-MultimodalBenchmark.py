import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Chaotic basin term with nested attractors
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += (x_normalized[i]**2 - 0.5 * np.sin(4 * np.pi * x_normalized[i]))**2
        
        # Exponential energy barriers
        barriers = 0.0
        for i in range(self.dim):
            barriers += np.exp(2.0 * np.abs(x_normalized[i]) - 1.0)
        
        # Saddle point structure
        saddle = 0.0
        for i in range(self.dim):
            saddle += x_normalized[i] * np.sin(2 * np.pi * x_normalized[i])
        
        # Nested multimodal component
        nested = 0.0
        for i in range(self.dim):
            nested += 0.5 * np.sin(8 * np.pi * x_normalized[i]) * np.cos(6 * np.pi * x_normalized[i])
            nested += 0.3 * np.sin(12 * np.pi * x_normalized[i])**2
        
        # Combined function
        return 2.0 * chaotic + barriers + 0.5 * saddle + nested