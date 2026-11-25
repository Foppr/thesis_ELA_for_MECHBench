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
        f2 = 1.2 * np.sum(np.sin(40 * np.pi * x_norm * np.cos(9 * x_norm)))
        
        # Eighth-order polynomial coupling with varying weights
        f3 = 0.3 * np.sum(x_norm**8 * np.sin(6 * np.pi * x_norm))
        
        # Modified quintic penalty with cross-dimensional interactions
        f4 = 0.3 * np.sum((x_norm**5) * (1 + 0.8 * np.sin(20 * x_norm)))
        
        # Enhanced quartic term with directional bias and additional chaos
        f5 = 0.4 * np.sum(x_norm**4 * np.cos(12 * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Additional high-frequency trigonometric component with exponential decay
        f6 = 0.2 * np.sum(np.sin(50 * np.pi * x_norm**2) * np.exp(-0.8 * x_norm**2))
        
        # Cross-dimensional coupling with enhanced exponential decay and sine modulation
        f7 = 0.18 * np.sum(np.exp(-0.6 * (x_norm[:-1]**2 + x_norm[1:]**2)) * x_norm[:-1] * x_norm[1:] * np.sin(10 * x_norm[:-1]))
        
        # Shifted chaotic sine-wave interaction with modified frequency and amplitude
        f8 = 0.35 * np.sum(np.sin(30 * np.pi * (x_norm + 0.4)**2) * np.cos(15 * np.pi * x_norm) * np.exp(-0.2 * x_norm**2))
        
        # Modified frequency modulation with polynomial weights, additional chaos and exponential decay
        f9 = 0.2 * np.sum(x_norm * np.sin(40 * np.pi * x_norm * np.exp(-0.6 * x_norm**2)) * np.cos(10 * x_norm) * np.sin(5 * x_norm))
        
        # Additional non-linear interaction term with higher frequency and multi-modulation
        f10 = 0.2 * np.sum(np.sin(25 * np.pi * x_norm**3) * np.cos(8 * np.pi * x_norm**2) * np.exp(-0.4 * x_norm**2))
        
        # Additional coupled sine-wave component for increased complexity with cubic modulation
        f11 = 0.15 * np.sum(np.sin(22 * np.pi * x_norm) * np.sin(26 * np.pi * x_norm) * np.exp(-0.4 * x_norm**2) * x_norm**3)
        
        # Additional multi-scale chaotic component with multiple sine-wave interactions
        f12 = 0.25 * np.sum(np.sin(35 * np.pi * np.sin(7 * x_norm)) * np.cos(18 * np.pi * np.cos(5 * x_norm)))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12
        
        return result