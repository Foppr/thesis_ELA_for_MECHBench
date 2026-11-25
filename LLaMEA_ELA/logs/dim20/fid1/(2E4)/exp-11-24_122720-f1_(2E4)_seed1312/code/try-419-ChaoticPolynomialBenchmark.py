import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaotic parameters
        self.r_values = np.random.uniform(1.8, 2.2, dim)
        # Polynomial drift coefficients
        self.poly_coeffs = np.random.uniform(-1.5, 1.5, (dim, 7))
        # Spectral wave components
        self.wave_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.wave_frequencies = np.random.randint(3, 15, dim)
        self.wave_phases = np.random.uniform(0, 2*np.pi, dim)
        # Additional harmonic coupling terms
        self.harmonic_coeffs = np.random.uniform(-0.5, 0.5, (dim, 4))
        # Control parameter for multimodality
        self.multimodal_strength = np.random.uniform(1.5, 3.5)
        # Additional chaotic feedback parameter
        self.feedback_strength = np.random.uniform(0.2, 0.8, dim)
        # Coupling strength between dimensions
        self.coupling_strength = np.random.uniform(0.3, 1.2, (dim, dim))
        # Additional sinusoidal modulation
        self.sin_modulation = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component
        chaotic_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Initialize chaotic value
            chaotic_val = 0.5
            # Iterate tent map with more iterations
            for _ in range(25):  # Transient iterations
                if chaotic_val < 0.5:
                    chaotic_val = self.r_values[i] * chaotic_val
                else:
                    chaotic_val = self.r_values[i] * (1 - chaotic_val)
            # Use final chaotic value as a multiplier with feedback
            feedback_term = self.feedback_strength[i] * np.sin(chaotic_val * xi)
            chaotic_sum += chaotic_val * np.cos(xi) + feedback_term
        
        # Polynomial drift component with higher degree terms
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d, coeff in enumerate(self.poly_coeffs[i]):
                poly_term += coeff * (xi ** (d + 1))
            poly_sum += poly_term
        
        # Spectral wave interference component with multiple frequencies
        wave_sum = 0
        for i in range(self.dim):
            xi = x[i]
            wave_term = 0
            for j in range(3):  # Multiple harmonic components
                freq = self.wave_frequencies[i] + j * 2
                amp = self.wave_amplitudes[i] * (1.0 / (j + 1))
                phase = self.wave_phases[i] + j * np.pi/4
                wave_term += amp * np.cos(freq * xi + phase)
            wave_sum += wave_term
        
        # Harmonic coupling terms between dimensions
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strength[i][j] * np.sin(x[i]) * np.cos(x[j])
        
        # Sinusoidal modulation component
        sin_sum = 0
        for i in range(self.dim):
            xi = x[i]
            sin_sum += self.sin_modulation[i] * np.sin(xi**2)
        
        # Combine all components with multimodal scaling
        result = (1.0 * chaotic_sum + 
                 1.5 * poly_sum + 
                 0.8 * wave_sum +
                 0.5 * coupling_sum +
                 0.3 * sin_sum) * self.multimodal_strength
        
        return result