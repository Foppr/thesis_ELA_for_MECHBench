import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic logarithmic interactions with adaptive scaling
        f2 = 0.9 * np.sum(np.log(1 + 0.5 * np.abs(x_norm)) * np.sin(35 * x_norm))
        
        # Adaptive polynomial scaling with dynamic exponents and cross-dimensional coupling
        f3 = 0.7 * np.sum((x_norm**4) * (1 + 0.7 * np.sin(15 * x_norm**2)) * np.exp(-0.3 * np.abs(x_norm)))
        
        # Dynamic cross-dimensional coupling with exponential decay and sinusoidal modulation
        f4 = 0.6 * np.sum(np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * (x_norm[:-1] + x_norm[1:])**2 * np.sin(10 * (x_norm[:-1] - x_norm[1:])))
        
        # Multi-scale sinusoidal modulation with varying frequencies and amplitude
        f5 = 0.8 * np.sum(np.sin(25 * x_norm) * np.cos(30 * x_norm) * np.exp(-0.7 * x_norm**2) * (1 + 0.3 * np.sin(5 * x_norm)))
        
        # Logarithmic barrier with enhanced chaotic perturbations
        f6 = 0.5 * np.sum(np.log(1 + 0.2 * np.abs(x_norm)) * np.sin(40 * np.pi * x_norm) * np.cos(20 * x_norm))
        
        # Adaptive quartic terms with directional bias and cross-dimensional interaction
        f7 = 0.6 * np.sum((x_norm**5) * (1 + 0.5 * np.cos(20 * x_norm)) * np.exp(-0.4 * np.abs(x_norm)))
        
        # Multi-frequency coupled sine waves with dynamic amplitude modulation and coupling
        f8 = 0.7 * np.sum(np.sin(30 * x_norm) * np.cos(25 * x_norm) * np.exp(-0.6 * x_norm**2) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Hybrid polynomial and trigonometric interactions with enhanced complexity
        f9 = 0.5 * np.sum((x_norm**6) * np.sin(15 * x_norm) * np.cos(12 * x_norm) * (1 + 0.4 * np.sin(8 * x_norm)))
        
        # Cross-dimensional exponential coupling with adaptive weights and chaotic modulation
        f10 = 0.4 * np.sum(np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * x_norm[:-1] * x_norm[1:] * np.sin(20 * x_norm[:-1]) * np.cos(15 * x_norm[1:]))
        
        # Additional chaotic frequency modulation with cross-dimensional coupling and polynomial weighting
        f11 = 0.4 * np.sum(np.sin(45 * x_norm) * np.cos(35 * x_norm) * np.exp(-0.8 * x_norm**2) * (x_norm[:-1]**2 + x_norm[1:]**2) * (1 + 0.2 * np.sin(10 * x_norm)))
        
        # High-order polynomial with chaotic sine modulation and multi-scale interactions
        f12 = 0.3 * np.sum((x_norm**8) * np.sin(20 * x_norm) * np.cos(16 * x_norm) * np.exp(-0.5 * np.abs(x_norm)))
        
        # Combined result
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12
        
        return result