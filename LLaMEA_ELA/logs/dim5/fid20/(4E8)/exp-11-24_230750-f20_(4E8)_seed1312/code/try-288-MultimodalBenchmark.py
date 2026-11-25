import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component for irregular oscillations
        tent = 0.0
        a = 1.5
        for i in range(self.dim):
            xi = x[i]
            if xi < 0.5:
                tent += a * xi
            else:
                tent += a * (1 - xi)
        
        # Adaptive spiral structure with rotational symmetry
        spiral = 0.0
        for i in range(self.dim):
            r = np.sqrt(x[i]**2 + x[(i+1) % self.dim]**2)
            theta = np.arctan2(x[(i+1) % self.dim], x[i])
            spiral += r * np.sin(3 * theta + 0.5 * x[i]) * np.cos(2 * theta)
        
        # Dynamic polynomial-vortex interactions
        vortex = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                vortex += (x[i]**2 + x[j]**2) * np.sin(2 * np.pi * dist)
        
        # Multi-scale Gaussian peaks with time-varying centers
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for k in range(4):
                center = -4.0 + 2.0 * k
                variance = 1.0 + 0.3 * np.sin(0.3 * x[i])
                amplitude = 0.8 + 0.4 * np.cos(0.5 * x[i])
                gaussian_peaks += amplitude * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional coupling with hyperbolic tangent interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.tanh(x[i] + x[j]) * (x[i]**2 + x[j]**2)
        
        # Saddle-point structure with chaotic modulation
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.3 + 0.7 * np.sin(0.6 * x[i])
                saddle += (x[i]**2 - x[i+1]**2) * modulator
        
        # Combined function with dimensionally adaptive weights
        dim_factor = 1.0 + 0.15 * np.log(self.dim + 1)
        return (0.2 * tent + 0.25 * spiral + 0.2 * vortex + 
                0.15 * gaussian_peaks + 0.1 * coupling + 0.1 * saddle) * dim_factor