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
        f2 = 0.8 * np.sum(np.log(1 + np.abs(x_norm)) * np.sin(30 * x_norm))
        
        # Adaptive polynomial scaling with dynamic exponents
        f3 = 0.6 * np.sum((x_norm**4) * (1 + 0.6 * np.sin(12 * x_norm**2)))
        
        # Dynamic cross-dimensional coupling with exponential decay
        f4 = 0.5 * np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * (x_norm[:-1] + x_norm[1:])**2)
        
        # Multi-scale sinusoidal modulation with varying frequencies
        f5 = 0.7 * np.sum(np.sin(20 * x_norm) * np.cos(25 * x_norm) * np.exp(-0.6 * x_norm**2))
        
        # Logarithmic barrier with chaotic perturbations
        f6 = 0.4 * np.sum(np.log(1 + 0.15 * np.abs(x_norm)) * np.sin(35 * np.pi * x_norm))
        
        # Adaptive quartic terms with directional bias
        f7 = 0.5 * np.sum((x_norm**5) * (1 + 0.4 * np.cos(15 * x_norm)))
        
        # Multi-frequency coupled sine waves with dynamic amplitude modulation
        f8 = 0.6 * np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Hybrid polynomial and trigonometric interactions
        f9 = 0.4 * np.sum((x_norm**6) * np.sin(10 * x_norm) * np.cos(8 * x_norm))
        
        # Cross-dimensional exponential coupling with adaptive weights
        f10 = 0.3 * np.sum(np.exp(-0.25 * (x_norm[:-1]**2 + x_norm[1:]**2)) * x_norm[:-1] * x_norm[1:] * np.sin(16 * x_norm[:-1]))
        
        # Additional chaotic frequency modulation with cross-dimensional coupling
        f11 = 0.35 * np.sum(np.sin(40 * x_norm) * np.cos(30 * x_norm) * np.exp(-0.7 * x_norm**2) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # High-order polynomial with chaotic sine modulation
        f12 = 0.25 * np.sum((x_norm**7) * np.sin(18 * x_norm) * np.cos(14 * x_norm))
        
        # Combined result
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12
        
        return result