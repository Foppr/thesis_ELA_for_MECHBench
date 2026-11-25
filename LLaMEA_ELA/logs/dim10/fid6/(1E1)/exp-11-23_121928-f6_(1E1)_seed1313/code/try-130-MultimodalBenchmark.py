import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sine terms creating many local minima
        f2 = np.sum(np.sin(73 * np.pi * x_norm)**2)
        
        # Cosine product with varying frequencies for complex landscape
        f3 = np.prod(np.cos(np.pi * x_norm * (1 + 1.5 * np.abs(x_norm))))
        
        # Additional polynomial term for shaping the landscape
        f4 = np.sum((x_norm**7) * np.sin(8.1 * np.pi * x_norm))
        
        # Chaotic interaction term using nested trigonometric functions with modified scaling
        f5 = np.sum(np.sin(np.pi * x_norm * np.exp(1.3 * np.abs(x_norm))) * np.cos(5.2 * np.pi * x_norm**2 + 0.41 * np.sin(9.7 * x_norm)))
        
        # New dynamic phase shift term based on dimensionality
        phase_shift = np.sum(np.sin(0.68 * np.pi * x_norm * (1 + 0.52 * self.dim)) * np.cos(1.12 * np.pi * x_norm**3))
        
        # Novel hybrid interaction term combining exponential and logarithmic scaling
        f6 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(np.log(np.abs(x_norm) + 1.25) * (1 + 0.88 * np.sin(self.dim * x_norm))))
        
        # Fractal-like component with recursive sine-cosine interactions
        fractal_term = np.sum(np.sin(np.pi * x_norm * np.sin(3.7 * np.pi * x_norm)) * np.cos(np.pi * x_norm * np.cos(2.5 * np.pi * x_norm)))
        
        # Enhanced adaptive scaling factor based on dimensionality and input magnitude
        scale_factor = 1.0 + 1.3 * np.log(self.dim + 1) + 0.45 * np.mean(np.abs(x_norm))
        
        # Additional chaotic sine-cosine interaction with dynamic frequency modulation
        freq_mod = np.sum(np.sin(3.1 * np.pi * x_norm * (1 + 0.7 * np.sin(0.9 * self.dim))) * np.cos(4.1 * np.pi * x_norm**2))
        
        # New exponential modulation term
        exp_mod = np.sum(np.exp(-0.5 * x_norm**2) * np.sin(2.3 * np.pi * x_norm * (1 + 0.3 * np.cos(self.dim * x_norm))))
        
        # Combined function with multiple competing forces
        return scale_factor * (0.78 * f1 + 0.52 * f2 - 0.45 * f3 + 0.32 * f4 + 0.25 * f5 + 0.17 * phase_shift + 0.12 * f6 + 0.11 * fractal_term + 0.08 * freq_mod + 0.06 * exp_mod) + 0.038 * np.sum(x_norm**8)