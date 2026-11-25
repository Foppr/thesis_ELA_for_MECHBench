import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.r = 3.9  # Logistic map parameter
        self.c = np.random.rand(dim) * 2 - 1  # Random coefficients
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function components with varying widths and centers
        rbfs = []
        for i in range(8):
            center = np.random.rand(self.dim) * 2 - 1
            width = np.random.rand() * 0.5 + 0.1
            rbf = np.exp(-np.sum(((x_norm - center) / width)**2))
            rbfs.append(rbf)
        
        # Chaotic logistic map component for irregularity
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += (self.r * self.c[i] * (1 - self.c[i])) if i < len(self.c) else 0
        
        # Adaptive penalty terms based on distance from origin
        distances = np.sqrt(np.sum(x_norm**2, axis=-1, keepdims=True))
        penalties = np.where(distances > 1.0, 
                           10 * (distances - 1.0)**2,
                           0.0)
        
        # Combine all components with varying weights
        rbf_sum = np.sum(rbfs)
        return 2.0 * rbf_sum + 0.5 * chaotic + 0.3 * np.sum(penalties)