import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Tent map chaotic parameters
        self.r_values = np.random.uniform(1.5, 2.0, dim)
        # Polynomial drift coefficients (higher degree)
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (dim, 6))
        # Spectral wave components with additional harmonics
        self.wave_amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.wave_frequencies = np.random.randint(1, 12, dim)
        self.wave_phases = np.random.uniform(0, 2*np.pi, dim)
        # Additional harmonic coupling terms
        self.harmonic_couplings = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Control parameters for multimodality and complexity
        self.multimodal_strength = np.random.uniform(1.0, 3.0)
        self.complexity_factor = np.random.uniform(0.5, 2.5)
        
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
            for _ in range(15):  # More transient iterations
                if chaotic_val < 0.5:
                    chaotic_val = self.r_values[i] * chaotic_val
                else:
                    chaotic_val = self.r_values[i] * (1 - chaotic_val)
            # Use final chaotic value as a multiplier with coupling
            coupled_chaotic = chaotic_val
            for j in range(self.dim):
                if i != j:
                    coupled_chaotic += self.harmonic_couplings[i][j] * np.sin(x[j])
            chaotic_sum += coupled_chaotic * np.cos(xi)
        
        # Polynomial drift component (higher degree terms)
        poly_sum = 0
        for i in range(self.dim):
            xi = x[i]
            poly_term = 0
            for d, coeff in enumerate(self.poly_coeffs[i]):
                poly_term += coeff * (xi ** d)
            poly_sum += poly_term
        
        # Spectral wave interference component with multiple harmonics
        wave_sum = 0
        for i in range(self.dim):
            xi = x[i]
            wave_term = 0
            for h in range(1, 4):  # Add 3 harmonic components
                wave_term += (self.wave_amplitudes[i] * 
                            np.sin(h * self.wave_frequencies[i] * xi + self.wave_phases[i]))
            wave_sum += wave_term
        
        # Additional coupling between dimensions in polynomial and wave terms
        coupling_factor = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_factor += self.harmonic_couplings[i][j] * x[i] * x[j]
        
        # Combine components with multimodal scaling and complexity factor
        result = (0.8 * chaotic_sum + 
                 1.5 * poly_sum + 
                 1.0 * wave_sum + 
                 0.3 * coupling_factor) * self.multimodal_strength * self.complexity_factor
        
        return result