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
            result += (x_norm[i]**2) * (1.0 + 0.5 * log_periodic)
        
        # Enhanced fractal-like interaction terms with self-similarity and chaotic coupling
        fractal_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic distance-based interaction with exponential scaling
                dist = np.abs(x_norm[i] - x_norm[j])
                fractal_interaction += (1.0 / (dist + 1e-8)) * (
                    np.sin(10 * np.log(dist + 1e-8)) + 
                    0.7 * np.cos(15 * np.log(dist + 1e-8)) +
                    0.3 * np.sin(25 * np.log(dist + 1e-8))
                )
        
        # Enhanced gradient-based attraction basins with varying depth and chaotic structure
        basin_term = 0.0
        for i in range(self.dim):
            # Create multiple local minima with chaotic basin depths
            basin_depth = 1.0 + 0.7 * np.sin(4 * x_norm[i]) * np.cos(3 * x_norm[i])
            basin_term += basin_depth * (x_norm[i]**2) * (
                1.0 - np.cos(3 * x_norm[i]) + 
                0.4 * np.sin(5 * x_norm[i])
            )
        
        # Enhanced multi-scale sinusoidal modulation with varying frequencies and amplitudes
        multiscale = 0.0
        for i in range(self.dim):
            freqs = [2, 5, 8, 12, 18]
            scale_factor = 1.0 + 0.6 * np.sin(3 * x_norm[i]) * np.cos(2 * x_norm[i])
            for freq in freqs:
                multiscale += scale_factor * (
                    np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) +
                    0.5 * np.cos(freq * x_norm[i]) * np.sin(freq * x_norm[i])
                )
        
        # Asymmetric elliptic structures with dynamic weighting
        elliptic_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric elliptic interaction with dynamic weights
                weight_i = 1.0 + 0.3 * np.sin(x_norm[i])
                weight_j = 1.0 + 0.3 * np.cos(x_norm[j])
                dist_squared = (x_norm[i] - x_norm[j])**2
                elliptic_term += weight_i * weight_j * np.exp(-dist_squared / 2.0) * (
                    np.sin(5 * dist_squared) + 0.5 * np.cos(10 * dist_squared)
                )
        
        # Exponential potentials with cross-dimensional interactions
        exp_potential = 0.0
        for i in range(self.dim):
            exp_potential += np.exp(-0.5 * x_norm[i]**2) * (
                1.0 + 0.4 * np.sin(8 * x_norm[i]) + 
                0.3 * np.cos(6 * x_norm[i])
            )
        
        # Global scaling with fractal dimensionality effect and chaotic modulation
        global_scale = 1.0 + 0.5 * np.exp(-0.5 * np.sum(x_norm**2)) * (
            1.0 + 0.3 * np.sin(10 * np.sum(x_norm**2))
        )
        
        # Combine all components with dynamic weighting
        return global_scale * (
            result + 
            0.5 * fractal_interaction + 
            0.4 * basin_term + 
            0.3 * multiscale + 
            0.2 * elliptic_term + 
            0.1 * exp_potential
        )