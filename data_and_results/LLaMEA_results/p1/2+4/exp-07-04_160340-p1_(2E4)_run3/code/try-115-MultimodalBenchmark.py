import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Add chaotic sinusoidal components with varying frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += (np.sin(12 * x[i]) * np.cos(7 * x[i]) + 
                         0.3 * np.sin(20 * x[i]) * np.cos(10 * x[i]) + 
                         0.1 * np.sin(25 * x[i]))
        
        # Create enhanced saddle points with higher-order hyperbolic tangent components
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (np.tanh(x[i])**3 - 0.3 * np.tanh(2 * x[i])**2 + 
                           0.05 * np.tanh(3 * x[i]))
        
        # Enhanced nested structure with more complex local minima
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += (0.15 * np.sin(25 * x[i]) * np.cos(12 * x[i]) * 
                           np.exp(-0.15 * x[i]**2) + 
                           0.05 * np.sin(30 * x[i]) * np.cos(15 * x[i]))
        
        # Improved interaction term between dimensions with non-linear coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += (0.08 * np.sin(6 * (x[i] + x[j])) * 
                                   np.cos(4 * (x[i] - x[j])) * 
                                   np.exp(-0.05 * (x[i]**2 + x[j]**2)))
        
        # Add a more complex scaling factor with exponential dependence
        scaling_factor = 1.0 + 0.15 * np.sum(np.abs(x_norm)) + 0.05 * np.sum(x_norm**3)
        
        # Combine all terms
        result = quadratic + trig_term + saddle_term + nested_term + interaction_term
        
        # Apply final scaling
        result *= scaling_factor
        
        return result