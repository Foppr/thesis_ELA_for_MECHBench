import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sinusoidal interactions with modified seventh-order polynomial frequency modulation
        f2 = 0.7 * np.sum(np.sin(25 * np.pi * x_norm**7 * np.cos(7 * x_norm)))
        
        # Seventh-order polynomial coupling with altered weights
        f3 = 0.25 * np.sum(x_norm**7 * np.sin(4 * np.pi * x_norm))
        
        # Modified quintic penalty with cross-dimensional interactions
        f4 = 0.18 * np.sum((x_norm**5) * (1 + 0.6 * np.sin(12 * x_norm)))
        
        # Enhanced quartic term with directional bias
        f5 = 0.35 * np.sum(x_norm**4 * np.cos(9 * x_norm))
        
        # Additional high-frequency trigonometric component with modified exponential decay
        f6 = 0.18 * np.sum(np.sin(35 * np.pi * x_norm**2) * np.exp(-0.6 * x_norm**2))
        
        # Cross-dimensional coupling with modified exponential decay and cosine modulation
        f7 = 0.15 * np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * x_norm[:-1] * x_norm[1:] * np.cos(4 * x_norm[:-1]))
        
        # Shifted chaotic sine-wave interaction with modified polynomial weighting
        f8 = 0.22 * np.sum(np.sin(20 * np.pi * (x_norm + 0.25)**3) * np.cos(10 * np.pi * x_norm))
        
        # Modified frequency modulation with altered polynomial weights and exponential decay
        f9 = 0.18 * np.sum(x_norm * np.sin(30 * np.pi * x_norm * np.exp(-0.4 * x_norm**2)) * np.cos(5 * x_norm))
        
        # Additional non-linear interaction term with modified seventh-order polynomial
        f10 = 0.18 * np.sum(np.sin(18 * np.pi * x_norm**7) * np.cos(6 * np.pi * x_norm**3))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
        
        return result