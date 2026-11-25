import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        f_val = np.sum(x**2) * (1.0 + 0.3 * np.sin(0.4 * np.sum(x**2)))
        
        # Enhanced oscillatory components with varying frequencies and chaotic modulations
        for i in range(self.dim):
            f_val += 0.5 * np.sin(17 * x[i]) * np.cos(9 * x[i]) * np.exp(-0.1 * abs(x[i])) * (1.0 + 0.25 * np.sin(3 * x[i]))
            
        # Modified saddle structure with enhanced directional dependency and chaotic components
        if self.dim >= 2:
            diff_sum = 0
            for i in range(self.dim - 1):
                diff_sum += (x[i] - x[i+1])**2 * (1.0 + 0.25 * np.sin(x[i] * x[i+1]) * np.cos(0.7 * x[i]) * np.exp(-0.05 * abs(x[i])))
            f_val += 0.35 * diff_sum
            
        # Multiple interacting Gaussian peaks with complex positioning and dynamic scaling
        for i in range(0, self.dim, 4):
            if i + 3 < self.dim:
                f_val += 0.35 * np.exp(-0.5 * ((x[i] - 2.0)**2 + (x[i+1] + 2.0)**2 + (x[i+2] - 1.5)**2 + (x[i+3] + 1.0)**2))
                
        # Additional high-frequency noise terms with chaotic modulation
        for i in range(self.dim):
            f_val += 0.2 * np.sin(27 * x[i]) * np.cos(22 * x[i]) * np.exp(-0.3 * abs(x[i])) * (1.0 + 0.15 * np.sin(5 * x[i]))
            
        # Cross-dimensional interaction terms with chaotic coupling - slightly modified coefficients
        if self.dim >= 4:
            interaction_sum = 0
            for i in range(self.dim - 3):
                interaction_sum += x[i] * x[i+1] * x[i+2] * x[i+3] * np.sin(0.5 * (x[i] + x[i+1] + x[i+2] + x[i+3])) * np.cos(0.3 * x[i]) * (1.0 + 0.15 * np.sin(x[i] * x[i+1]))
            f_val += 0.3 * interaction_sum
            
        # Chaotic oscillation component for increased complexity - slightly modified
        chaotic_term = 0.3 * np.sin(np.sum(x) * 12) * np.cos(np.sum(x) * 8)
        f_val += chaotic_term
        
        return f_val