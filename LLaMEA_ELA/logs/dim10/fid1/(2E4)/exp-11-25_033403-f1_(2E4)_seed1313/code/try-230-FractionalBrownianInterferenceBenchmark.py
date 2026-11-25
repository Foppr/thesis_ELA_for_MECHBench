import numpy as np

class FractionalBrownianInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractional Brownian motion parameters
        self.hurst_exponents = np.random.uniform(0.1, 0.9, dim)
        self.spectral_indices = np.random.uniform(1.0, 3.0, dim)
        self.scaling_factors = np.random.uniform(0.5, 2.0, dim)
        # Interference pattern parameters
        self.interference_frequencies = np.random.uniform(0.5, 5.0, dim)
        self.interference_amplitudes = np.random.uniform(0.1, 2.0, dim)
        self.phase_offsets = np.random.uniform(0, 2*np.pi, dim)
        # Dynamic scaling parameters
        self.dynamic_scaling = np.random.uniform(0.1, 1.5, dim)
        self.scaling_decay = np.random.uniform(0.01, 0.5, dim)
        # Fractal dimension and roughness parameters
        self.fractal_dimensions = np.random.uniform(1.0, 2.5, dim)
        self.roughness_factors = np.random.uniform(0.5, 3.0, dim)
        # Multi-scale harmonic components
        self.harmonic_orders = np.random.randint(2, 10, dim)
        self.frequency_modulation = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize fitness value
        fitness = 0.0
        
        # Fractional Brownian motion component
        fbm_terms = 0.0
        for i in range(self.dim):
            # Create fractional Brownian motion-like behavior using sine waves with varying frequencies
            fbm_term = 0.0
            for k in range(1, 21):  # Sum of 20 harmonic components
                freq = k ** (2.0 * self.hurst_exponents[i])
                amp = 1.0 / (k ** (self.spectral_indices[i] + 0.5))
                fbm_term += amp * np.sin(freq * x[i] + self.phase_offsets[i])
            fbm_terms += fbm_term
            
        # Interference pattern component
        interference_terms = 0.0
        for i in range(self.dim):
            # Sine-wave interference with dynamic scaling and phase modulation
            interference = 0.0
            for k in range(1, self.harmonic_orders[i] + 1):
                freq = self.interference_frequencies[i] * k
                amp = self.interference_amplitudes[i] / (k ** 1.5)
                interference += amp * np.sin(freq * x[i] + self.phase_offsets[i])
            interference_terms += interference
            
        # Dynamic scaling component
        scaling_terms = 0.0
        for i in range(self.dim):
            # Apply dynamic scaling with exponential decay
            scale_factor = self.scaling_factors[i] * np.exp(-self.scaling_decay[i] * np.abs(x[i]))
            # Add fractal dimension scaling
            fractal_scale = (1.0 + self.fractal_dimensions[i] * np.log(1.0 + np.abs(x[i])))
            scaling_terms += scale_factor * fractal_scale * np.sin(self.dynamic_scaling[i] * x[i])
            
        # Roughness and multi-scale component
        roughness_terms = 0.0
        for i in range(self.dim):
            # Add multiple scales of harmonic components with different roughness factors
            roughness = 0.0
            for k in range(1, 15):
                scale = 1.0 / (k ** self.roughness_factors[i])
                roughness += scale * np.sin(k * x[i])
            roughness_terms += roughness
            
        # Combine all components with weighted contributions
        fitness = 0.3 * fbm_terms + 0.4 * interference_terms + 0.2 * scaling_terms + 0.1 * roughness_terms
        
        # Add high-order polynomial terms for additional complexity
        poly_terms = 0.0
        for i in range(self.dim):
            poly_term = 0.0
            for k in range(3, 8):
                poly_term += (x[i]**k) / (k * self.fractal_dimensions[i])
            poly_terms += poly_term
            
        fitness += 0.05 * poly_terms
        
        # Add frequency modulation for increased complexity
        freq_mod_terms = 0.0
        for i in range(self.dim):
            freq_mod = np.sin(self.frequency_modulation[i] * x[i]) * np.cos(self.frequency_modulation[i] * x[i])
            freq_mod_terms += freq_mod
            
        fitness += 0.05 * freq_mod_terms
        
        return fitness