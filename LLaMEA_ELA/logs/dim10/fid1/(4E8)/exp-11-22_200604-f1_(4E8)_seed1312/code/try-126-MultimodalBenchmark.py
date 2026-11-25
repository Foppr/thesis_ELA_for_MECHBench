import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Chaotic logarithmic interactions with adaptive scaling
        f2 = 0.6 * np.sum(np.log(1 + np.abs(x_norm)) * np.sin(27 * x_norm))
        
        # Adaptive polynomial scaling with dynamic exponents
        f3 = 0.45 * np.sum((x_norm**3) * (1 + 0.4 * np.sin(11 * x_norm**2)))
        
        # Dynamic cross-dimensional coupling with exponential decay
        f4 = 0.35 * np.sum(np.exp(-0.25 * (x_norm[:-1]**2 + x_norm[1:]**2)) * (x_norm[:-1] + x_norm[1:])**2)
        
        # Multi-scale sinusoidal modulation with varying frequencies
        f5 = 0.55 * np.sum(np.sin(16 * x_norm) * np.cos(22 * x_norm) * np.exp(-0.45 * x_norm**2))
        
        # Logarithmic barrier with chaotic perturbations
        f6 = 0.25 * np.sum(np.log(1 + 0.08 * np.abs(x_norm)) * np.sin(32 * np.pi * x_norm))
        
        # Adaptive quartic terms with directional bias
        f7 = 0.35 * np.sum((x_norm**4) * (1 + 0.25 * np.cos(13 * x_norm)))
        
        # Multi-frequency coupled sine waves with dynamic amplitude modulation
        f8 = 0.45 * np.sum(np.sin(24 * x_norm) * np.cos(19 * x_norm) * np.exp(-0.35 * x_norm**2))
        
        # Hybrid polynomial and trigonometric interactions
        f9 = 0.3 * np.sum((x_norm**5) * np.sin(9 * x_norm) * np.cos(7 * x_norm))
        
        # Cross-dimensional exponential coupling with adaptive weights
        f10 = 0.2 * np.sum(np.exp(-0.15 * (x_norm[:-1]**2 + x_norm[1:]**2)) * x_norm[:-1] * x_norm[1:] * np.sin(15 * x_norm[:-1]))
        
        # Combined result
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
        
        return result