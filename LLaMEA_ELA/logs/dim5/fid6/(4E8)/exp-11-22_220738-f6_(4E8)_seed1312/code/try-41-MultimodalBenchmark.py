import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic term for central attraction
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms to create many local minima
        f2 = np.sum(np.sin(15 * np.pi * x_norm)**2 + 0.5 * np.sin(25 * np.pi * x_norm)**2)
        
        # Polynomial terms with different degrees to add complexity
        f3 = np.sum(x_norm**4 + 0.4 * x_norm**6 + 0.1 * x_norm**8)
        
        # Exponential decay with cosine modulation for additional structure
        f4 = np.sum(np.exp(-x_norm**2) * np.cos(5 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Additional sinusoidal term with varying phase to increase multimodality
        f5 = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) + 
                   0.3 * np.sin(20 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Chaotic oscillation component for increased complexity
        f6 = np.sum(np.sin(50 * np.pi * x_norm + np.sin(10 * np.pi * x_norm))**2)
        
        # Asymmetric saddle structure
        f7 = np.sum((x_norm**3 - 0.5 * x_norm**2) * (x_norm**2 - 0.3 * x_norm))
        
        # Cross-dimensional coupling term
        coupling = 0.0
        for i in range(self.dim-1):
            coupling += (x_norm[i] - x_norm[i+1])**2 * np.sin(10 * np.pi * (x_norm[i] + x_norm[i+1]))
        f8 = coupling
        
        # Combine all terms with carefully chosen weights
        return 0.2 * f1 + 0.5 * f2 + 0.1 * f3 + 0.08 * f4 + 0.07 * f5 + 0.05 * f6 + 0.03 * f7 + 0.02 * f8 + 5 * np.sum(np.sin(x_norm)) + 3 * np.sum(np.cos(x_norm))