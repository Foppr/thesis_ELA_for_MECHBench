import numpy as np

class FractalHarmonicConditioningLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal pattern parameters
        self.fractal_centers = np.random.uniform(-4.0, 4.0, (6, dim))
        self.fractal_scales = np.random.uniform(0.5, 2.0, (6, dim))
        self.fractal_weights = np.random.uniform(0.5, 2.0, 6)
        # Initialize harmonic oscillation components
        self.oscillation_frequencies = np.random.uniform(1.0, 5.0, (4, dim))
        self.oscillation_amplitudes = np.random.uniform(0.5, 2.5, (4, dim))
        self.oscillation_phases = np.random.uniform(0, 2*np.pi, (4, dim))
        # Initialize conditioning layers
        self.conditioning_coeffs = np.random.uniform(0.1, 2.0, dim)
        self.conditioning_exponents = np.random.uniform(1.0, 3.0, dim)
        # Add cross-term interaction coefficients
        self.cross_terms = np.random.uniform(-0.5, 0.5, (dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute fractal-based self-similarity pattern
        fractal_potential = 0.0
        for i in range(6):
            fractal_dist = 0.0
            for j in range(self.dim):
                scaled_x = (x[j] - self.fractal_centers[i, j]) / self.fractal_scales[i, j]
                fractal_dist += scaled_x**2
            fractal_potential += self.fractal_weights[i] * np.exp(-0.5 * fractal_dist)
        
        # Add harmonic oscillation components with non-linear coupling
        harmonic_terms = 0.0
        for i in range(4):
            harmonic_sum = 0.0
            for j in range(self.dim):
                harmonic_sum += self.oscillation_amplitudes[i, j] * np.sin(
                    self.oscillation_frequencies[i, j] * x[j] + 
                    self.oscillation_phases[i, j]
                )
            # Apply non-linear transformation to coupling
            harmonic_terms += np.cos(harmonic_sum) * (1.0 + 0.1 * np.sin(harmonic_sum))
        
        # Add adaptive conditioning layers with cross-term interactions
        conditioning_terms = 0.0
        for j in range(self.dim):
            base_term = self.conditioning_coeffs[j] * (np.abs(x[j])**self.conditioning_exponents[j])
            cross_term = 0.0
            for k in range(self.dim):
                if j != k:
                    cross_term += self.cross_terms[j, k] * x[j] * x[k]
            conditioning_terms += base_term + 0.3 * cross_term
        
        # Combine all components with varying weights and add interaction term
        total = 0.7 * fractal_potential + 0.5 * harmonic_terms + 1.3 * conditioning_terms
        
        # Add a small perturbation term to increase complexity
        perturbation = 0.01 * np.sum(np.sin(x) * np.cos(x))
        total += perturbation
        
        return total