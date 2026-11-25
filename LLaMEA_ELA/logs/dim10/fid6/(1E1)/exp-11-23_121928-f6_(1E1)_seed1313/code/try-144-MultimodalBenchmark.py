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
        f2 = np.sum(np.sin(67 * np.pi * x_norm)**2)
        
        # Cosine product with varying frequencies for complex landscape
        f3 = np.prod(np.cos(np.pi * x_norm * (1 + 1.7 * np.abs(x_norm))))
        
        # Additional polynomial term for shaping the landscape
        f4 = np.sum((x_norm**5) * np.sin(7.8 * np.pi * x_norm))
        
        # Chaotic interaction term using nested trigonometric functions with modified scaling
        f5 = np.sum(np.sin(np.pi * x_norm * np.exp(1.4 * np.abs(x_norm))) * np.cos(5.2 * np.pi * x_norm**2 + 0.4 * np.sin(9.7 * x_norm)))
        
        # New dynamic phase shift term based on dimensionality
        phase_shift = np.sum(np.sin(0.68 * np.pi * x_norm * (1 + 0.5 * self.dim)) * np.cos(1.1 * np.pi * x_norm**3))
        
        # Novel hybrid interaction term combining exponential and logarithmic scaling
        f6 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(np.log(np.abs(x_norm) + 1.3) * (1 + 0.85 * np.sin(self.dim * x_norm))))
        
        # Fractal-like component with recursive sine-cosine interactions
        fractal_term = np.sum(np.sin(np.pi * x_norm * np.sin(3.7 * np.pi * x_norm)) * np.cos(np.pi * x_norm * np.cos(2.7 * np.pi * x_norm)))
        
        # New logarithmic fractal component for increased complexity
        log_fractal = np.sum(np.log(np.abs(x_norm) + 0.6) * np.sin(2.8 * np.pi * x_norm * np.cos(1.9 * np.pi * x_norm)))
        
        # Enhanced adaptive scaling factor based on dimensionality and input magnitude
        scale_factor = 1.0 + 1.3 * np.log(self.dim + 1) + 0.42 * np.mean(np.abs(x_norm))
        
        # Additional chaotic sine-cosine interaction with dynamic frequency modulation
        freq_mod = np.sum(np.sin(3.1 * np.pi * x_norm * (1 + 0.7 * np.sin(0.9 * self.dim))) * np.cos(4.1 * np.pi * x_norm**2))
        
        # Combined function with multiple competing forces
        return scale_factor * (0.75 * f1 + 0.48 * f2 - 0.41 * f3 + 0.27 * f4 + 0.19 * f5 + 0.09 * phase_shift + 0.07 * f6 + 0.05 * fractal_term + 0.04 * log_fractal + 0.03 * freq_mod) + 0.035 * np.sum(x_norm**6)