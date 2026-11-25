import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal sine-wave interactions with recursive structure
        fractal = 0.0
        for i in range(self.dim):
            # Recursive sine pattern with diminishing amplitude
            amp = 1.0
            for j in range(1, min(6, self.dim - i + 1)):
                amp *= 0.7
                fractal += amp * np.sin(2 ** j * x[i]) * np.cos(2 ** j * x[i])
        
        # Self-similar basin structure with multiple nested minima
        basins = 0.0
        scales = [1.0, 2.0, 4.0]
        for scale in scales:
            for i in range(self.dim):
                basins += np.exp(-0.5 * ((x[i] / scale) ** 2)) * np.sin(scale * x[i])
        
        # Logarithmic barrier penalties with varying severity
        barriers = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                barriers += np.log(np.abs(x[i]) - 3.0) * np.exp(-0.1 * (x[i] ** 2))
        
        # Multi-scale Gaussian peaks with fractal variance
        peaks = 0.0
        for i in range(self.dim):
            sigma = 0.5 + 0.5 * np.sin(i)
            peaks += np.exp(-0.5 * ((x[i] - np.sin(i)) / sigma) ** 2) * np.cos(3 * x[i])
        
        # Combined fitness with adaptive weights
        return 0.4 * fractal + 0.3 * basins + 0.2 * barriers + 0.1 * peaks