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
        f2 = 0.8 * np.sum(np.sin(31 * np.pi * x_norm * np.cos(7.2 * x_norm)))
        
        # Seventh-order polynomial coupling with varying weights
        f3 = 0.21 * np.sum(x_norm**7 * np.sin(5.1 * np.pi * x_norm))
        
        # Modified quartic penalty with cross-dimensional interactions
        f4 = 0.22 * np.sum((x_norm**4) * (1 + 0.72 * np.sin(14.3 * x_norm)))
        
        # Enhanced cubic term with directional bias
        f5 = 0.31 * np.sum(x_norm**3 * np.cos(9.8 * x_norm))
        
        # Additional high-frequency trigonometric component
        f6 = 0.15 * np.sum(np.sin(41 * np.pi * x_norm**2) * np.exp(-0.71 * x_norm**2))
        
        # Cross-dimensional coupling with exponential decay
        f7 = 0.13 * np.sum(np.exp(-0.51 * (x_norm[:-1]**2 + x_norm[1:]**2)) * x_norm[:-1] * x_norm[1:])
        
        # Shifted chaotic sine-wave interaction
        f8 = 0.25 * np.sum(np.sin(25 * np.pi * (x_norm + 0.31)**2) * np.cos(12.1 * np.pi * x_norm))
        
        # Modified frequency modulation with polynomial weights (slightly altered)
        f9 = 0.17 * np.sum(x_norm * np.sin(35 * np.pi * x_norm * np.exp(-0.52 * x_norm**2)))
        
        # Additional non-linear interaction term (slightly modified)
        f10 = 0.14 * np.sum(np.sin(18.7 * np.pi * x_norm**3) * np.cos(6.3 * np.pi * x_norm**2))
        
        # Additional chaotic component with logarithmic scaling
        f11 = 0.19 * np.sum(np.log(np.abs(x_norm) + 1.1) * np.sin(23 * np.pi * x_norm))
        
        # Increased cross-dimensional coupling strength
        f12 = 0.16 * np.sum(np.exp(-0.38 * (x_norm[:-1]**2 + x_norm[1:]**2)) * (x_norm[:-1]**2) * (x_norm[1:]**2))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12
        
        return result