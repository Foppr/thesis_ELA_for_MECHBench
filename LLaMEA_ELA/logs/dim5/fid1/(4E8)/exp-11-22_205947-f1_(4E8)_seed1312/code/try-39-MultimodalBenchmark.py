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
            sin_term += (np.sin(30 * np.pi * x_norm[i]) * np.exp(-0.5 * (x_norm[i] - 0.2)**2) + 
                       np.cos(25 * np.pi * x_norm[i]) * np.exp(-0.5 * (x_norm[i] + 0.2)**2) +
                       np.sin(18 * np.pi * x_norm[i]) * np.exp(-0.3 * (x_norm[i] - 0.4)**2))
        
        # Additional complex quadratic term with multiple minima
        quad_term = 0.0
        for i in range(self.dim):
            quad_term += (x_norm[i] - 0.15)**2 * (1 + np.sin(12 * np.pi * x_norm[i])**4) + \
                        (x_norm[i] + 0.15)**2 * (1 + np.cos(11 * np.pi * x_norm[i])**4) + \
                        (x_norm[i] - 0.05)**2 * (1 + np.sin(9 * np.pi * x_norm[i])**3)
            
        # Enhanced cross-dimensional interaction terms with higher frequency
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += 0.3 * np.sin(15 * np.pi * x_norm[i]) * np.cos(8 * np.pi * x_norm[j]) * \
                                  np.exp(-0.15 * (x_norm[i] - x_norm[j])**2) + \
                                  0.2 * np.cos(12 * np.pi * x_norm[i]) * np.sin(7 * np.pi * x_norm[j]) * \
                                  np.exp(-0.2 * (x_norm[i] + x_norm[j])**2)
        
        # Additional higher-order polynomial interaction
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += x_norm[i]**5 * np.sin(4 * np.pi * x_norm[i]) + \
                        x_norm[i]**3 * np.cos(6 * np.pi * x_norm[i])
            
        # Additional radial basis function component
        rbf_term = 0.0
        for i in range(self.dim):
            rbf_term += np.exp(-2.0 * (x_norm[i] - 0.3)**2) + \
                       np.exp(-1.5 * (x_norm[i] + 0.3)**2) + \
                       np.exp(-3.0 * (x_norm[i] - 0.1)**2)
            
        # Combine terms with different weights
        result = sum_sq + 1.2 * sin_term + 0.5 * quad_term + 0.25 * interaction_term + 0.3 * poly_term + 0.4 * rbf_term
        
        return result