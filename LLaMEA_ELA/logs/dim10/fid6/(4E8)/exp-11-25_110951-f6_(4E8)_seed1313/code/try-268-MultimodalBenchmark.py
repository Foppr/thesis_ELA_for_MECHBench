import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with log-periodic modulation
        result = 0.0
        for i in range(self.dim):
            # Log-periodic oscillation pattern
            log_periodic = np.log(np.abs(x_norm[i]) + 1e-8) * np.sin(2 * np.pi * np.log(np.abs(x_norm[i]) + 1e-8))
            result += (x_norm[i]**2) * (1.0 + 0.3 * log_periodic)
        
        # Fractal-like interaction terms with self-similarity
        fractal_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Self-similar distance-based interaction
                dist = np.abs(x_norm[i] - x_norm[j])
                fractal_interaction += (1.0 / (dist + 1e-8)) * np.sin(10 * np.log(dist + 1e-8))
        
        # Gradient-based attraction basins with varying depth
        basin_term = 0.0
        for i in range(self.dim):
            # Create multiple local minima with different basin depths
            basin_depth = 1.0 + 0.5 * np.sin(4 * x_norm[i])
            basin_term += basin_depth * (x_norm[i]**2) * (1.0 - np.cos(3 * x_norm[i]))
        
        # Multi-scale sinusoidal modulation with varying frequencies
        multiscale = 0.0
        for i in range(self.dim):
            freqs = [2, 5, 8, 12]
            scale_factor = 1.0 + 0.4 * np.sin(3 * x_norm[i])
            for freq in freqs:
                multiscale += scale_factor * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Global scaling with fractal dimensionality effect
        global_scale = 1.0 + 0.3 * np.exp(-0.5 * np.sum(x_norm**2))
        
        return global_scale * (result + 0.4 * fractal_interaction + 0.3 * basin_term + 0.2 * multiscale)