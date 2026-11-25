import numpy as np

class ChaoticSinePolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave parameters with high frequency variations
        self.sine_freqs = 5.0 + 15.0 * np.random.rand(dim)
        self.sine_ampls = 2.0 + 3.0 * np.random.rand(dim)
        # Dynamic polynomial exponents that vary based on dimension
        self.poly_exponents = 1.0 + 5.0 * np.random.rand(dim)
        # Radial barrier coefficients with varying strengths
        self.barrier_coeffs = 0.5 + 4.0 * np.random.rand(dim)
        # Cross-dimensional coupling with chaotic interaction patterns
        self.coupling_matrix = np.random.randn(dim, dim) * 2.0
        # Adaptive scaling factors for each dimension
        self.scaling_factors = 0.1 + 2.9 * np.random.rand(dim)
        # Multi-scale noise with varying amplitudes and frequencies
        self.noise_amps = 0.5 + 2.5 * np.random.rand(dim)
        self.noise_freqs = 1.0 + 8.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-wave component
        sine_term = 0.0
        for i in range(self.dim):
            sine_term += self.sine_ampls[i] * np.sin(self.sine_freqs[i] * x_norm[i])
        
        # Dynamic polynomial component
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += np.power(np.abs(x_norm[i]), self.poly_exponents[i])
        
        # Radial barrier component with exponential decay
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term += self.barrier_coeffs[i] * np.exp(-np.abs(x_norm[i]) / (1.0 + 0.5 * x_norm[i]**2))
        
        # Cross-dimensional chaotic coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.coupling_matrix[i, j] * np.sin(x_norm[i] * x_norm[j])
        
        # Adaptive scaling and conditioning
        scaling_factor = 1.0
        for i in range(self.dim):
            scaling_factor *= (1.0 + self.scaling_factors[i] * np.abs(x_norm[i])**3)
        
        # Multi-scale noise component
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += self.noise_amps[i] * np.cos(self.noise_freqs[i] * x_norm[i])
        
        # Combine all terms with varying weights
        result = 0.25 * sine_term + 0.3 * poly_term + 0.2 * barrier_term + 0.15 * coupling_term + 0.1 * noise_term
        
        # Add a global chaotic penalty term
        penalty = 0.08 * np.sum(np.sin(5.0 * x_norm) ** 2)
        
        return result * scaling_factor + penalty