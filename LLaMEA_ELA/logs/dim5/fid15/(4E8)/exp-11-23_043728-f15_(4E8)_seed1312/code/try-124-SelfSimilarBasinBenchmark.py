import numpy as np

class SelfSimilarBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.basin_count = 5
        self.fractal_exp = 2.3
        self.gradient_modulation = 1.8
        self.spectral_factor = 3.7
        self.interference_strength = 0.6
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Create self-similar basin structure with multiple attraction points
        basin_centers = np.array([[-0.8, -0.4, 0.0, 0.4, 0.8]] * self.basin_count).T
        basin_strengths = np.array([2.0, 1.5, 1.0, 1.5, 2.0])
        
        # Calculate basin attraction fields with fractal scaling
        basin_fields = np.zeros(self.dim)
        for i in range(self.dim):
            distances = np.abs(x_norm[i] - basin_centers[i % self.basin_count])
            basin_fields[i] = np.sum(basin_strengths * np.exp(-distances**(2.0 + self.fractal_exp)))
        
        # Add spectral interference patterns with multiple frequency components
        spectral_pattern = np.zeros(self.dim)
        for i in range(self.dim):
            freq_base = 2.0 * (i % 5) + 1.0
            spectral_pattern[i] = np.sin(freq_base * x_norm[i]) * np.cos(freq_base * x_norm[i] * 0.5) * \
                                np.sin(freq_base * x_norm[i] * 1.3) * np.cos(freq_base * x_norm[i] * 2.7)
        
        # Combine basin and spectral components
        combined = basin_fields + self.spectral_factor * spectral_pattern
        
        # Apply adaptive gradient modulation based on dimensionality
        grad_mod = 1.0 + self.gradient_modulation * (1.0 / (1.0 + np.exp(-0.5 * (self.dim - 10))))
        
        # Add higher-order polynomial terms for increased ruggedness
        poly_term = np.sum(combined**4) + 0.3 * np.sum(combined**6)
        
        # Introduce interference effects with chaotic modulation
        interference = self.interference_strength * np.sum(np.sin(3.0 * x_norm) * np.cos(2.0 * x_norm))
        
        # Add adaptive penalty for dimensionality and solution distribution
        penalty = 0.1 * self.dim * (np.std(x_norm)**1.5 + 0.05 * np.mean(np.abs(x_norm)))
        
        # Final fitness with adaptive scaling
        scale_factor = 1.0 + 0.02 * np.log(self.dim + 1) + 0.01 * np.sin(self.dim * 0.6)
        
        return scale_factor * (grad_mod * poly_term + interference + penalty)