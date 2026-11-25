import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic tent map constants
        self.tent_map = np.array([0.5] * dim)  # Initialize with fixed values for stability
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Polynomial coupling terms - creates complex interaction between dimensions
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x[i]**3) * (x[j]**2) + (x[i]**2) * (x[j]**3)
        
        # Tent map chaotic interaction - introduces nonlinearity and sensitivity
        tent_interaction = 0.0
        for i in range(self.dim):
            # Apply chaotic tent map dynamics
            if x_scaled[i] < 0.5:
                tent_val = 2 * x_scaled[i]
            else:
                tent_val = 2 * (1 - x_scaled[i])
            tent_interaction += tent_val * np.sin(x[i])
            
        # Fractal-like radial component with varying exponents
        fractal_term = 0.0
        for i in range(self.dim):
            r = np.abs(x[i])
            # Varying exponents to create fractal structure
            exponent = 1.5 + 0.5 * np.sin(i)
            fractal_term += r**exponent
            
        # Adaptive noise component that depends on solution position
        adaptive_noise = 0.0
        for i in range(self.dim):
            # Noise magnitude increases with distance from origin
            noise_magnitude = 0.1 * (1 + np.abs(x[i]) / 5.0)
            adaptive_noise += noise_magnitude * np.random.uniform(-1, 1)
            
        # Combined function value
        return poly_term + tent_interaction + fractal_term + adaptive_noise + 3.0