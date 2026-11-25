import numpy as np

class SelfSimilarBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.basin_count = 5
        self.fractal_exponent = 1.8
        self.gradient_modulation = 0.7
        self.spectral_peak = 3.0
        self.interference_strength = 1.5
        self.adaptive_scale = 2.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Create self-similar basin structure with multiple attraction points
        basin_centers = np.linspace(-0.8, 0.8, self.basin_count)
        basin_strengths = np.ones(self.basin_count) * 2.0
        
        basin_contributions = np.zeros(self.dim)
        for i in range(self.basin_count):
            distances = np.abs(x_norm - basin_centers[i])
            basin_contributions += basin_strengths[i] * np.exp(-distances**self.fractal_exponent)
        
        # Add spectral interference patterns with multiple frequency components
        spectral_pattern = np.zeros(self.dim)
        for i in range(self.dim):
            freq = self.spectral_peak * (i + 1) * 0.5
            spectral_pattern[i] = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.3) + \
                                0.5 * np.sin(freq * x_norm[i] * 2.0)
        
        # Combine basin structure with spectral interference
        combined_field = basin_contributions + self.interference_strength * spectral_pattern
        
        # Apply adaptive gradient modulation based on dimensionality
        grad_modulation = 1.0 + self.gradient_modulation * np.sin(self.dim * 0.5)
        
        # Add higher-order polynomial terms for increased ruggedness
        polynomial_term = np.sum(combined_field**4) + 0.3 * np.sum(combined_field**6)
        
        # Introduce adaptive scaling factor
        scale_factor = self.adaptive_scale * (1.0 + 0.1 * np.sin(self.dim * 0.3))
        
        # Add boundary penalty and dimensionality-dependent complexity
        boundary_penalty = 0.5 * np.sum(np.maximum(0, np.abs(x_norm) - 0.9)**2)
        complexity_factor = 0.2 * self.dim * np.log(self.dim + 1)
        
        return scale_factor * (polynomial_term + boundary_penalty + complexity_factor)