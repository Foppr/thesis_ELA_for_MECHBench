import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute scaling factors for fractional Brownian motion-like behavior
        self.scaling_factors = np.array([0.5 + 0.5 * np.sin(i * 0.7) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic with dynamic scaling
        result = np.sum(self.scaling_factors * (x - 1.0)**2)
        
        # Add chaotic interaction terms with nested structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use a chaotic interaction function
                interaction = np.sin(10.0 * (x[i] - x[j])) * np.exp(-0.1 * (x[i] - x[j])**2)
                result += 0.3 * interaction
        
        # Add fractional Brownian motion-like correlation
        fbm_term = 0.0
        for i in range(self.dim):
            fbm_term += self.scaling_factors[i] * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
        result += 0.2 * fbm_term
        
        # Add nested attractor structure with dynamic scaling
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += (x[i] - 0.5 * np.sin(3.0 * x[i]))**2
        result += 0.1 * nested_term
        
        # Add dynamic global minimum shift based on dimension
        shift = np.sum(np.sin(np.arange(self.dim) * 0.5) * x)
        result += 0.05 * shift**2
        
        # Add a complex sinusoidal modulation to increase landscape ruggedness
        mod_term = 0.0
        for i in range(self.dim):
            mod_term += np.sin(5.0 * x[i]) * np.cos(4.0 * x[i]) * np.sin(2.0 * x[i])
        result += 0.15 * mod_term
        
        return result