import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sinusoidal interactions with non-linear frequency modulation
        f2 = 0.7 * np.sum(np.sin(25 * np.pi * x_norm * np.cos(6 * x_norm)))
        
        # Seventh-order polynomial coupling with varying weights
        f3 = 0.15 * np.sum(x_norm**7 * np.sin(4 * np.pi * x_norm))
        
        # Modified quintic penalty with cross-dimensional interactions
        f4 = 0.18 * np.sum((x_norm**5) * (1 + 0.6 * np.sin(12 * x_norm)))
        
        # Enhanced quartic term with directional bias
        f5 = 0.25 * np.sum(x_norm**4 * np.cos(9 * x_norm))
        
        # Additional high-frequency trigonometric component with exponential decay
        f6 = 0.12 * np.sum(np.sin(35 * np.pi * x_norm**2) * np.exp(-0.6 * x_norm**2))
        
        # Cross-dimensional coupling with exponential decay and sinusoidal modulation
        f7 = 0.08 * np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * x_norm[:-1] * x_norm[1:] * np.sin(5 * x_norm[:-1]))
        
        # Shifted chaotic sine-wave interaction with polynomial modulation
        f8 = 0.2 * np.sum(np.sin(20 * np.pi * (x_norm + 0.4)**3) * np.cos(10 * np.pi * x_norm))
        
        # Modified frequency modulation with polynomial weights and exponential factor
        f9 = 0.13 * np.sum(x_norm * np.sin(30 * np.pi * x_norm * np.exp(-0.4 * x_norm**2)) * np.cos(3 * x_norm))
        
        # Additional non-linear interaction term with higher frequency
        f10 = 0.11 * np.sum(np.sin(15 * np.pi * x_norm**4) * np.cos(6 * np.pi * x_norm**3))
        
        # Additional complex coupling term
        f11 = 0.09 * np.sum(np.sin(8 * np.pi * x_norm) * np.cos(14 * np.pi * x_norm**2) * (x_norm**3 + x_norm**2))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11
        
        return result