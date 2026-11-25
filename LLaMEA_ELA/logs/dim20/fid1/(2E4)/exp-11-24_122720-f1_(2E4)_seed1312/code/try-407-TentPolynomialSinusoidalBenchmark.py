import numpy as np

class TentPolynomialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaotic parameters with higher complexity
        self.tent_r = np.random.uniform(2.8, 3.9, dim)
        # Additional fractal-like parameter for self-similarity
        self.fractal_exponents = np.random.uniform(0.3, 0.8, dim)
        # Polynomial coupling with higher degrees and more terms
        self.poly_degrees = np.random.randint(3, 8, dim)
        self.poly_coefficients = np.random.uniform(-2.0, 2.0, (dim, 5))
        # Sinusoidal modulation with multiple frequencies and harmonics
        self.sin_amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.sin_frequencies = np.random.randint(2, 12, dim)
        self.sin_harmonics = np.random.randint(1, 4, dim)
        # Additional noise component with dynamic scaling
        self.noise_level = np.random.uniform(0.2, 1.0, dim)
        # New parameter for sharp fitness transitions
        self.transition_widths = np.random.uniform(0.1, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic component with multiple iterations
        tent_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Multi-iteration tent map with fractal-like behavior
            tent_value = xi
            for _ in range(10):  # More iterations for stronger chaos
                if tent_value < 0.5:
                    tent_value = self.tent_r[i] * tent_value
                else:
                    tent_value = self.tent_r[i] * (1 - tent_value)
            
            # Apply fractal scaling effect
            fractal_effect = np.power(np.abs(tent_value), self.fractal_exponents[i])
            tent_sum += fractal_effect
        
        # Polynomial coupling component with higher order terms
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d in range(self.poly_degrees[i]):
                poly_term += self.poly_coefficients[i, d % 5] * (xi ** (d + 1))
            poly_sum += poly_term
        
        # Sinusoidal modulation with multiple harmonics and transition effects
        sin_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Base sinusoidal term
            sin_term = self.sin_amplitudes[i] * np.sin(self.sin_frequencies[i] * xi)
            # Add harmonic components
            for h in range(1, self.sin_harmonics[i]):
                sin_term += (self.sin_amplitudes[i] / (h + 1)) * np.sin(h * self.sin_frequencies[i] * xi)
            
            # Apply transition sharpness effect
            transition_effect = np.exp(-np.power(xi / self.transition_widths[i], 2))
            sin_sum += sin_term * transition_effect
        
        # Combine all components with new weights and add noise
        result = (0.8 * tent_sum + 
                 1.5 * poly_sum + 
                 0.7 * sin_sum +
                 np.sum(self.noise_level * np.random.uniform(-1, 1, self.dim)))
        
        return result