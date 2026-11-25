import numpy as np

class FractalAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 2.3  # Fractional dimension for fractal structure
        self.attraction_strength = 1.5
        self.frequency_base = 3.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Create fractal-like pattern using fractional Brownian motion approximation
        fractal_pattern = np.zeros(self.dim)
        for i in range(self.dim):
            # Multi-scale fractal contribution with different frequencies
            scale = 2 ** (i % 4)
            freq = self.frequency_base * scale
            fractal_pattern[i] = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.7)
        
        # Add gradient-based attraction fields with multiple local minima
        attraction_fields = np.zeros(self.dim)
        for i in range(self.dim):
            # Create multiple attraction points with varying strengths
            center_points = np.array([-0.8, -0.3, 0.2, 0.7])
            strengths = np.array([1.2, 0.8, 1.0, 0.6])
            
            distances = np.abs(x_norm[i] - center_points)
            attraction_fields[i] = np.sum(strengths * np.exp(-distances**2))
        
        # Combine fractal pattern with attraction fields
        combined_pattern = fractal_pattern + 0.5 * attraction_fields
        
        # Create complex curvature using higher-order polynomial terms
        curvature_term = np.sum(combined_pattern**4) + 0.3 * np.sum(combined_pattern**6)
        
        # Add cross-dimensional coupling with interaction weights
        coupling_strength = 0.15
        coupling_term = coupling_strength * np.sum((x_norm[1:] - x_norm[:-1])**3)
        
        # Introduce non-smooth features to increase optimization difficulty
        non_smooth = 0.2 * np.sum(np.abs(x_norm)**1.7)
        
        # Add dimensionality-dependent penalty for bias reduction
        penalty = 0.05 * self.dim * np.std(x_norm)**2
        
        # Final fitness calculation with adaptive scaling
        adaptive_scale = 1.0 + 0.01 * np.log(self.dim + 1)
        
        return adaptive_scale * (curvature_term + coupling_term + non_smooth + penalty)