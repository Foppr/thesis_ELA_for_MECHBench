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
        
        # Add periodic trigonometric components with varying frequencies
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += np.sin(10 * x[i]) * np.cos(5 * x[i]) + 0.5 * np.sin(15 * x[i])
        
        # Create saddle points with hyperbolic tangent components
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.tanh(x[i])**2 - 0.5 * np.tanh(2 * x[i])
        
        # Nested structure with multiple local minima
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += 0.1 * np.sin(20 * x[i]) * np.cos(10 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add a complex interaction term between dimensions
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += 0.05 * np.sin(5 * (x[i] + x[j])) * np.cos(3 * (x[i] - x[j]))
        
        # Combine all terms
        result = quadratic + trig_term + saddle_term + nested_term + interaction_term
        
        # Add a global scaling factor to control the difficulty
        result *= (1.0 + 0.1 * np.sum(np.abs(x_norm)))
        
        return result