import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal modulations with varying amplitudes
        f2 = 0.5 * np.sum(np.sin(15 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm))
        
        # Quartic and quintic polynomial penalties for deeper valleys
        f3 = 0.1 * np.sum(x_norm**4)
        f4 = 0.05 * np.sum(x_norm**5)
        
        # Cubic cross-terms with varying interaction strengths
        f5 = 0.1 * np.sum(x_norm[:-1]**3 * x_norm[1:])
        f6 = 0.08 * np.sum(x_norm[:-2]**2 * x_norm[1:-1] * x_norm[2:])
        
        # Chaotic sinusoidal component with random phase shifts
        phases = np.random.rand(self.dim) * 2 * np.pi
        f7 = 0.25 * np.sum(np.sin(12 * np.pi * (x_norm + phases)))
        
        # Multi-scale trigonometric interactions
        f8 = 0.15 * np.sum(np.cos(5 * np.pi * x_norm**3) * np.sin(9 * np.pi * x_norm))
        
        # High-order cross-dimensional interactions
        f9 = 0.04 * np.sum(x_norm[:-3] * x_norm[1:-2] * x_norm[2:-1] * x_norm[3:])
        
        # Shifted and scaled sinusoidal components to create multiple local minima
        f10 = 0.3 * np.sum(np.sin(10 * np.pi * (x_norm + 0.2)) * np.cos(4 * np.pi * (x_norm - 0.1)))
        
        # Combine all components with different weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
        
        return result