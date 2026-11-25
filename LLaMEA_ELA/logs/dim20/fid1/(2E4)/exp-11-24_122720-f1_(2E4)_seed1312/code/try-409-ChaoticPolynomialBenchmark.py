import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaotic parameters
        self.r_values = np.random.uniform(1.5, 2.0, dim)
        # Polynomial drift coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        # Spectral wave components
        self.wave_amplitudes = np.random.uniform(0.5, 2.5, dim)
        self.wave_frequencies = np.random.randint(2, 12, dim)
        self.wave_phases = np.random.uniform(0, 2*np.pi, dim)
        # Harmonic coupling terms
        self.harmonic_coupling = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Adaptive scaling factors
        self.scaling_factors = np.random.uniform(0.8, 1.5, dim)
        # Control parameter for multimodality
        self.multimodal_strength = np.random.uniform(1.0, 3.0)
        
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
            # Use final chaotic value as a multiplier
            chaotic_sum += chaotic_val * np.cos(xi)
        
        # Polynomial drift component
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d, coeff in enumerate(self.poly_coeffs[i]):
                poly_term += coeff * (xi ** d)
            poly_sum += poly_term * self.scaling_factors[i]
        
        # Spectral wave interference component
        wave_sum = 0
        for i in range(self.dim):
            xi = x[i]
            wave_term = (self.wave_amplitudes[i] * 
                        np.cos(self.wave_frequencies[i] * xi + self.wave_phases[i]))
            wave_sum += wave_term
        
        # Harmonic coupling component
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.harmonic_coupling[i][j] * np.sin(x[i]) * np.cos(x[j])
        
        # Combine all components with multimodal scaling
        result = (0.6 * chaotic_sum + 
                 1.2 * poly_sum + 
                 0.9 * wave_sum + 
                 0.3 * coupling_sum) * self.multimodal_strength
        
        return result