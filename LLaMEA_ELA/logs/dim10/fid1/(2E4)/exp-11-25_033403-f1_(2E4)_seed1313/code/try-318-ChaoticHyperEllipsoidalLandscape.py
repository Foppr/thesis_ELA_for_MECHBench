import numpy as np

class ChaoticHyperEllipsoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic hyper-ellipsoidal structures
        self.ellipsoid_centers = np.random.uniform(-4.0, 4.0, (6, dim))
        self.ellipsoid_radii = np.random.uniform(0.5, 3.0, (6, dim))
        self.ellipsoid_weights = np.random.uniform(0.5, 3.0, 6)
        # Initialize chaotic sine-wave modulations
        self.modulation_frequencies = np.random.uniform(1.0, 8.0, (4, dim))
        self.modulation_amplitudes = np.random.uniform(0.2, 2.0, (4, dim))
        self.modulation_phases = np.random.uniform(0, 2*np.pi, (4, dim))
        # Initialize momentum-based gradient steering
        self.momentum_coeffs = np.random.uniform(0.1, 1.5, dim)
        self.momentum_exponents = np.random.uniform(1.2, 3.0, dim)
        # Initialize fractal-like interaction terms
        self.fractal_interaction_weights = np.random.uniform(0.3, 2.5, (5, dim))
        self.fractal_interaction_exponents = np.random.uniform(0.5, 2.0, (5, dim))
        # Initialize adaptive conditioning
        self.conditioning_coeffs = np.random.uniform(0.05, 2.0, dim)
        self.conditioning_exponents = np.random.uniform(0.8, 3.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic hyper-ellipsoidal structures
        ellipsoid_potential = 0.0
        for i in range(6):
            ellipsoid_dist = 0.0
            for j in range(self.dim):
                scaled_x = (x[j] - self.ellipsoid_centers[i, j]) / self.ellipsoid_radii[i, j]
                ellipsoid_dist += scaled_x**2
            ellipsoid_potential += self.ellipsoid_weights[i] * np.exp(-0.5 * ellipsoid_dist)
        
        # Add chaotic sine-wave modulations
        modulation_terms = 0.0
        for i in range(4):
            modulation_sum = 0.0
            for j in range(self.dim):
                modulation_sum += self.modulation_amplitudes[i, j] * np.sin(
                    self.modulation_frequencies[i, j] * x[j] + 
                    self.modulation_phases[i, j]
                )
            modulation_terms += np.cos(modulation_sum)
        
        # Add momentum-based gradient steering
        momentum_terms = 0.0
        for j in range(self.dim):
            momentum_terms += self.momentum_coeffs[j] * (
                np.abs(x[j])**self.momentum_exponents[j]
            )
        
        # Add fractal-like interaction terms
        fractal_interaction_terms = 0.0
        for i in range(5):
            interaction_sum = 0.0
            for j in range(self.dim):
                interaction_sum += self.fractal_interaction_weights[i, j] * (
                    np.abs(x[j])**self.fractal_interaction_exponents[i, j]
                )
            fractal_interaction_terms += np.exp(-interaction_sum)
        
        # Add adaptive conditioning
        conditioning_terms = 0.0
        for j in range(self.dim):
            conditioning_terms += self.conditioning_coeffs[j] * (
                np.abs(x[j])**self.conditioning_exponents[j]
            )
        
        # Combine all components with varying weights
        total = 1.2 * ellipsoid_potential + 0.8 * modulation_terms + 1.0 * momentum_terms + 0.6 * fractal_interaction_terms + 1.5 * conditioning_terms
        
        return total