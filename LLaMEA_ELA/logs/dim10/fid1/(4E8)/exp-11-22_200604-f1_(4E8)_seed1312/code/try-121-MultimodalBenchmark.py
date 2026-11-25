import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Fractal-like Gaussian process with recursive scaling
        f2 = 0.8 * np.sum(np.exp(-5.0 * np.abs(x_norm)) * np.sin(10 * x_norm) * np.cos(7 * x_norm))
        
        # Adaptive noise injection with exponential decay
        noise = np.random.normal(0, 0.1, self.dim)
        f3 = 0.6 * np.sum((x_norm + noise)**2 * np.exp(-0.5 * (x_norm + noise)**2))
        
        # Directional momentum terms with periodic modulation
        f4 = 0.5 * np.sum(np.sin(12 * x_norm) * np.cos(9 * x_norm) * (x_norm**3))
        
        # Recursive cross-dimensional interactions with fractal scaling
        f5 = 0.4 * np.sum(np.exp(-0.1 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                          np.sin(15 * (x_norm[:-1] + x_norm[1:])) * 
                          np.cos(8 * (x_norm[:-1] - x_norm[1:])))
        
        # Multi-scale sinusoidal with dynamic frequency modulation
        f6 = 0.7 * np.sum(np.sin(20 * x_norm) * np.cos(13 * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Adaptive quartic coupling with chaotic perturbations
        f7 = 0.55 * np.sum((x_norm**4) * (1 + 0.2 * np.sin(25 * x_norm)) * np.cos(6 * x_norm))
        
        # Momentum-based directional bias with exponential weighting
        f8 = 0.3 * np.sum(np.exp(-0.2 * np.abs(x_norm)) * np.sin(18 * x_norm) * (x_norm**2))
        
        # Combined result
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
        
        return result