import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced recursive sine-wave interactions with exponential decay
        fractal = 0.0
        for i in range(self.dim):
            amp = 1.0
            for j in range(1, min(5, self.dim - i + 1)):
                amp *= 0.6
                fractal += amp * np.sin(2 ** j * x[i]) * np.cos(2 ** (j+1) * x[i])
        
        # Adaptive basin structure with variable scaling and phase shifts
        basins = 0.0
        scales = [0.5, 1.0, 2.0, 4.0]
        for scale in scales:
            for i in range(self.dim):
                phase = np.sin(i * np.pi / 4)
                basins += np.exp(-0.5 * ((x[i] - phase) / scale) ** 2) * np.sin(scale * x[i])
        
        # Modified logarithmic barrier penalties with dynamic severity
        barriers = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                severity = 1.0 + 0.5 * np.sin(i)
                barriers += severity * np.log(np.abs(x[i]) - 3.9) * np.exp(-0.05 * (x[i] ** 2))
        
        # Multi-scale Gaussian peaks with adaptive variance and frequency modulation
        peaks = 0.0
        for i in range(self.dim):
            freq = 2 + np.sin(i)
            sigma = 0.3 + 0.7 * np.cos(i)
            peaks += np.exp(-0.5 * ((x[i] - np.sin(i)) / sigma) ** 2) * np.cos(freq * x[i])
        
        # Combined fitness with optimized weights and normalization
        return 0.35 * fractal + 0.3 * basins + 0.25 * barriers + 0.1 * peaks