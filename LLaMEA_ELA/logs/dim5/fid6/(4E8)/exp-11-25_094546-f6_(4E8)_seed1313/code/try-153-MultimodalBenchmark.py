import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic saddle-point component with embedded Gaussian mixtures
        saddle = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Saddle point with chaotic modulation
            saddle += (xi**2 - 1.0)**2 * np.sin(10.0 * xi) + 0.5 * np.exp(-5.0 * (xi - 0.3)**2)
            
        # Embedded Gaussian mixture components with dynamic weights
        gaussian = 0.0
        centers = np.linspace(-0.8, 0.8, 5)
        for i, center in enumerate(centers):
            weight = 0.2 + 0.1 * np.sin(i * 0.5)
            gaussian += weight * np.exp(-0.5 * (x_norm - center)**2 / 0.1**2)
            
        # Multi-scale harmonic interactions with phase modulation
        harmonic = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            freqs = [2.0, 4.0, 8.0, 16.0]
            for j, freq in enumerate(freqs):
                phase = np.sin(0.5 * (i + j) * np.pi / self.dim)
                harmonic += np.sin(freq * xi + phase) * np.cos(freq * xi * 0.7)
                
        # Dynamic coupling with time-delayed feedback
        coupling = 0.0
        for i in range(self.dim):
            if i > 2:
                delay = x_norm[i-1] - 0.5 * x_norm[i-2] + 0.3 * x_norm[i-3]
                coupling += np.sin(8.0 * delay) * np.exp(-0.5 * delay**2)
            else:
                coupling += np.cos(6.0 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
                
        # Adaptive roughness with fractal-like scaling
        roughness = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            roughness += np.sin(3.0 * xi) * np.cos(7.0 * xi) * (1.0 + 0.3 * np.sin(5.0 * xi))
            
        # Combined landscape with dynamic scaling factor
        total = saddle + 0.8 * gaussian + 0.6 * harmonic + 0.4 * coupling + 0.7 * roughness
        
        # Dynamic scaling based on dimensionality
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.3)
        
        return scale_factor * total