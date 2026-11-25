import numpy as np

class ChaoticRadialFunction:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.a = 3.9
        self.b = 0.5
        self.c = 0.3
        
    def f(self, x):
        x = np.array(x)
        
        # Radial basis function component
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r**2 / (2.0 * self.dim)) * np.sin(r)
        
        # Chaotic sine coupling terms
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Generate chaotic sequence using logistic map
            chaotic_val = np.sin(self.a * xi * (1 - xi))
            chaotic_sum += np.sin(2.0 * chaotic_val + self.b * xi) * np.cos(3.0 * xi)
            
        # Adaptive dimensional penalty based on coordinate values
        penalty = 0.0
        for i in range(self.dim):
            penalty += (i + 1) * np.abs(x[i])**3 * np.exp(-np.abs(x[i]))
            
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic interaction term
                interaction = np.sin(self.a * x[i] * x[j]) * np.cos(self.b * (x[i]**2 + x[j]**2))
                cross_term += interaction * np.exp(-np.abs(x[i] - x[j]) / (i + j + 1))
                
        # Multi-modal peaks with varying amplitudes
        peak_term = 0.0
        for i in range(self.dim):
            peak_term += np.sin(5.0 * x[i])**2 * np.cos(3.0 * x[i])**2
            
        # Global minimum adjustment
        global_min_shift = np.sum((x - 0.5)**2) / (2.0 * self.dim)
        
        # Combine all terms
        result = radial_term + chaotic_sum + penalty + cross_term + peak_term + global_min_shift
        
        return result