import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        term1 = np.sum(x_norm**2)
        
        # Chaotic sine-wave interference with varying amplitudes and frequencies
        term2 = 0.4 * np.sum(np.sin(25 * x_norm) * np.cos(17 * x_norm) * np.exp(-0.3 * np.abs(x_norm)))
        
        # Polynomial modulation with trigonometric coupling
        term3 = 0.25 * np.sum((x_norm**7) * np.sin(9 * np.pi * x_norm))
        
        # Cross-dimensional exponential decay with sine coupling
        term4 = 0.3 * np.sum(np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * np.sin(8 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Nested chaotic component with gradient bias reduction
        term5 = 0.2 * np.sum(np.sin(30 * x_norm) * np.cos(22 * x_norm) * np.exp(-0.1 * x_norm**2))
        
        # Additional sinusoidal modulation with peak sharpening
        term6 = 0.15 * np.sum(np.sin(12 * np.pi * x_norm) * np.cos(14 * np.pi * x_norm) * (1 + 0.2 * np.sin(5 * x_norm)))
        
        # Combine all terms
        result = term1 + term2 + term3 + term4 + term5 + term6
        
        return result