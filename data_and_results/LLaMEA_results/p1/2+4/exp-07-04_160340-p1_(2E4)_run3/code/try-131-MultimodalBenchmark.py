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
        
        # Base quadratic term with adaptive conditioning
        quadratic = np.sum(x_norm**2) * (1.0 + 0.1 * np.sum(np.abs(x_norm)))
        
        # Fractal-like trigonometric components with exponentially increasing frequencies
        trig_term = 0.0
        for i in range(self.dim):
            freq = 2**(i+1)
            trig_term += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0) * np.exp(-0.01 * i)
        
        # Chaotic saddle points with fractional powers
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (np.tanh(x[i]**1.5) - 0.5 * np.tanh(x[i]**0.5)) * np.exp(-0.05 * i)
        
        # Nested structure with exponentially decaying local minima
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += 0.01 * np.sin(50 * x[i]) * np.cos(25 * x[i]) * np.exp(-0.2 * x[i]**2) * np.exp(-0.1 * i)
        
        # Complex interaction term with fractal dimensionality
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create fractal-like interaction with varying strength
                strength = 0.02 * (1.0 + 0.5 * np.sin(i * j))
                interaction_term += strength * np.sin(3 * (x[i] + x[j])) * np.cos(7 * (x[i] - x[j])) * np.exp(-0.02 * (i+j))
        
        # Add chaotic noise component for increased ruggedness
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += 0.005 * np.sin(100 * x[i]) * np.cos(50 * x[i]) * np.tanh(x[i]**3)
        
        # Combine all terms with adaptive weighting
        result = quadratic + trig_term + saddle_term + nested_term + interaction_term + noise_term
        
        # Add a global scaling factor with fractal-like complexity
        scaling = 1.0 + 0.2 * np.sum(np.abs(x_norm)) + 0.05 * np.sin(np.sum(x_norm))
        result *= scaling
        
        return result