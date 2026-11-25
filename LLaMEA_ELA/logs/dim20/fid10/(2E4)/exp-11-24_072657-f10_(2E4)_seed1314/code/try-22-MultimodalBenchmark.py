import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map sequence for dimensionality
        self.logistic_seq = np.array([0.5] + [4 * x * (1 - x) for _ in range(dim + 10)])
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic logistic map based term
        chaotic_term = np.sum(self.logistic_seq[:self.dim] * np.sin(np.pi * x_norm))
        
        # Radial basis function with varying widths
        rbfs = []
        for i in range(self.dim):
            width = 0.5 + 0.5 * np.sin(i)
            rbfs.append(np.exp(-width * np.sum((x_norm - np.sin(i))**2)))
        rbf_term = np.sum(rbfs)
        
        # High-dimensional coupling with sine modulation
        coupling_term = 0
        for i in range(self.dim - 1):
            coupling_term += np.sin(x_norm[i] * x_norm[i+1]) * np.cos(2 * np.pi * (i + 1) / self.dim)
            
        # Polynomial chaos term with mixed degrees
        poly_term = np.sum(x_norm**4 + x_norm**3 - 2 * x_norm**2 + x_norm)
        
        # Saddle point structure via trigonometric coupling
        saddle_term = np.sum(np.sin(3 * x_norm) * np.cos(5 * x_norm))
        
        # Clustered valley structure with exponential decay
        cluster_term = 0
        for i in range(self.dim):
            cluster_term += np.exp(-np.abs(x_norm[i] - np.sin(i))) * np.cos(2 * np.pi * x_norm[i])
            
        # Combine all terms with adaptive weights
        return 0.4 * chaotic_term + 0.3 * rbf_term + 0.2 * coupling_term + 0.1 * poly_term + 0.1 * saddle_term + 0.2 * cluster_term