import numpy as np

class FractalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Fractal-like self-similarity using recursive sine-cosine combinations
        f2 = 0.5 * np.sum(np.sin(10 * np.sin(5 * x_norm)) * np.cos(8 * np.cos(3 * x_norm)))
        
        # Multi-scale oscillatory component with varying frequencies and amplitudes
        scales = np.arange(1, self.dim + 1)
        f3 = 0.4 * np.sum(np.sin(scales * x_norm) * np.cos(scales * x_norm**2))
        
        # Discontinuous gradient field with step-like transitions
        step_field = np.zeros_like(x_norm)
        for i in range(self.dim):
            step_field[i] = np.floor(5 * np.sin(x_norm[i])) + 0.5 * np.sin(10 * x_norm[i])
        f4 = 0.3 * np.sum(step_field**2)
        
        # Multi-modal attraction basins with varying depths and widths
        basin_depths = 1 + 0.5 * np.sin(2 * x_norm)
        basin_widths = 0.5 + 0.3 * np.cos(3 * x_norm)
        f5 = 0.6 * np.sum(basin_depths * np.exp(-0.5 * ((x_norm - 0.3) / basin_widths)**2))
        
        # Rugged terrain with sharp peaks and valleys using chaotic modulation
        chaos_mod = np.sin(15 * x_norm + np.sin(7 * x_norm))
        f6 = 0.4 * np.sum(np.abs(x_norm)**1.5 * chaos_mod)
        
        # Self-similar pattern at multiple scales using recursive fractal mapping
        fractal_pattern = 0.3 * np.sum(np.sin(20 * x_norm) * np.cos(12 * x_norm) * 
                                      np.exp(-0.2 * np.abs(x_norm)))
        f7 = fractal_pattern
        
        # Asymmetric penalty landscapes with dynamic scaling
        asym_penalty = np.sum(np.abs(x_norm)**2.2 * np.sin(9 * x_norm) * 
                             np.exp(-0.15 * x_norm**2))
        f8 = 0.35 * asym_penalty
        
        # Combined result with chaotic modulation and multi-scale interaction
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
        
        return result