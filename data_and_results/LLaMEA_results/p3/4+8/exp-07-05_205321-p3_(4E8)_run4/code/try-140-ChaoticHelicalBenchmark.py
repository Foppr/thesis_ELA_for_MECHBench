import numpy as np

class ChaoticHelicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Helical component with varying pitch and amplitude
        r = np.sqrt(np.sum(x_norm**2))
        theta = np.arctan2(x_norm[1], x_norm[0]) if self.dim >= 2 else 0.0
        helical = np.sin(5 * theta + 2 * r) * np.cos(3 * theta - r)
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i]) * np.sin(3 * x_norm[i]**2)
        
        # Saddle point component with hyperbolic tangents
        saddle = 0.0
        for i in range(self.dim):
            saddle += np.tanh(2 * x_norm[i]) * np.sin(4 * x_norm[i])
        
        # Multi-modal interaction term with exponential decay
        modal = 0.0
        for i in range(self.dim):
            modal += np.exp(-0.5 * (x_norm[i] - 0.5)**2) * np.sin(8 * np.pi * x_norm[i])
        
        # Cross-dimensional interaction with phase shifts
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited cross-interaction
                cross += 0.3 * np.sin(3 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(2 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Combine all components with dynamic weights based on dimensionality
        weight_helical = 0.4 + 0.1 * np.sin(self.dim)
        weight_chaotic = 0.3 + 0.05 * np.cos(self.dim)
        weight_saddle = 0.2 + 0.05 * np.sin(self.dim * 0.5)
        weight_modal = 0.1 + 0.05 * np.cos(self.dim * 0.3)
        weight_cross = 0.05
        
        result = (weight_helical * helical + 
                  weight_chaotic * chaotic + 
                  weight_saddle * saddle + 
                  weight_modal * modal + 
                  weight_cross * cross)
        
        # Add a global minimum offset to ensure the optimum is not at zero
        return result + 0.5 * np.sin(0.5 * r) * np.cos(0.3 * r)