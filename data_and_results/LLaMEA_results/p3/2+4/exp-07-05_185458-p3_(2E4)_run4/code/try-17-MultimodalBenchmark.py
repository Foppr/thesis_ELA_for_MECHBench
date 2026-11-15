import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base for conditioning
        f1 = np.sum(x_norm**2)
        
        # Radial periodic terms with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            dist = np.sqrt(np.sum((x_norm - np.roll(x_norm, i))**2))
            f2 += np.sin(10 * dist + i) * np.exp(-0.5 * dist**2)
        
        # Coupled sine waves with adaptive frequency based on dimensionality
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f3 += np.sin((i+1) * (j+1) * x_norm[i] * x_norm[j]) * np.exp(-0.1 * (i-j)**2)
        
        # Polynomial interaction terms with chaotic modulation
        f4 = np.sum((x_norm**3 + 0.5 * x_norm**5) * np.sin(np.pi * x_norm))
        
        # Adaptive difficulty scaling with dimensionality
        scale = 1.0 + 0.1 * self.dim
        
        # Combine all components
        return scale * (f1 + 0.5 * f2 + 0.3 * f3 + 0.1 * f4)