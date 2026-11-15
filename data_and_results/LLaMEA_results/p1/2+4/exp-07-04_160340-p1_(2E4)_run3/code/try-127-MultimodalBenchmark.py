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
        
        # Add periodic trigonometric components with modified frequencies and amplitudes
        trig_term = 0.0
        for i in range(self.dim):
            trig_term += 0.8 * np.sin(12 * x[i]) * np.cos(6 * x[i]) + 0.3 * np.sin(18 * x[i]) + 0.2 * np.cos(9 * x[i])
        
        # Create saddle points with hyperbolic tangent components
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.tanh(1.5 * x[i])**2 - 0.4 * np.tanh(3 * x[i])
        
        # Nested structure with multiple local minima
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += 0.15 * np.sin(25 * x[i]) * np.cos(12 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Add a complex interaction term between dimensions with modified coefficients
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += 0.08 * np.sin(6 * (x[i] + x[j])) * np.cos(4 * (x[i] - x[j])) + 0.03 * np.cos(8 * (x[i] - x[j]))
        
        # Combine all terms
        result = quadratic + trig_term + saddle_term + nested_term + interaction_term
        
        # Add a global scaling factor to control the difficulty
        result *= (1.0 + 0.15 * np.sum(np.abs(x_norm)))
        
        # Shift the global minimum to increase problem difficulty
        result += 0.5 * np.sum(np.sin(0.5 * x)**2)
        
        return result