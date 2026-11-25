import numpy as np

class ChaoticRadialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Radial basis function component with varying widths
        result = 0.0
        for i in range(self.dim):
            width = 1.0 + 0.5 * np.sin(i)
            result += np.exp(-np.sum((x - np.sin(i))**2) / (2.0 * width**2))
            
        # Chaotic sine coupling terms with logistic map modulation
        for i in range(self.dim):
            chaotic_factor = np.sin(3.14159 * (i + 1) * np.sin(x[i]))
            result += 0.5 * np.sin(2.0 * x[i] + chaotic_factor) * np.cos(2.0 * x[i] - chaotic_factor)
            
        # Adaptive penalty based on distance and dimensionality
        dist = np.sqrt(np.sum(x**2))
        penalty = 2.0 * dist * np.exp(-dist / 3.0) * (1.0 + 0.1 * np.sin(dist))
        result += penalty
        
        # Cross-dimensional interaction with logistic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                log_factor = 1.0 + 0.3 * np.sin(x[i] * x[j])
                result += 0.3 * np.sin(x[i] * x[j]) * log_factor * (1.0 / (1.0 + abs(x[i] - x[j])))
                
        # Multi-scale oscillatory terms with varying frequencies
        for i in range(self.dim):
            freq = 2.5 * (i + 1) * np.cos(i)  # Slightly increased frequency scaling
            result += 0.2 * np.sin(freq * x[i])**3 * np.cos(freq * x[i])**3
            
        # Asymmetric basin terms to create varied curvature - modified coefficients
        for i in range(self.dim):
            asym_term = (x[i] - 1.5)**4 + 0.7 * (x[i] + 1.0)**3  # Changed shift and coefficient
            result += 0.15 * asym_term * np.exp(-abs(x[i]))
            
        # Central repulsion with adaptive strength - modified parameters
        center_dist = np.sqrt(np.sum((x - 0.5)**2))
        result += 1.0 * np.exp(-center_dist**2 / 2.0) * np.sin(center_dist)
        
        return result