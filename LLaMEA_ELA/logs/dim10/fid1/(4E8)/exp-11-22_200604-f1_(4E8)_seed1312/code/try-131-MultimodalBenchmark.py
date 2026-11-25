import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic logarithmic interactions with modified scaling
        f2 = 0.7 * np.sum(np.log(1 + 0.5 * np.abs(x_norm)) * np.sin(31 * x_norm))
        
        # Adaptive polynomial scaling with enhanced dynamic exponents
        f3 = 0.5 * np.sum((x_norm**3) * (1 + 0.5 * np.sin(13 * x_norm**2)))
        
        # Improved cross-dimensional coupling with stronger exponential decay
        f4 = 0.4 * np.sum(np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * (x_norm[:-1] + x_norm[1:])**2)
        
        # Refined multi-scale sinusoidal modulation with adjusted frequencies
        f5 = 0.6 * np.sum(np.sin(18 * x_norm) * np.cos(24 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Enhanced logarithmic barrier with stronger chaotic perturbations
        f6 = 0.3 * np.sum(np.log(1 + 0.1 * np.abs(x_norm)) * np.sin(35 * np.pi * x_norm))
        
        # Refined quartic terms with increased directional bias
        f7 = 0.4 * np.sum((x_norm**4) * (1 + 0.3 * np.cos(15 * x_norm)))
        
        # Improved multi-frequency coupled sine waves with enhanced amplitude modulation
        f8 = 0.5 * np.sum(np.sin(26 * x_norm) * np.cos(21 * x_norm) * np.exp(-0.4 * x_norm**2))
        
        # Modified hybrid polynomial and trigonometric interactions
        f9 = 0.35 * np.sum((x_norm**5) * np.sin(10 * x_norm) * np.cos(8 * x_norm))
        
        # Enhanced cross-dimensional exponential coupling with adaptive weights
        f10 = 0.25 * np.sum(np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)) * x_norm[:-1] * x_norm[1:] * np.sin(17 * x_norm[:-1]))
        
        # Additional chaotic resonance terms for increased complexity
        f11 = 0.15 * np.sum(np.sin(40 * x_norm) * np.cos(30 * x_norm) * np.exp(-0.25 * x_norm**2))
        
        # Combined result
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11
        
        return result