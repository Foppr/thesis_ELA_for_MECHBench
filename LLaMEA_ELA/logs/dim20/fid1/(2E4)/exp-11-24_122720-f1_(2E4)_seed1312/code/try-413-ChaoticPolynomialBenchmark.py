import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map chaotic parameters with enhanced distribution
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        # Polynomial drift coefficients with varied degrees
        self.poly_degrees = np.random.randint(2, 6, dim)
        self.poly_coefficients = np.random.uniform(-2.0, 2.0, (dim, 3))
        # Spectral wave interference parameters with frequency scaling
        self.wave_amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.wave_frequencies = np.random.randint(1, 8, dim)
        # Additional noise component with adaptive scaling
        self.noise_level = np.random.uniform(0.1, 0.5, dim)
        # Adaptive weights for different components
        self.weights = np.random.uniform(0.5, 1.5, 3)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component with enhanced chaos
        logistic_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced logistic map iteration with multiple steps
            logistic_value = xi
            for _ in range(10):  # Increased iterations for stronger chaos
                logistic_value = self.logistic_r[i] * logistic_value * (1 - logistic_value)
            logistic_sum += logistic_value * np.cos(xi)  # Add cosine modulation to chaos
        
        # Polynomial drift component with higher degree terms
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d in range(self.poly_degrees[i]):
                poly_term += self.poly_coefficients[i, d % 3] * (xi ** (d + 1))
            poly_sum += poly_term
        
        # Spectral wave interference component with combined harmonics
        wave_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Combine multiple wave frequencies
            wave_term = (self.wave_amplitudes[i] * 
                        np.sin(self.wave_frequencies[i] * xi) + 
                        self.wave_amplitudes[i] * 
                        np.cos(self.wave_frequencies[i] * xi) +
                        0.3 * self.wave_amplitudes[i] * 
                        np.sin(3 * self.wave_frequencies[i] * xi))
            wave_sum += wave_term
        
        # Add noise component
        noise_sum = 0
        for i in range(self.dim):
            noise_sum += self.noise_level[i] * np.random.uniform(-1, 1)
        
        # Combine all components with adaptive weights
        result = (self.weights[0] * logistic_sum + 
                 self.weights[1] * poly_sum + 
                 self.weights[2] * wave_sum + 
                 noise_sum)
        
        return result