import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of squares term
        sum_sq = np.sum(x_norm**2)
        
        # Multiple high-frequency sinusoidal terms creating multiple local minima
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (np.sin(25 * np.pi * x_norm[i]) * np.exp(-0.5 * (x_norm[i] - 0.3)**2) + 
                       np.cos(20 * np.pi * x_norm[i]) * np.exp(-0.5 * (x_norm[i] + 0.3)**2))
        
        # Additional complex quadratic term with multiple minima
        quad_term = 0.0
        for i in range(self.dim):
            quad_term += (x_norm[i] - 0.1)**2 * (1 + np.sin(10 * np.pi * x_norm[i])**3) + \
                        (x_norm[i] + 0.1)**2 * (1 + np.cos(9 * np.pi * x_norm[i])**3)
            
        # Enhanced cross-dimensional interaction terms with higher frequency and stronger coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += 0.3 * np.sin(12 * np.pi * x_norm[i]) * np.cos(8 * np.pi * x_norm[j]) * \
                                  np.exp(-0.15 * (x_norm[i] - x_norm[j])**2)
        
        # Additional higher-order polynomial interaction with more complex structure
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += x_norm[i]**5 * np.sin(4 * np.pi * x_norm[i]) + \
                        x_norm[i]**3 * np.cos(6 * np.pi * x_norm[i])
            
        # Add a global shaping term to improve conditioning and increase challenge
        shape_term = 0.0
        for i in range(self.dim):
            shape_term += (x_norm[i] - 0.2)**4 + (x_norm[i] + 0.2)**4
            
        # Combine terms with different weights
        result = sum_sq + 0.9 * sin_term + 0.4 * quad_term + 0.2 * interaction_term + 0.25 * poly_term + 0.1 * shape_term
        
        return result