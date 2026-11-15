import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Precompute chaotic coefficients for each dimension
        self.coeffs = np.random.uniform(0.5, 2.0, dim)
        # Precompute polynomial weights for chaos
        self.poly_weights = np.random.uniform(-1.0, 1.0, (dim, 4))
        # Precompute constraint coefficients
        self.constraint_coeffs = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply chaotic scaling and polynomial chaos
        f_val = 0.0
        for i in range(self.dim):
            # Chaotic term based on sine and cosine with varying frequencies
            chaotic_term = np.sin(self.coeffs[i] * x[i]) * np.cos(self.coeffs[i] * x[i] * 0.7)
            # Polynomial chaos component
            poly_term = (self.poly_weights[i, 0] * x[i]**2 + 
                         self.poly_weights[i, 1] * x[i]**3 + 
                         self.poly_weights[i, 2] * x[i]**4 + 
                         self.poly_weights[i, 3] * x[i]**5)
            # Constraint-based penalty
            constraint_penalty = self.constraint_coeffs[i] * x[i]**2
            
            f_val += chaotic_term + poly_term + constraint_penalty
            
        # Add cross-dimensional interaction terms with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(0.5 * x[i] * x[j]) * np.cos(0.3 * x[i] + 0.4 * x[j])
                f_val += 0.1 * interaction
                
        # Add a dominant saddle-point structure
        saddle_term = np.sum((x - 1.0)**2 * (x + 1.0)**2)
        f_val += 0.05 * saddle_term
        
        # Add noise to increase ruggedness
        noise = np.random.normal(0, 0.05, self.dim)
        f_val += np.sum(noise * x)
        
        # Ensure positivity and add small constant
        f_val = max(f_val, 0.01) + 0.01
        
        return f_val