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
        
        # Enhanced sinusoidal terms with multiple frequencies creating complex landscape
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += (np.sin(15 * np.pi * x_norm[i]) + 0.5 * np.sin(30 * np.pi * x_norm[i])) * np.exp(-0.3 * (x_norm[i] - 0.3)**2)
        
        # Modified quadratic terms with multiple minima
        quad_term = 0.0
        for i in range(self.dim):
            quad_term += (x_norm[i] - 0.15)**2 * (1 + 0.7 * np.sin(8 * np.pi * x_norm[i])**2) + 0.3 * (x_norm[i] + 0.2)**4
            
        # Enhanced cross-dimensional interaction terms with varying coupling strengths
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Varying coupling strengths and frequencies for complexity
                coupling_strength = 0.15 * (1 + 0.5 * np.sin(np.pi * i / self.dim))
                interaction_term += coupling_strength * np.sin(10 * np.pi * x_norm[i]) * np.cos(6 * np.pi * x_norm[j])
        
        # Additional higher-order polynomial for increased landscape complexity
        high_order_term = 0.0
        for i in range(self.dim):
            high_order_term += 0.2 * (x_norm[i]**5 - 0.5 * x_norm[i]**3)
            
        # Combine all terms with optimized weights for better fitness
        result = 0.8 * sum_sq + 0.7 * sin_term + 0.35 * quad_term + 0.15 * interaction_term + 0.25 * high_order_term
        
        return result