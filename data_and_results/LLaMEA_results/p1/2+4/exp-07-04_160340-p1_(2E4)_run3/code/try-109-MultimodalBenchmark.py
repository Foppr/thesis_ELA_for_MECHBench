import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] range
        x_norm = x / 5.0
        
        # Create exponentially decaying sinusoidal waves
        wave_term = 0.0
        for i in range(self.dim):
            wave_term += np.exp(-0.1 * np.abs(x[i])) * np.sin(10 * np.pi * x[i]) * np.cos(5 * np.pi * x[i])
        
        # Add multiple overlapping local minima with varying depths
        minima_term = 0.0
        centers = np.array([[-2.0, -1.0, 0.0, 1.0, 2.0] * (self.dim // 5 + 1)])[:self.dim]
        for i in range(self.dim):
            minima_term += 0.5 * np.exp(-0.5 * (x[i] - centers[i])**2) * np.sin(3 * np.pi * x[i])**2
        
        # Introduce dynamic scaling based on input values
        scale_factor = 1.0 + 0.5 * np.sum(np.sin(x)**2)
        
        # Combine terms with non-separability
        result = scale_factor * (np.sum(x**2) + wave_term + minima_term)
        
        # Add a complex, non-linear interaction term
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        result += 0.1 * interaction_term
        
        # Add a chaotic component using a modified sine map
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(100 * np.sin(10 * x[i]))
        
        result += 0.05 * chaotic_term
        
        return result