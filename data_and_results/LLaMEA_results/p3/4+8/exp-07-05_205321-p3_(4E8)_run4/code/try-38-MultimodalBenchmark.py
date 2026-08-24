import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component with nested saddle points
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += (x_norm[i]**2 - 2 * x_norm[i] * np.sin(2 * np.pi * x_norm[i]) + 
                       np.cos(2 * np.pi * x_norm[i]) * np.sin(2 * np.pi * x_norm[i]))
        
        # Nested radial structure with varying curvature
        r = np.sqrt(np.sum(x_norm**2))
        nested = np.sin(5 * r) * np.exp(-0.5 * r**2) + 0.5 * np.cos(3 * r) * np.exp(-0.3 * r)
        
        # Gradient flow complexity with directional sensitivity
        gradient_comp = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                gradient_comp += np.sin(x_norm[i] * x_norm[j]) * np.exp(-0.1 * (x_norm[i] - x_norm[j])**2)
        
        # Combine components with varying weights
        return 0.4 * chaotic + 0.3 * nested + 0.3 * gradient_comp + 1.0