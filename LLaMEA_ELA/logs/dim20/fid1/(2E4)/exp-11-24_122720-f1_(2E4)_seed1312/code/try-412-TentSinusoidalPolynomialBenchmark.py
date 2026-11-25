import numpy as np

class TentSinusoidalPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map parameters for chaos generation
        self.tent_params = np.random.uniform(1.5, 2.0, dim)
        # Sinusoidal modulation frequencies and amplitudes
        self.sin_freq = np.random.uniform(0.5, 3.0, dim)
        self.sin_amp = np.random.uniform(0.5, 2.0, dim)
        # Polynomial interpolation coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        # Control parameters for landscape complexity
        self.complexity_factor = np.random.uniform(0.5, 2.5)
        self.multimodal_depth = np.random.uniform(1.0, 3.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic component
        tent_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Initialize chaotic value
            tent_val = 0.5
            # Iterate tent map
            for _ in range(15):  # Transient iterations
                if tent_val < 0.5:
                    tent_val = self.tent_params[i] * tent_val
                else:
                    tent_val = self.tent_params[i] * (1 - tent_val)
            # Use final chaotic value to modulate sinusoidal term
            tent_sum += tent_val * np.sin(self.sin_freq[i] * xi) * self.sin_amp[i]
        
        # Polynomial interpolation component
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d, coeff in enumerate(self.poly_coeffs[i]):
                poly_term += coeff * (xi ** d)
            poly_sum += poly_term
        
        # Sinusoidal modulation component
        sin_sum = 0
        for i in range(self.dim):
            xi = x[i]
            sin_term = np.sin(self.sin_freq[i] * xi + np.pi/4) * self.sin_amp[i]
            sin_sum += sin_term
        
        # Combine all components with scaling factors
        result = (self.multimodal_depth * tent_sum + 
                 0.5 * poly_sum + 
                 0.3 * sin_sum) * self.complexity_factor
        
        return result