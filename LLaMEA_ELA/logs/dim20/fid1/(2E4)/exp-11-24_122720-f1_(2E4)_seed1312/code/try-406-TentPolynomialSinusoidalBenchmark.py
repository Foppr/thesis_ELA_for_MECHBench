import numpy as np

class TentPolynomialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaotic parameters with increased complexity
        self.tent_r = np.random.uniform(2.8, 3.9, dim)
        # Higher-order polynomial coupling with more terms
        self.poly_degrees = np.random.randint(3, 8, dim)
        self.poly_coefficients = np.random.uniform(-2.0, 2.0, (dim, 5))
        # Enhanced sinusoidal modulation with multiple frequencies
        self.sin_amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.sin_frequencies = np.random.randint(2, 12, dim)
        self.sin_phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Fractal-like geometric distortion component
        self.fractal_amplitudes = np.random.uniform(0.5, 2.5, dim)
        self.fractal_frequencies = np.random.randint(3, 10, dim)
        # Additional noise and coupling terms
        self.noise_level = np.random.uniform(0.2, 1.0, dim)
        self.coupling_strength = np.random.uniform(0.5, 2.0, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic component with multiple iterations
        tent_sum = 0
        for i in range(self.dim):
            xi = x[i]
            tent_value = xi
            for _ in range(10):  # Increased chaos iterations
                if tent_value < 0.5:
                    tent_value = self.tent_r[i] * tent_value
                else:
                    tent_value = self.tent_r[i] * (1 - tent_value)
            tent_sum += tent_value
        
        # Enhanced polynomial coupling with cross-terms
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d in range(self.poly_degrees[i]):
                poly_term += self.poly_coefficients[i, d % 5] * (xi ** (d + 1))
            # Add cross-coupling terms between dimensions
            for j in range(self.dim):
                if i != j:
                    poly_term += self.coupling_strength[i, j] * x[i] * x[j]
            poly_sum += poly_term
        
        # Enhanced sinusoidal modulation with phase shifts and multiple harmonics
        sin_sum = 0
        for i in range(self.dim):
            xi = x[i]
            sin_term = (self.sin_amplitudes[i] * 
                       np.sin(self.sin_frequencies[i] * xi + self.sin_phase_shifts[i]) + 
                       self.sin_amplitudes[i] * 
                       np.cos(self.sin_frequencies[i] * xi + self.sin_phase_shifts[i]))
            # Add higher harmonics
            sin_term += 0.5 * self.sin_amplitudes[i] * np.sin(2 * self.sin_frequencies[i] * xi + self.sin_phase_shifts[i])
            sin_sum += sin_term
        
        # Fractal-like geometric distortion component
        fractal_sum = 0
        for i in range(self.dim):
            xi = x[i]
            fractal_term = self.fractal_amplitudes[i] * np.sin(self.fractal_frequencies[i] * xi) * np.cos(self.fractal_frequencies[i] * xi)
            fractal_sum += fractal_term
        
        # Combine all components with adjusted weights
        result = (0.8 * tent_sum + 
                 1.5 * poly_sum + 
                 0.6 * sin_sum + 
                 0.4 * fractal_sum)
        
        # Add noise component
        noise = np.sum(self.noise_level * np.random.uniform(-1, 1, self.dim))
        result += noise
        
        return result