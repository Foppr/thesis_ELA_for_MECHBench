import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map chaotic parameters
        self.r_values = np.random.uniform(3.5, 4.0, dim)
        # Polynomial drift coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 4))
        # Spectral wave components
        self.wave_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.wave_frequencies = np.random.randint(1, 8, dim)
        self.wave_phases = np.random.uniform(0, 2*np.pi, dim)
        # Control parameter for multimodality
        self.multimodal_strength = np.random.uniform(0.5, 2.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map component
        chaotic_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Initialize chaotic value
            chaotic_val = 0.5
            # Iterate logistic map
            for _ in range(10):  # Transient iterations
                chaotic_val = self.r_values[i] * chaotic_val * (1 - chaotic_val)
            # Use final chaotic value as a multiplier
            chaotic_sum += chaotic_val * np.sin(xi)
        
        # Polynomial drift component
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d, coeff in enumerate(self.poly_coeffs[i]):
                poly_term += coeff * (xi ** d)
            poly_sum += poly_term
        
        # Spectral wave interference component
        wave_sum = 0
        for i in range(self.dim):
            xi = x[i]
            wave_term = (self.wave_amplitudes[i] * 
                        np.sin(self.wave_frequencies[i] * xi + self.wave_phases[i]))
            wave_sum += wave_term
        
        # Combine components with multimodal scaling
        result = (0.7 * chaotic_sum + 
                 1.3 * poly_sum + 
                 0.8 * wave_sum) * self.multimodal_strength
        
        return result