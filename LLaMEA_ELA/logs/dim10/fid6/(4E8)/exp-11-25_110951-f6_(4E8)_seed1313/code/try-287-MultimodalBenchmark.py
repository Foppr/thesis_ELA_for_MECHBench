import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with enhanced log-periodic modulation
        result = 0.0
        for i in range(self.dim):
            # Enhanced log-periodic oscillation with multiple frequencies
            log_periodic = np.log(np.abs(x_norm[i]) + 1e-8) * (
                np.sin(2 * np.pi * np.log(np.abs(x_norm[i]) + 1e-8)) +
                0.5 * np.sin(4 * np.pi * np.log(np.abs(x_norm[i]) + 1e-8)) +
                0.3 * np.sin(6 * np.pi * np.log(np.abs(x_norm[i]) + 1e-8))
            )
            result += (x_norm[i]**2) * (1.0 + 0.4 * log_periodic)
        
        # Enhanced fractal-like interaction terms with self-similarity
        fractal_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Self-similar distance-based interaction with exponential decay
                dist = np.abs(x_norm[i] - x_norm[j])
                fractal_interaction += (1.0 / (dist + 1e-8)) * (
                    np.sin(10 * np.log(dist + 1e-8)) + 
                    0.5 * np.cos(15 * np.log(dist + 1e-8))
                ) * np.exp(-0.5 * dist**2)
        
        # Enhanced gradient-based attraction basins with varying depth and shape
        basin_term = 0.0
        for i in range(self.dim):
            # Create multiple local minima with different basin depths and shapes
            basin_depth = 1.0 + 0.6 * np.sin(4 * x_norm[i])
            basin_shape = 1.0 + 0.3 * np.cos(2 * x_norm[i])
            basin_term += basin_depth * (x_norm[i]**2) * basin_shape * (
                1.0 - np.cos(3 * x_norm[i]) + 0.2 * np.sin(6 * x_norm[i])
            )
        
        # Multi-scale sinusoidal modulation with varying frequencies and amplitudes
        multiscale = 0.0
        for i in range(self.dim):
            freqs = [2, 5, 8, 12, 15]
            scale_factor = 1.0 + 0.5 * np.sin(3 * x_norm[i]) + 0.3 * np.cos(4 * x_norm[i])
            for k, freq in enumerate(freqs):
                multiscale += scale_factor * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * (
                    1.0 + 0.2 * np.sin(k * x_norm[i])
                )
        
        # Asymmetric elliptic structures with dynamic weighting
        elliptic_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction based on directional differences
                diff = x_norm[i] - x_norm[j]
                elliptic_term += (diff**2) * (
                    1.0 + 0.5 * np.sin(5 * diff) + 0.3 * np.cos(7 * diff)
                ) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Dynamic weighting scheme with fractal dimensionality effect
        global_scale = 1.0 + 0.4 * np.exp(-0.3 * np.sum(x_norm**2)) + 0.2 * np.sin(2 * np.sum(x_norm))
        
        # Add novel exponential potentials and cross-dimensional coupling
        exp_potential = 0.0
        for i in range(self.dim):
            exp_potential += np.exp(-0.5 * x_norm[i]**2) * np.cos(3 * x_norm[i])
            
        # Cross-dimensional interaction with higher-order terms
        cross_dim_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim_interaction += (x_norm[i]**3) * (x_norm[j]**3) * np.sin(2 * (x_norm[i] + x_norm[j]))
        
        # Combine all terms with carefully tuned weights to increase complexity
        return global_scale * (
            result + 
            0.5 * fractal_interaction + 
            0.4 * basin_term + 
            0.3 * multiscale + 
            0.2 * elliptic_term +
            0.1 * exp_potential +
            0.15 * cross_dim_interaction
        )