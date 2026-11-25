import numpy as np

class PolynomialRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial chaos parameters
        self.poly_degrees = np.random.randint(2, 6, size=dim)
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, size=dim)
        # Ridge function parameters with adaptive scaling
        self.ridge_centers = np.random.uniform(-3.0, 3.0, size=dim)
        self.ridge_widths = np.random.uniform(0.5, 3.0, size=dim)
        self.ridge_amplitudes = np.random.uniform(1.0, 5.0, size=dim)
        # Dynamic gradient modulation parameters
        self.gradient_magnitude = np.random.uniform(0.5, 3.0, size=dim)
        self.gradient_frequency = np.random.uniform(0.1, 2.0, size=dim)
        self.gradient_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Connectivity and conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 10.0, size=dim)
        self.connectivity_strength = np.random.uniform(0.3, 2.0, size=(dim, dim))
        # Adaptive noise components
        self.noise_amplitude = np.random.uniform(0.1, 1.0, size=dim)
        self.noise_frequency = np.random.uniform(0.5, 3.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component
        polynomial_term = 0.0
        for i in range(self.dim):
            poly_val = np.polyval([1] + [0]*(self.poly_degrees[i]-1) + [self.poly_coeffs[i]], x[i])
            polynomial_term += poly_val * self.conditioning_factors[i]
        
        # Ridge function component
        ridge_term = 0.0
        for i in range(self.dim):
            distance = np.abs(x[i] - self.ridge_centers[i])
            ridge_value = self.ridge_amplitudes[i] * np.exp(-distance**2 / (2 * self.ridge_widths[i]**2))
            ridge_term += ridge_value
        
        # Dynamic gradient modulation
        gradient_term = 0.0
        for i in range(self.dim):
            grad_val = self.gradient_magnitude[i] * np.sin(self.gradient_frequency[i] * x[i] + self.gradient_phase[i])
            gradient_term += grad_val * self.conditioning_factors[i]
        
        # Connectivity and conditioning effects
        connectivity_term = 0.0
        for i in range(self.dim):
            conn_val = 0.0
            for j in range(self.dim):
                if i != j:
                    conn_val += self.connectivity_strength[i, j] * np.sin(x[i] - x[j])
            connectivity_term += conn_val * self.conditioning_factors[i]
        
        # Adaptive noise component
        noise_term = 0.0
        for i in range(self.dim):
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i])
            noise_term += noise_val
        
        # Combine all terms with different weights
        return (1.5 * polynomial_term + 
                2.0 * ridge_term + 
                1.2 * gradient_term + 
                0.8 * connectivity_term + 
                0.5 * noise_term)