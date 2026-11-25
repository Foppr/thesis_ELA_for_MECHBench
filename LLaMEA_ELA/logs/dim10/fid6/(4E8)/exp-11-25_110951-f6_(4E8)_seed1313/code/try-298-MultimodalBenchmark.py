import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like self-similarity with recursive oscillations
        fractal = 0.0
        for i in range(self.dim):
            # Log-periodic oscillations with varying frequencies
            freq = 2.0 * (1.0 + 0.5 * np.sin(3.0 * x_norm[i]))
            log_term = np.log(np.abs(x_norm[i]) + 1e-8)
            oscillation = np.sin(freq * x_norm[i] * np.exp(log_term)) * np.cos(freq * x_norm[i] * 0.5 * np.exp(log_term))
            fractal += oscillation
        
        # Logarithmic barrier potentials with adaptive barriers
        barriers = 0.0
        for i in range(self.dim):
            # Barrier potential that increases near boundaries
            barrier_height = 2.0 * np.log(1.0 + np.abs(x_norm[i]))
            barrier_width = 0.5 + 0.3 * np.cos(4.0 * x_norm[i])
            barriers += barrier_height * np.exp(-0.5 * (x_norm[i]**2) / barrier_width**2)
        
        # Spectral harmonic interference with frequency modulation
        spectral = 0.0
        for i in range(self.dim):
            # Modulated harmonic components with varying amplitudes
            amp = 1.0 + 0.4 * np.sin(2.0 * x_norm[i])
            freq_mod = 5.0 + 2.0 * np.cos(3.0 * x_norm[i])
            spectral += amp * np.sin(freq_mod * x_norm[i]) * np.cos(freq_mod * x_norm[i] * 0.7)
        
        # Nested optima with self-similar structure
        nested = 0.0
        for i in range(self.dim):
            # Create nested minima using recursive scaling
            scale_factor = 1.0 / (1.0 + np.exp(-5.0 * x_norm[i]))
            nested += scale_factor * np.sin(10.0 * x_norm[i]) * np.cos(8.0 * x_norm[i])
        
        # Combine all components with dynamic weighting
        result = 0.3 * fractal + 0.4 * barriers + 0.2 * spectral + 0.1 * nested
        
        # Add global scaling based on distance from origin
        r_squared = np.sum(x_norm**2)
        global_scale = 1.0 + 0.3 * np.exp(-0.1 * r_squared) + 0.2 * np.sin(5.0 * r_squared)
        
        return global_scale * result