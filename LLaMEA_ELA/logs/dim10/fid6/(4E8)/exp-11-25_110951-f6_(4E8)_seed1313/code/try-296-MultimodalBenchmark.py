import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic gradient flows with exponential potentials
        chaotic_flow = 0.0
        for i in range(self.dim):
            # Exponential potential with chaotic modulation
            exp_potential = np.exp(-0.5 * (x_norm[i]**2)) * (1.0 + 0.3 * np.sin(10 * x_norm[i]))
            # Chaotic coupling term
            chaotic_term = 0.5 * np.sin(3 * x_norm[i] + np.cos(7 * x_norm[i]))
            chaotic_flow += exp_potential * chaotic_term
        
        # Logarithmic barrier potentials with adaptive scaling
        barrier_potential = 0.0
        for i in range(self.dim):
            # Logarithmic barrier that becomes steeper near boundaries
            log_barrier = -np.log(1.0 + np.exp(-5.0 * (x_norm[i] - 1.0))) - np.log(1.0 + np.exp(-5.0 * (-x_norm[i] - 1.0)))
            # Adaptive scaling based on dimensionality
            adaptive_scale = 1.0 + 0.2 * np.sin(self.dim * x_norm[i])
            barrier_potential += adaptive_scale * log_barrier
        
        # Spectral harmonic interference with phase modulation
        spectral_harmonic = 0.0
        for i in range(self.dim):
            # Multiple frequency components with varying amplitudes
            freq1 = 8.0 + 2.0 * np.sin(3 * x_norm[i])
            freq2 = 6.0 + 1.5 * np.cos(4 * x_norm[i])
            amplitude1 = 1.0 + 0.4 * np.cos(5 * x_norm[i])
            amplitude2 = 0.8 + 0.3 * np.sin(6 * x_norm[i])
            # Phase modulation based on other dimensions
            phase_mod = np.sum(np.sin(x_norm[:i]) if i > 0 else [0])
            spectral_harmonic += (amplitude1 * np.sin(freq1 * x_norm[i] + phase_mod) + 
                                amplitude2 * np.cos(freq2 * x_norm[i] + phase_mod))
        
        # Dynamic attractor regions with fractal-like self-similarity
        attractor_regions = 0.0
        for i in range(self.dim):
            # Create nested attraction basins with fractal characteristics
            basin_depth = (x_norm[i]**2) * (1.0 + 0.5 * np.sin(15 * x_norm[i]))
            # Add fractal-like perturbation
            fractal_perturb = 0.3 * np.sin(30 * x_norm[i]) * np.cos(15 * x_norm[i])
            attractor_regions += basin_depth + fractal_perturb
        
        # Combine all components with dynamic weights based on position
        r_squared = np.sum(x_norm**2)
        weight1 = 1.0 + 0.3 * np.sin(r_squared)
        weight2 = 1.0 + 0.2 * np.cos(r_squared)
        weight3 = 1.0 + 0.4 * np.tan(0.5 * r_squared)
        
        result = weight1 * chaotic_flow + weight2 * barrier_potential + weight3 * spectral_harmonic + attractor_regions
        
        # Add global scaling and non-uniform curvature effects
        global_scale = 1.0 + 0.8 * np.exp(-0.3 * r_squared) * np.sin(2 * r_squared)
        
        return global_scale * result