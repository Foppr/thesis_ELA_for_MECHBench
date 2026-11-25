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
        f2 = 0.7 * np.sum(np.sin(27 * np.pi * x_norm * np.cos(6.5 * x_norm)))
        
        # Fifth-order polynomial coupling with varying weights
        f3 = 0.16 * np.sum(x_norm**5 * np.sin(4.2 * np.pi * x_norm))
        
        # Modified quartic penalty with cross-dimensional interactions
        f4 = 0.16 * np.sum((x_norm**4) * (1 + 0.65 * np.sin(12.5 * x_norm)))
        
        # Enhanced cubic term with directional bias
        f5 = 0.26 * np.sum(x_norm**3 * np.cos(8.2 * x_norm))
        
        # Additional high-frequency trigonometric component
        f6 = 0.11 * np.sum(np.sin(37 * np.pi * x_norm**2) * np.exp(-0.62 * x_norm**2))
        
        # Cross-dimensional coupling with exponential decay
        f7 = 0.09 * np.sum(np.exp(-0.42 * (x_norm[:-1]**2 + x_norm[1:]**2)) * x_norm[:-1] * x_norm[1:])
        
        # Shifted chaotic sine-wave interaction
        f8 = 0.21 * np.sum(np.sin(21 * np.pi * (x_norm + 0.27)**2) * np.cos(10.5 * np.pi * x_norm))
        
        # Modified frequency modulation with polynomial weights (slightly altered)
        f9 = 0.13 * np.sum(x_norm * np.sin(31 * np.pi * x_norm * np.exp(-0.45 * x_norm**2)))
        
        # Additional non-linear interaction term (slightly modified)
        f10 = 0.11 * np.sum(np.sin(15.5 * np.pi * x_norm**3) * np.cos(5.0 * np.pi * x_norm**2))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
        
        return result