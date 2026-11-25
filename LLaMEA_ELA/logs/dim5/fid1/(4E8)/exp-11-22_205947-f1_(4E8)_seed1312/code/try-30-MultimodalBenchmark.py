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
        
        # Multiple sinusoidal terms creating multiple local minima with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (np.sin(15 * np.pi * x_norm[i]) + 0.5 * np.sin(30 * np.pi * x_norm[i])) * np.exp(-0.5 * (x_norm[i] - 0.3)**2)
        
        # Enhanced quadratic term with multiple minima and nonlinearity
        quad_term = 0.0
        for i in range(self.dim):
            quad_term += (x_norm[i] - 0.15)**2 * (1 + 0.5 * np.sin(8 * np.pi * x_norm[i])**2) + 0.3 * (x_norm[i] + 0.2)**4
            
        # Stronger cross-dimensional interaction terms with higher frequency coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += 0.2 * np.sin(10 * np.pi * x_norm[i]) * np.sin(5 * np.pi * x_norm[j]) * (1 + 0.1 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Additional harmonic term for increased landscape complexity
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += 0.15 * np.sin(20 * np.pi * x_norm[i]) * np.cos(10 * np.pi * x_norm[i])
        
        # Combine terms with optimized weights
        result = sum_sq + 0.7 * sin_term + 0.3 * quad_term + 0.15 * interaction_term + 0.2 * harmonic_term
        
        return result