import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic logistic map parameters
        self.r = 3.95
        self.x_logistic = 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponentially decaying basis functions
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sum(np.exp(-3 * r**2) * np.cos(5 * np.pi * r))
        
        # Sinusoidal spiral term to create rotational complexity
        if self.dim >= 2:
            theta = np.arctan2(x_norm[1], x_norm[0])
            spiral = np.sin(9 * theta) * np.cos(6 * theta) * np.exp(-r**2)
        else:
            spiral = 0.0
            
        # Additional high-frequency oscillation in all dimensions with chaotic modulation
        chaotic_mod = 0.0
        for i in range(self.dim):
            self.x_logistic = self.r * self.x_logistic * (1 - self.x_logistic)
            chaotic_mod += np.sin(15 * x_norm[i]) * np.cos(12 * x_norm[i]) * self.x_logistic
            
        # Quadratic penalty to keep solution near origin
        penalty = 0.3 * np.sum(x_norm**2)
        
        # Add a global multimodal term with multiple peaks
        multi_peak = 0.0
        for i in range(self.dim):
            multi_peak += np.sin(2 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
        multi_peak = np.exp(-0.5 * multi_peak**2)
        
        # Combine all components
        return radial + 3 * spiral + 1.5 * chaotic_mod + penalty + 0.8 * multi_peak