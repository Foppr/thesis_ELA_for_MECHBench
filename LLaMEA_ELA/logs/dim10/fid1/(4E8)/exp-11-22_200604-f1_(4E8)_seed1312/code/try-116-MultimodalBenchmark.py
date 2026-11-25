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
        f3 = 0.22 * np.sum(x_norm**7 * np.sin(5.1 * np.pi * x_norm))
        
        # Modified quintic penalty with cross-dimensional interactions
        f4 = 0.22 * np.sum((x_norm**5) * (1 + 0.75 * np.sin(14.8 * x_norm)))
        
        # Enhanced quartic term with directional bias
        f5 = 0.32 * np.sum(x_norm**4 * np.cos(9.7 * x_norm))
        
        # Additional high-frequency trigonometric component with exponential decay
        f6 = 0.18 * np.sum(np.sin(41 * np.pi * x_norm**2) * np.exp(-0.72 * x_norm**2))
        
        # Cross-dimensional coupling with stronger exponential decay
        f7 = 0.15 * np.sum(np.exp(-0.52 * (x_norm[:-1]**2 + x_norm[1:]**2)) * x_norm[:-1] * x_norm[1:])
        
        # Shifted chaotic sine-wave interaction with modified phase
        f8 = 0.28 * np.sum(np.sin(25 * np.pi * (x_norm + 0.31)**2) * np.cos(12.3 * np.pi * x_norm))
        
        # Modified frequency modulation with polynomial weights (significantly altered)
        f9 = 0.18 * np.sum(x_norm * np.sin(37 * np.pi * x_norm * np.exp(-0.55 * x_norm**2)))
        
        # Additional non-linear interaction term (heavily modified)
        f10 = 0.16 * np.sum(np.sin(18.3 * np.pi * x_norm**3) * np.cos(6.2 * np.pi * x_norm**2))
        
        # Additional cross-dimensional coupling with cubic interactions
        f11 = 0.12 * np.sum((x_norm[:-2]**3 + x_norm[1:-1]**3) * x_norm[2:] * np.sin(8.9 * np.pi * x_norm[:-2]))
        
        # Combined result with adjusted weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11
        
        return result