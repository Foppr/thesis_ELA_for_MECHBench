import numpy as np

class ChaoticFractalHarmonicLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic fractal pattern parameters
        self.fractal_centers = np.random.uniform(-4.5, 4.5, (8, dim))
        self.fractal_scales = np.random.uniform(0.3, 2.5, (8, dim))
        self.fractal_weights = np.random.uniform(0.2, 3.0, 8)
        # Initialize chaotic harmonic oscillation components
        self.oscillation_frequencies = np.random.uniform(0.5, 6.0, (6, dim))
        self.oscillation_amplitudes = np.random.uniform(0.3, 3.0, (6, dim))
        self.oscillation_phases = np.random.uniform(0, 2*np.pi, (6, dim))
        # Initialize chaotic conditioning layers
        self.conditioning_coeffs = np.random.uniform(0.05, 2.5, dim)
        self.conditioning_exponents = np.random.uniform(0.5, 4.0, dim)
        # Additional chaotic interaction terms
        self.interaction_coefficients = np.random.uniform(-1.0, 1.0, (dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic fractal-based self-similarity pattern
        fractal_potential = 0.0
        for i in range(8):
            fractal_dist = 0.0
            for j in range(self.dim):
                scaled_x = (x[j] - self.fractal_centers[i, j]) / self.fractal_scales[i, j]
                fractal_dist += scaled_x**2
            fractal_potential += self.fractal_weights[i] * np.exp(-0.3 * fractal_dist)
        
        # Add chaotic harmonic oscillation components with dynamic interaction
        harmonic_terms = 0.0
        for i in range(6):
            harmonic_sum = 0.0
            for j in range(self.dim):
                harmonic_sum += self.oscillation_amplitudes[i, j] * np.sin(
                    self.oscillation_frequencies[i, j] * x[j] + 
                    self.oscillation_phases[i, j]
                )
            # Add chaotic interaction term between dimensions
            interaction_term = 0.0
            for k in range(self.dim):
                if k != i % self.dim:
                    interaction_term += self.interaction_coefficients[i % self.dim, k] * x[k]
            harmonic_terms += np.cos(harmonic_sum + interaction_term)
        
        # Add chaotic conditioning layers with modified exponents
        conditioning_terms = 0.0
        for j in range(self.dim):
            conditioning_terms += self.conditioning_coeffs[j] * (
                np.abs(x[j])**self.conditioning_exponents[j]
            )
        
        # Combine all components with varying weights and chaotic modulation
        total = 0.8 * fractal_potential + 0.6 * harmonic_terms + 1.5 * conditioning_terms
        
        return total