import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees
        f1 = np.sum(x_norm**6)
        
        # Trigonometric terms with multiple frequencies and phase shifts
        f2 = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) + 
                   np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Exponential interaction with logarithmic scaling
        f3 = np.sum(np.exp(-np.abs(x_norm)) * np.log(np.abs(x_norm) + 1.2))
        
        # Adaptive weighting based on dimensionality and input magnitude
        weight_factor = 1.0 + 0.5 * np.sin(self.dim * np.pi * x_norm)
        
        # Dynamic phase modulation with chaotic behavior
        f4 = np.sum(np.sin(weight_factor * x_norm**2 + 0.3 * np.sin(1.7 * x_norm)) * 
                   np.cos(0.8 * x_norm + 0.5 * np.cos(2.3 * x_norm)))
        
        # Cross-term interactions with dynamic scaling
        f5 = np.sum(x_norm * np.sin(np.pi * x_norm**3) * np.cos(0.5 * np.pi * x_norm**2))
        
        # Multi-scale harmonic components
        f6 = np.sum(np.sin(11 * np.pi * x_norm) + np.cos(13 * np.pi * x_norm) + 
                   np.sin(17 * np.pi * x_norm) * np.cos(19 * np.pi * x_norm))
        
        # Dimensionality-dependent adjustment
        dim_adjust = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combine all components with adaptive coefficients
        result = (0.4 * f1 + 0.3 * f2 - 0.2 * f3 + 0.15 * f4 + 0.05 * f5 + 0.1 * f6) * dim_adjust
        
        # Add small perturbation for additional complexity
        result += 0.01 * np.sum(np.sin(20 * x_norm) * np.cos(25 * x_norm))
        
        return result