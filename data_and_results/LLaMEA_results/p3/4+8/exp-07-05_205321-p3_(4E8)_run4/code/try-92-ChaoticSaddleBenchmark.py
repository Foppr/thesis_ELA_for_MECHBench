import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like radial component with chaotic scaling
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sin(10 * r) * np.exp(-r**2) + 0.5 * np.sin(30 * r) * np.exp(-0.5 * r**2)
        
        # Nested oscillatory terms with varying frequencies and amplitudes
        nested = 0.0
        for i in range(self.dim):
            freq = (i + 1) * 2.0
            amp = 1.0 / (i + 1)
            nested += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Non-separable cross-terms creating a complex interaction landscape
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(3 * x_norm[i] + 2 * x_norm[j]) * np.cos(2 * x_norm[i] - x_norm[j])
        
        # Saddle-point structure with multiple local minima and maxima
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i]**2 - 1.0)**2 * np.sin(5 * x_norm[i])
        
        # Combine all components
        return 0.3 * radial + 0.4 * nested + 0.2 * cross + 0.1 * saddle