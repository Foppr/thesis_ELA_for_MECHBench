import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different coefficients
        f1 = np.sum(x_norm**2)
        
        # Add multiple local minima using chaotic sinusoidal terms with varying frequencies
        f2 = 0.5 * np.sum(np.sin(15 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Add a quartic penalty term to create deeper valleys
        f3 = 0.08 * np.sum(x_norm**4)
        
        # Add an additional cubic term to increase complexity
        f4 = 0.15 * np.sum(x_norm**3)
        
        # Add a secondary trigonometric component with different frequency and amplitude
        f5 = 0.25 * np.sum(np.cos(10 * np.pi * x_norm**2))
        
        # Add a cross-term interaction to increase dimensionality complexity
        f6 = 0.06 * np.sum(x_norm[:-1] * x_norm[1:] * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Add a shifted sinusoidal component to create more challenging optima
        f7 = 0.08 * np.sum(np.sin(6 * np.pi * (x_norm + 0.2)**3))
        
        # Add a fifth-order polynomial term for increased complexity
        f8 = 0.04 * np.sum(x_norm**5)
        
        # Add a chaotic sine-wave interaction term with non-linear modulation
        f9 = 0.12 * np.sum(np.sin(20 * np.pi * x_norm * np.exp(-0.5 * x_norm**2)))
        
        # Add a high-frequency sinusoidal component to increase landscape roughness
        f10 = 0.03 * np.sum(np.sin(25 * np.pi * x_norm**2))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
        
        return result