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
        
        # Fifth-order polynomial coupling with varying weights
        f3 = 0.15 * np.sum(x_norm**5 * np.sin(4 * np.pi * x_norm))
        
        # Modified quartic penalty with cross-dimensional interactions
        f4 = 0.15 * np.sum((x_norm**4) * (1 + 0.6 * np.sin(12 * x_norm)))
        
        # Enhanced cubic term with directional bias
        f5 = 0.25 * np.sum(x_norm**3 * np.cos(8 * x_norm))
        
        # Additional high-frequency trigonometric component
        f6 = 0.1 * np.sum(np.sin(35 * np.pi * x_norm**2) * np.exp(-0.6 * x_norm**2))
        
        # Cross-dimensional coupling with exponential decay (slightly modified)
        f7 = 0.08 * np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * x_norm[:-1] * x_norm[1:])
        
        # Shifted chaotic sine-wave interaction (modified shift)
        f8 = 0.2 * np.sum(np.sin(20 * np.pi * (x_norm + 0.3)**2) * np.cos(10 * np.pi * x_norm))
        
        # Modified frequency modulation with polynomial weights (slightly altered)
        f9 = 0.12 * np.sum(x_norm * np.sin(30 * np.pi * x_norm * np.exp(-0.35 * x_norm**2)))
        
        # Additional non-linear interaction term (modified exponent)
        f10 = 0.1 * np.sum(np.sin(15 * np.pi * x_norm**3) * np.cos(5 * np.pi * x_norm**2.5))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
        
        return result