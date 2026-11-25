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
            periodic += np.sin(15 * np.pi * x[i]) ** 2
        
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
        
        # Add chaotic component for increased challenge
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(19 * x[i]) * np.cos(21 * x[i])
        
        # Add higher-order polynomial interactions for more complex landscape
        high_order = 0.0
        for i in range(self.dim - 4):
            high_order += (x[i] - x[i+4])**7
        
        # Shift global minimum to create more challenging landscape
        shift = 0.9
        
        # Combine terms to create challenging landscape
        return quadratic + 0.35 * periodic + 0.25 * interaction + 0.2 * cubic_interaction + 0.15 * quartic_interaction + 0.1 * chaotic + 0.05 * high_order + shift