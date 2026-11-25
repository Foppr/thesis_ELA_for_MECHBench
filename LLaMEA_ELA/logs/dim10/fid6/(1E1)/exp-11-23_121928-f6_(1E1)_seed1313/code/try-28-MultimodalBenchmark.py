import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with mixed degrees
        f1 = np.sum(x_norm**6 + 0.5 * x_norm**4 + 0.1 * x_norm**2)
        
        # Radial basis function component with multiple centers
        centers = np.linspace(-1, 1, min(5, self.dim))
        rbfs = []
        for i in range(len(centers)):
            if i < len(x_norm):
                rbfs.append(np.exp(-10 * (x_norm[i] - centers[i])**2))
        f2 = np.sum(rbfs) if rbfs else 0
        
        # Trigonometric terms with varying frequencies and amplitudes
        f3 = np.sum(np.sin(20 * x_norm) * np.cos(10 * x_norm) + 
                   np.sin(8 * x_norm) * np.cos(4 * x_norm))
        
        # Sigmoidal shaping term to create plateaus and steep regions
        f4 = np.sum(1 / (1 + np.exp(-5 * x_norm)) * (1 - 1 / (1 + np.exp(-5 * x_norm))))
        
        # Coupled chaotic terms with parameter modulation
        f5 = 0
        for i in range(self.dim):
            if i < len(x_norm):
                f5 += np.sin(np.pi * x_norm[i] * np.sin(3 * np.pi * x_norm[i]))
        
        # Dimensionality-dependent scaling and weighting
        dim_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combine all components with appropriate weights
        result = dim_factor * (0.4 * f1 + 0.3 * f2 + 0.2 * f3 + 0.05 * f4 + 0.05 * f5)
        
        # Add small noise term to prevent perfect symmetry
        noise = 0.001 * np.sum(np.random.rand(self.dim) * x_norm**2)
        
        return result + noise