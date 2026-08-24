import numpy as np

class ChaoticNeuralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        # Precompute chaotic parameters
        self.weights = np.random.uniform(-1.0, 1.0, dim)
        self.biases = np.random.uniform(-0.5, 0.5, dim)
        self.chaotic_params = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply chaotic neural network dynamics
        result = 0.0
        for i in range(self.dim):
            # Dynamic weight modulation based on position
            mod_weight = self.weights[i] * (1.0 + 0.3 * np.sin(self.chaotic_params[i] * x[i]))
            
            # Neural activation with polynomial chaos components
            activation = mod_weight * x[i] + self.biases[i]
            chaos_term = 0.1 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
            
            # Polynomial chaos expansion
            poly_term = 0.05 * x[i]**3 + 0.02 * x[i]**4 + 0.005 * x[i]**6
            
            # Basin structure with adaptive scaling
            basin_scale = 1.0 + 0.2 * np.tanh(0.5 * x[i])
            
            result += activation**2 + chaos_term + poly_term * basin_scale
            
        # Cross-dimensional coupling with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.05 * np.sin(3.0 * x[i] + 2.0 * x[j]) * np.cos(1.5 * x[i] - x[j])
                result += coupling * (1.0 + 0.1 * np.sin(12.0 * x[i]))
                
        # Global conditioning with fractal-like scaling
        fractal_scale = 1.0 + 0.15 * np.sum(np.sin(5.0 * x) * np.cos(3.0 * x))
        result = result * fractal_scale
        
        return result