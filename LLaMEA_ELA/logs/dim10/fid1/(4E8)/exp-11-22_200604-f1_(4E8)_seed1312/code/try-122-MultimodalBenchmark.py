import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic logarithmic interactions with higher frequency modulations
        f2 = 1.2 * np.sum(np.log(1 + 0.5 * np.abs(x_norm)) * np.sin(35 * x_norm))
        
        # Adaptive polynomial scaling with dynamic exponents and multi-frequency components
        f3 = 0.8 * np.sum((x_norm**4) * (1 + 0.7 * np.sin(15 * x_norm**2) + 0.3 * np.cos(10 * x_norm)))
        
        # Dynamic cross-dimensional coupling with multiple exponential decay rates
        f4 = 0.6 * np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * (x_norm[:-1] + x_norm[1:])**2 * 
                         (1 + 0.2 * np.sin(5 * x_norm[:-1])))
        
        # Multi-scale sinusoidal modulation with varying frequencies and amplitude variations
        f5 = 0.9 * np.sum(np.sin(20 * x_norm) * np.cos(25 * x_norm) * np.exp(-0.6 * x_norm**2) * 
                         (1 + 0.3 * np.sin(8 * x_norm)))
        
        # Enhanced logarithmic barrier with chaotic perturbations and multiple scales
        f6 = 0.5 * np.sum(np.log(1 + 0.2 * np.abs(x_norm)) * np.sin(40 * np.pi * x_norm) * 
                         (1 + 0.1 * np.cos(15 * x_norm)))
        
        # Adaptive quartic terms with directional bias and multi-scale modulation
        f7 = 0.6 * np.sum((x_norm**5) * (1 + 0.4 * np.cos(15 * x_norm)) * 
                         (1 + 0.2 * np.sin(12 * x_norm**2)))
        
        # Multi-frequency coupled sine waves with dynamic amplitude modulation and phase shifts
        f8 = 0.7 * np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * np.exp(-0.5 * x_norm**2) * 
                         (1 + 0.25 * np.sin(7 * x_norm)))
        
        # Hybrid polynomial and trigonometric interactions with higher order terms
        f9 = 0.5 * np.sum((x_norm**6) * np.sin(10 * x_norm) * np.cos(8 * x_norm) * 
                         (1 + 0.2 * np.cos(5 * x_norm)))
        
        # Cross-dimensional exponential coupling with adaptive weights and chaotic modulation
        f10 = 0.4 * np.sum(np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * x_norm[:-1] * x_norm[1:] * 
                          np.sin(18 * x_norm[:-1]) * (1 + 0.3 * np.sin(9 * x_norm[:-1])))
        
        # Additional chaotic saddle point terms
        f11 = 0.3 * np.sum(np.sin(50 * x_norm) * np.cos(40 * x_norm) * 
                          (x_norm**2 + 0.1 * np.abs(x_norm)))
        
        # Combined result
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11
        
        return result