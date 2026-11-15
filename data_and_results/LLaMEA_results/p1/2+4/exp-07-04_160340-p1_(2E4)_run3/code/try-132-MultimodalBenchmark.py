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
        
        # Add periodic trigonometric components with altered frequencies and coefficients
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += 0.8 * np.sin(12 * x[i]) * np.cos(6 * x[i]) + 0.3 * np.sin(18 * x[i])
        
        # Create saddle points with modified hyperbolic tangent components
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += 0.7 * np.tanh(1.5 * x[i])**2 - 0.4 * np.tanh(3 * x[i])
        
        # Nested structure with modified local minima characteristics
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += 0.15 * np.sin(25 * x[i]) * np.cos(12 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Add a more complex interaction term between dimensions
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += 0.08 * np.sin(7 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j])) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Combine all terms
        result = quadratic + trig_term + saddle_term + nested_term + interaction_term
        
        # Add a global scaling factor to control the difficulty
        result *= (1.0 + 0.15 * np.sum(np.abs(x_norm)))
        
        return result