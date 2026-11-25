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
            periodic += np.sin(13 * np.pi * x[i]) ** 2
        
        # Add interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim - 1):
            interaction += (x[i] - x[i+1])**4
        
        # Add cubic interaction terms for increased complexity
        cubic_interaction = 0.0
        for i in range(self.dim - 2):
            cubic_interaction += (x[i] - x[i+2])**5
        
        # Add quartic interaction terms for even more complexity
        quartic_interaction = 0.0
        for i in range(self.dim - 3):
            quartic_interaction += (x[i] - x[i+3])**6
        
        # Add quintic interaction terms for maximum complexity
        quintic_interaction = 0.0
        for i in range(self.dim - 4):
            quintic_interaction += (x[i] - x[i+4])**7
        
        # Add chaotic component for increased challenge
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(17 * x[i]) * np.cos(19 * x[i])
        
        # Add higher frequency chaotic component
        high_freq_chaotic = 0.0
        for i in range(self.dim):
            high_freq_chaotic += np.sin(23 * x[i]) * np.cos(29 * x[i])
        
        # Add dynamic shift based on problem dimensions
        shift = 0.8 + 0.1 * np.sin(np.sum(x) / self.dim)
        
        # Combine terms to create challenging landscape
        return quadratic + 0.3 * periodic + 0.2 * interaction + 0.15 * cubic_interaction + 0.1 * quartic_interaction + 0.05 * quintic_interaction + 0.03 * chaotic + 0.02 * high_freq_chaotic + shift