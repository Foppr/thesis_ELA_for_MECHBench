import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Enhanced exponential barrier terms with varying decay rates
        f2 = np.sum(np.exp(-3.0 * np.abs(x_norm)) + 0.5 * np.exp(-7.0 * np.abs(x_norm)))
        
        # Multi-frequency sinusoidal modulation with varying amplitudes
        f3 = np.sum(np.sin(8 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) + 
                   0.3 * np.sin(12 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Modified chaotic component with better distribution and convergence properties
        chaotic = 0.0
        for i in range(self.dim):
            if i == 0:
                chaotic += 4 * 0.3 * (1 - 0.3)
            else:
                chaotic += 4 * x_norm[i-1] * (1 - x_norm[i-1]) * (1 - 0.1 * x_norm[i-1])
        f4 = chaotic
        
        # Additional ruggedness term using higher-order polynomial interactions
        f5 = np.sum((x_norm**4 - 2*x_norm**2 + 1) * np.exp(-2.0 * np.abs(x_norm)))
        
        # Combine all terms with optimized weights
        return 0.4 * f1 + 0.3 * f2 + 0.3 * f3 + 0.15 * f4 + 0.1 * f5