import numpy as np

class NestedTrigonometricPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for nested trigonometric structure
        self.frequency_scales = np.random.uniform(0.5, 3.0, dim)
        self.amplitude_scales = np.random.uniform(0.1, 2.0, dim)
        self.phase_offsets = np.random.uniform(-np.pi, np.pi, dim)
        self.nesting_levels = np.random.randint(2, 6, dim)
        self.fractal_exponents = np.random.uniform(0.3, 1.8, dim)
        self.coupling_strengths = np.random.uniform(0.2, 1.5, (dim, dim))
        self.modulation_frequencies = np.random.uniform(0.1, 2.0, dim)
        self.adaptive_weights = np.random.uniform(0.5, 2.0, dim)
        self.hierarchical_exponents = np.random.uniform(0.5, 2.5, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested trigonometric polynomial with multiple levels of recursion
        result = 0.0
        for i in range(self.dim):
            # Base level contribution
            base_term = self.amplitude_scales[i] * np.sin(self.frequency_scales[i] * x_norm[i] + self.phase_offsets[i])
            
            # Nested recursive terms with increasing complexity
            nested_value = base_term
            for level in range(1, self.nesting_levels[i]):
                freq_mod = 1.0 + 0.3 * np.sin(level * self.modulation_frequencies[i])
                nested_value = np.sin(freq_mod * nested_value + self.phase_offsets[i]) * \
                              (1.0 + 0.2 * np.cos(level * x_norm[i]))
            
            # Apply hierarchical scaling
            scaled_term = nested_value * self.adaptive_weights[i] * \
                         (np.abs(x_norm[i])**self.hierarchical_exponents[i])
            result += scaled_term
            
        # Fractal-like self-similarity terms with cross-dimensional coupling
        fractal_terms = 0.0
        for i in range(self.dim):
            # Self-similar pattern at multiple scales
            scale_factor = self.fractal_exponents[i]
            fractal_component = np.sum([
                np.sin((scale_factor**k) * x_norm[i]) * 
                (1.0 + 0.1 * np.cos(k * x_norm[i])) * 
                np.exp(-0.5 * (x_norm[i])**2)
                for k in range(1, min(6, int(scale_factor*3)))
            ])
            fractal_terms += fractal_component
            
        # Cross-dimensional coupling with adaptive strength
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = self.coupling_strengths[i, j]
                coupling_term = coupling_strength * np.sin(x_norm[i] + x_norm[j]) * \
                               np.cos(x_norm[i] - x_norm[j])
                coupling_terms += coupling_term
                
        # Additional nonlinear modulation and scaling
        nonlinear_modulation = 0.0
        for i in range(self.dim):
            nonlinear_modulation += (np.sin(x_norm[i]**2) + 
                                   np.cos(x_norm[i]**3)) * \
                                  np.exp(-0.1 * np.abs(x_norm[i]))
            
        # Combine all components with optimized weights
        total = 0.4 * result + 0.3 * fractal_terms + 0.2 * coupling_terms + 0.1 * nonlinear_modulation
        
        return total