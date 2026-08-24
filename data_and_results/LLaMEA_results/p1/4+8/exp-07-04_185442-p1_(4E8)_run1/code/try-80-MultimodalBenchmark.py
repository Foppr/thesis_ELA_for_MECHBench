import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Logistic map chaotic dynamics in each dimension
        logistic = np.sum(4 * x_norm * (1 - x_norm))
        
        # Radial basis function with varying widths and centers
        centers = np.linspace(-1, 1, min(5, self.dim))
        widths = np.logspace(-2, 1, min(5, self.dim))
        rbf = np.sum(np.exp(-np.sum(((x_norm[:, np.newaxis] - centers) / widths)**2, axis=0)))
        
        # Asymmetric saddle points with varying steepness
        saddle = np.sum((x_norm**2 - 1)**2 * np.sin(2 * np.pi * x_norm)**2)
        
        # Cross-dimensional coupling with exponential decay
        coupling = np.sum(np.exp(-0.5 * np.abs(x_norm[:-1] - x_norm[1:])) * (x_norm[:-1] + x_norm[1:]))
        
        # Add a chaotic noise component
        chaotic_noise = 0.02 * np.sum(np.sin(13 * x_norm) * np.cos(7 * x_norm))
        
        # Combine all components
        return logistic + rbf + saddle + coupling + chaotic_noise