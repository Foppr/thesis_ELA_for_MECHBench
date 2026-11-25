import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute correlation matrix for cross-dimensional interactions
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i == j:
                    self.correlation_matrix[i, j] = 1.0
                else:
                    self.correlation_matrix[i, j] = 0.3 * np.sin(0.5 * (i - j)) + 0.2 * np.cos(0.3 * (i + j))
        
        # Precompute dynamic centers for radial basis functions
        self.centers = np.array([np.sin(i * 0.7) * np.cos(i * 0.4) for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Periodic trigonometric component with varying frequencies
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.3 * i)
            f1 += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Radial basis functions with dynamic centers and varying widths
        f2 = 0.0
        for i in range(self.dim):
            center = self.centers[i]
            width = 0.2 + 0.3 * np.sin(0.4 * i)
            f2 += np.exp(-0.5 * ((x_norm[i] - center) / width) ** 2)
        
        # Non-linear correlation component
        f3 = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    corr_term = self.correlation_matrix[i, j] * x_norm[i] * x_norm[j]
                    f3 += corr_term
        
        # Mixed polynomial and exponential component
        f4 = 0.0
        for i in range(self.dim):
            poly_term = x_norm[i]**4 + 0.5 * x_norm[i]**3
            exp_term = np.exp(-0.5 * x_norm[i]**2)
            f4 += poly_term * exp_term
        
        # Combine all components with dynamic weights
        weights = [0.25 + 0.1 * np.sin(0.5 * i) for i in range(4)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4