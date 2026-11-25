import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute hyperchaotic logistic map constants
        self.logistic_map = np.array([0.5] * dim)  # Initialize with fixed values for stability
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Higher-order polynomial coupling terms - creates even more complex interaction between dimensions
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += 0.8 * (x[i]**4) * (x[j]**3) + 0.6 * (x[i]**3) * (x[j]**4) + 0.3 * (x[i]**2) * (x[j]**5)
        
        # Hyperchaotic logistic map interaction - introduces even more nonlinearity and sensitivity
        logistic_interaction = 0.0
        for i in range(self.dim):
            # Apply hyperchaotic logistic map dynamics
            r = 3.99  # Hyperchaotic parameter
            logistic_val = r * x_scaled[i] * (1 - x_scaled[i])
            logistic_interaction += 0.7 * logistic_val * np.cos(x[i]) + 0.3 * np.sin(x[i])
            
        # Multi-scale fractal-like radial component with varying exponents and scaling factors
        fractal_term = 0.0
        for i in range(self.dim):
            r = np.abs(x[i])
            # Multiple scales with different exponents to create multi-fractal structure
            exponent1 = 1.3 + 0.2 * np.sin(i)
            exponent2 = 1.9 + 0.1 * np.cos(i)
            fractal_term += 0.8 * r**exponent1 + 0.4 * r**exponent2
            
        # Multi-scale adaptive noise component that depends on solution position and multiple frequencies
        adaptive_noise = 0.0
        for i in range(self.dim):
            # Multiple noise scales with different magnitudes
            noise_magnitude1 = 0.12 * (1 + np.abs(x[i]) / 4.0)
            noise_magnitude2 = 0.06 * (1 + np.abs(x[i]) / 2.5)
            adaptive_noise += noise_magnitude1 * np.random.uniform(-1, 1) + \
                             noise_magnitude2 * np.sin(x[i] * 2 * np.pi) * np.cos(x[i] * 3 * np.pi)
            
        # Combined function value
        return poly_term + logistic_interaction + fractal_term + adaptive_noise + 4.5