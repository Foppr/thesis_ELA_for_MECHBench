import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with multiple centers
        rbf_sum = 0.0
        centers = np.random.uniform(-1, 1, (10, self.dim))
        for i in range(10):
            center = centers[i]
            distance = np.sum((x_norm - center)**2)
            rbf_sum += np.exp(-5 * distance) * np.sin(10 * np.pi * distance)
        
        # Fractal-like structure using recursive sine components
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2**(i+1) * np.pi * x_norm[i]) * np.cos(3**(i+1) * np.pi * x_norm[i])
        
        # Gradient attraction fields creating valleys and ridges
        attraction = 0.0
        for i in range(self.dim):
            attraction += (x_norm[i]**3 - 0.5 * x_norm[i]) * np.cos(2 * np.pi * x_norm[i])
        
        # Multi-scale periodic structure with varying frequencies
        periodic = 0.0
        for i in range(self.dim):
            freq = 2**(i % 3 + 1)
            periodic += np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Asymmetric scaling and coupling between dimensions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling += (x_norm[i]**2 + x_norm[j]**2) * np.sin(np.pi * (x_norm[i] - x_norm[j]))
        
        # Add noise and scale components
        noise = 0.01 * np.random.random()
        
        return 0.8 * rbf_sum + 0.6 * fractal + 0.4 * attraction + 0.5 * periodic + 0.3 * coupling + noise