import numpy as np

class TentPolynomialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaotic parameters
        self.tent_r = np.random.uniform(1.5, 3.9, dim)
        # Polynomial coupling coefficients
        self.poly_degrees = np.random.randint(2, 6, dim)
        self.poly_coefficients = np.random.uniform(-1.0, 1.0, (dim, 3))
        # Sinusoidal modulation parameters
        self.sin_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.sin_frequencies = np.random.randint(1, 8, dim)
        # Additional noise component
        self.noise_level = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic component
        tent_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Simplified tent map iteration
            tent_value = xi
            for _ in range(5):  # Iterate 5 times for chaos
                if tent_value < 0.5:
                    tent_value = self.tent_r[i] * tent_value
                else:
                    tent_value = self.tent_r[i] * (1 - tent_value)
            tent_sum += tent_value
        
        # Polynomial coupling component
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d in range(self.poly_degrees[i]):
                poly_term += self.poly_coefficients[i, d % 3] * (xi ** (d + 1))
            poly_sum += poly_term
        
        # Sinusoidal modulation component
        sin_sum = 0
        for i in range(self.dim):
            xi = x[i]
            sin_term = (self.sin_amplitudes[i] * 
                       np.sin(self.sin_frequencies[i] * xi) + 
                       self.sin_amplitudes[i] * 
                       np.cos(self.sin_frequencies[i] * xi))
            sin_sum += sin_term
        
        # Combine all components with adjusted weights
        result = (0.7 * tent_sum + 
                 1.3 * poly_sum + 
                 0.5 * sin_sum)
        
        return result