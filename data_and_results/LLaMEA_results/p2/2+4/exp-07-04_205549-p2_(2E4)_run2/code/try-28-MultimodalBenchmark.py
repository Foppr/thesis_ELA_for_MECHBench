import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for peak positions and variances
        self.peaks = np.random.rand(dim, 10) * 10 - 5  # Random peak locations in [-5, 5]
        self.variances = 0.5 + np.random.rand(10) * 2  # Variances for each peak
        
    def f(self, x):
        x = np.array(x)
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Gaussian peaks component
        peaks_value = 0.0
        for i in range(10):
            peak_pos = self.peaks[:, i]
            variance = self.variances[i]
            diff = x_norm - peak_pos / 5.0
            peaks_value -= np.exp(-0.5 * np.sum(diff**2 / variance))
        
        # Spiral global attractor term
        spiral = 0.0
        r = np.sqrt(np.sum(x_norm**2))
        theta = np.arctan2(x_norm[1], x_norm[0]) if self.dim >= 2 else 0.0
        spiral = 2.0 * r * np.sin(5 * theta) * np.exp(-0.1 * r**2)
        
        # Cross-dimensional interaction term
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.3 * np.sin(10 * (x_norm[i] + x_norm[j])) * np.cos(8 * (x_norm[i] - x_norm[j]))
        
        # Add a conditioning term to increase difficulty
        conditioning = 0.5 * np.sum(x_norm**4)
        
        return peaks_value + spiral + interaction + conditioning