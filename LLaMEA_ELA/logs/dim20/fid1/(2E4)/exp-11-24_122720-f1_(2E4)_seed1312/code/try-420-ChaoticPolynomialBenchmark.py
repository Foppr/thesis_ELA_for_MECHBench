import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaotic parameters
        self.r_values = np.random.uniform(1.5, 2.0, dim)
        # Polynomial drift coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        # Spectral wave components
        self.wave_amplitudes = np.random.uniform(0.3, 1.5, dim)
        self.wave_frequencies = np.random.randint(2, 10, dim)
        self.wave_phases = np.random.uniform(0, 2*np.pi, dim)
        # Control parameter for multimodality
        self.multimodal_strength = np.random.uniform(0.8, 2.5)
        # Additional chaotic feedback parameter
        self.feedback_strength = np.random.uniform(0.1, 0.5, dim)
        # Interaction terms between dimensions
        self.interaction_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component
        chaotic_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Initialize chaotic value
            chaotic_val = 0.5
            # Iterate tent map
            for _ in range(15):  # Transient iterations
                if chaotic_val < 0.5:
                    chaotic_val = self.r_values[i] * chaotic_val
                else:
                    chaotic_val = self.r_values[i] * (1 - chaotic_val)
            # Use final chaotic value as a multiplier with feedback
            feedback_term = self.feedback_strength[i] * np.sin(chaotic_val * xi)
            chaotic_sum += chaotic_val * np.cos(xi) + feedback_term
        
        # Polynomial drift component
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d, coeff in enumerate(self.poly_coeffs[i]):
                poly_term += coeff * (xi ** (d + 1))
            poly_sum += poly_term
        
        # Spectral wave interference component
        wave_sum = 0
        for i in range(self.dim):
            xi = x[i]
            wave_term = (self.wave_amplitudes[i] * 
                        np.cos(self.wave_frequencies[i] * xi + self.wave_phases[i]))
            wave_sum += wave_term
        
        # Interaction terms between dimensions
        interaction_sum = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_sum += self.interaction_coeffs[i][j] * x[i] * x[j]
        
        # Combine components with multimodal scaling
        result = (0.8 * chaotic_sum + 
                 1.2 * poly_sum + 
                 0.7 * wave_sum + 
                 0.3 * interaction_sum) * self.multimodal_strength
        
        return result