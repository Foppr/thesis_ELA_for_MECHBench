import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute hyperchaotic sine map constants
        self.sine_map = np.array([0.5] * dim)  # Initialize with fixed values for stability
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Fractional polynomial coupling terms - creates even more complex interaction between dimensions
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x[i]**2.5) * (x[j]**3.5) + (x[i]**3.5) * (x[j]**2.5) + 0.3 * (x[i]**1.5) * (x[j]**4.5)
        
        # Hyperchaotic sine map interaction - introduces even more nonlinearity and sensitivity
        sine_interaction = 0.0
        for i in range(self.dim):
            # Apply hyperchaotic sine map dynamics
            r = 3.99  # Hyperchaotic parameter
            sine_val = r * np.sin(x_scaled[i]) * (1 - np.sin(x_scaled[i]))
            sine_interaction += sine_val * np.exp(-x[i]**2 / 50.0)
            
        # Multi-scale fractal-like radial component with varying fractional exponents and scaling factors
        fractal_term = 0.0
        for i in range(self.dim):
            r = np.abs(x[i])
            # Multiple scales with different fractional exponents to create multi-fractal structure
            exponent1 = 1.3 + 0.2 * np.sin(i * 0.5)
            exponent2 = 1.7 + 0.1 * np.cos(i * 0.3)
            fractal_term += r**exponent1 + 0.4 * r**exponent2
            
        # Multi-scale adaptive noise component that depends on solution position and multiple frequencies
        adaptive_noise = 0.0
        for i in range(self.dim):
            # Multiple noise scales with different magnitudes
            noise_magnitude1 = 0.12 * (1 + np.abs(x[i]) / 4.0)
            noise_magnitude2 = 0.06 * (1 + np.abs(x[i]) / 2.0)
            adaptive_noise += noise_magnitude1 * np.random.uniform(-1, 1) + \
                             noise_magnitude2 * np.sin(x[i] * 3 * np.pi) * np.cos(x[i] * 5 * np.pi)
            
        # Combined function value
        return poly_term + sine_interaction + fractal_term + adaptive_noise + 4.0