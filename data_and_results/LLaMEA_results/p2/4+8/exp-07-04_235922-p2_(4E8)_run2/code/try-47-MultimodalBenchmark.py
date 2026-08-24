import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute centers for radial basis functions
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with Gaussian peaks
        rbf = 0.0
        for i in range(10):
            center = self.centers[i]
            rbf += np.exp(-np.sum((x - center)**2) / (2 * 0.5**2)) * np.cos(2 * np.pi * np.sum((x - center)**2))
        
        # Trigonometric polynomial component
        trig = 0.0
        for i in range(self.dim):
            trig += (i + 1) * np.sin((i + 1) * x[i]) * np.cos((i + 1) * x[i])
        
        # Polynomial coupling with adaptive conditioning
        poly = 0.0
        for i in range(self.dim - 1):
            poly += (x[i]**2 + x[i+1]**2) * np.sin(3 * (x[i] - x[i+1]))
        
        # Cross-dimensional interaction with exponential decay
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.exp(-0.1 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
        
        # Add a global scaling factor that varies with dimensionality
        scaling = 1.0 + 0.1 * self.dim
        
        result = scaling * (rbf + trig + poly + cross)
        
        # Add small random noise to make it more challenging
        result += 0.001 * np.random.random()
        
        return result