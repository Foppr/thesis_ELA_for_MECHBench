import numpy as np

class TentPolynomialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaotic parameters with improved distribution
        self.tent_r = np.random.uniform(2.8, 3.9, dim)
        # Polynomial coupling coefficients with varied degrees
        self.poly_degrees = np.random.randint(3, 7, dim)
        self.poly_coefficients = np.random.uniform(-1.5, 1.5, (dim, 4))
        # Sinusoidal modulation parameters with frequency scaling
        self.sin_amplitudes = np.random.uniform(0.8, 2.5, dim)
        self.sin_frequencies = np.random.randint(2, 10, dim)
        # Additional noise component with adaptive scaling
        self.noise_level = np.random.uniform(0.05, 0.3, dim)
        # Adaptive weights for different components
        self.weights = np.random.uniform(0.6, 1.4, 3)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Tent map chaotic component with enhanced chaos
        tent_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced tent map iteration with multiple steps
            tent_value = xi
            for _ in range(8):  # Increased iterations for stronger chaos
                if tent_value < 0.5:
                    tent_value = self.tent_r[i] * tent_value
                else:
                    tent_value = self.tent_r[i] * (1 - tent_value)
            tent_sum += tent_value * np.sin(xi)  # Add sinusoidal modulation to chaos
        
        # Polynomial coupling component with higher degree terms
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d in range(self.poly_degrees[i]):
                poly_term += self.poly_coefficients[i, d % 4] * (xi ** (d + 1))
            poly_sum += poly_term
        
        # Sinusoidal modulation component with combined harmonics
        sin_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Combine multiple sinusoidal frequencies
            sin_term = (self.sin_amplitudes[i] * 
                       np.sin(self.sin_frequencies[i] * xi) + 
                       self.sin_amplitudes[i] * 
                       np.cos(self.sin_frequencies[i] * xi) +
                       0.5 * self.sin_amplitudes[i] * 
                       np.sin(2 * self.sin_frequencies[i] * xi))
            sin_sum += sin_term
        
        # Add noise component
        noise_sum = 0
        for i in range(self.dim):
            noise_sum += self.noise_level[i] * np.random.uniform(-1, 1)
        
        # Combine all components with adaptive weights
        result = (self.weights[0] * tent_sum + 
                 self.weights[1] * poly_sum + 
                 self.weights[2] * sin_sum + 
                 noise_sum)
        
        return result