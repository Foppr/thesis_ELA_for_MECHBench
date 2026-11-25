import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic spiral basin component
        spiral = 0.0
        for i in range(self.dim):
            r = np.sqrt(x[i]**2 + x[(i+1)%self.dim]**2)
            theta = np.arctan2(x[(i+1)%self.dim], x[i])
            spiral += np.exp(-0.1 * r) * np.cos(3 * theta + 0.5 * r)
        
        # Dynamic Gaussian peaks with time-varying amplitudes
        gaussian_peaks = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.2 * i + np.sum(x))
            center = 2.0 * np.cos(0.3 * i)
            variance = 0.3 + 0.2 * np.sin(0.4 * i)
            gaussian_peaks += amp * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Asymmetric saddle structure with directional coupling
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                dx = x[i+1] - x[i]
                saddle += (x[i]**3 - x[i+1]**3) * np.tanh(0.5 * dx) * np.cos(0.2 * x[i])
        
        # Fractal dimensionality component with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.1 * i * self.dim)
            fractal += scale * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Cross-dimensional interaction with cosine coupling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.cos(0.5 * (x[i] + x[j])) * (x[i] - x[j])**2
        
        # Combine all components with adaptive weighting
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        return (0.25 * spiral + 0.3 * gaussian_peaks + 0.2 * saddle + 
                0.15 * fractal + 0.1 * coupling) * dim_factor