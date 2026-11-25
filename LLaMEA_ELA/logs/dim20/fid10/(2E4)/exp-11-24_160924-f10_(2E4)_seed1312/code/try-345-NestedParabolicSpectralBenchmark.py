import numpy as np

class NestedParabolicSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for nested parabolic wells
        self.well_depths = np.random.uniform(1.0, 5.0, dim)
        self.well_positions = np.random.uniform(-4.0, 4.0, dim)
        self.well_widths = np.random.uniform(0.5, 2.0, dim)
        self.nested_scales = np.random.uniform(0.1, 1.0, dim)
        # Spectral band parameters
        self.spectral_frequencies = np.random.uniform(1.0, 5.0, dim)
        self.spectral_amplitudes = np.random.uniform(0.5, 2.0, dim)
        # Noise modulation parameters
        self.noise_levels = np.random.uniform(0.01, 0.3, dim)
        self.noise_frequency = np.random.uniform(0.5, 2.0, dim)
        # Interaction parameters - modified for increased complexity and better fitness
        self.interaction_strengths = np.random.uniform(0.3, 2.0, (dim, dim))
        # Added exponential-based cross-dimensional coupling for enhanced complexity
        self.exp_coupling_strengths = np.random.uniform(0.1, 1.0, (dim, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Nested parabolic wells with hyperbolic scaling
        for i in range(self.dim):
            xi = x[i]
            depth = self.well_depths[i]
            position = self.well_positions[i]
            width = self.well_widths[i]
            scale = self.nested_scales[i]
            
            # Hyperbolic parabolic well with nested structure
            distance = np.abs(xi - position)
            parabolic_term = depth * (distance / width)**2
            # Add hyperbolic scaling for nested effect
            nested_term = scale * np.log(1 + parabolic_term)
            result += nested_term
            
        # Spectral band interactions
        for i in range(self.dim):
            xi = x[i]
            freq = self.spectral_frequencies[i]
            amp = self.spectral_amplitudes[i]
            
            # Spectral band interaction with sinusoidal modulation
            spectral_interaction = amp * np.sin(freq * xi) * np.cos(freq * xi)
            result += spectral_interaction
            
        # Cross-dimensional interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                strength = self.interaction_strengths[i][j]
                
                # Cross-dimension parabolic interaction
                interaction_term = strength * (xi - xj)**2
                result += interaction_term
                
                # Add exponential-based coupling for enhanced complexity
                exp_coupling = self.exp_coupling_strengths[i][j] * np.exp(-0.5 * (xi - xj)**2)
                result += exp_coupling
                
        # Adaptive noise modulation
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i]
            freq = self.noise_frequency[i]
            
            # Adaptive noise with spectral characteristics
            noise_component = noise_level * np.sin(freq * xi) * np.cos(freq * xi)
            noise_component += 0.3 * np.sin(2 * freq * xi) * np.cos(2 * freq * xi)
            result += noise_component
            
        # Global scaling with spectral modulation
        global_factor = 1.0 + 0.5 * np.sin(np.sum(x) / self.dim)
        global_factor *= (1.0 + 0.3 * np.cos(2.0 * np.sum(x)))
        result *= global_factor
        
        return result