import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = np.sum(x**2) / self.dim
        
        # Periodic multimodal term with multiple global minima
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(30 * np.pi * x[i]) ** 2 + 0.7 * np.cos(15 * np.pi * x[i]) ** 2
        
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim - 1):
            interaction += (x[i] - x[i+1])**8 + 0.4 * (x[i] + x[i+1])**5
        
        # Add cubic interaction terms for increased complexity
        cubic_interaction = 0.0
        for i in range(self.dim - 2):
            cubic_interaction += (x[i] - x[i+2])**7 + 0.3 * (x[i] + x[i+2])**4
        
        # Add quartic interaction terms for even higher complexity
        quartic_interaction = 0.0
        for i in range(self.dim - 3):
            quartic_interaction += (x[i] - x[i+3])**9
        
        # Add chaotic component using logistic map with varying parameter for enhanced complexity
        chaotic = 0.0
        r_values = [3.98, 3.88, 3.78, 3.68, 3.58]
        for i in range(self.dim):
            r = r_values[i % len(r_values)]
            if i == 0:
                chaotic += np.sin(r * x[i] * (1 - x[i])) ** 2
            else:
                chaotic += np.sin(r * x[i-1] * (1 - x[i-1])) ** 2
        
        # Add a dynamic shift based on sine and cosine functions for global minimum
        shift = 0.0
        for i in range(self.dim):
            shift += 0.6 * np.sin(6 * x[i]) + 0.4 * np.cos(8 * x[i])
        
        # Combine terms to create challenging landscape
        return quadratic + 0.5 * periodic + 0.3 * interaction + 0.15 * cubic_interaction + 0.07 * quartic_interaction + 0.3 * chaotic + shift