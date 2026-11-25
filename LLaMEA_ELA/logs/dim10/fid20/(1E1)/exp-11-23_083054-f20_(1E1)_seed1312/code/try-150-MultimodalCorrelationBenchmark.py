import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced correlation matrix with stronger cross-dimensional dependencies
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i == j:
                    self.correlation_matrix[i, j] = 1.0
                else:
                    self.correlation_matrix[i, j] = 0.6 * np.sin(0.7 * (i - j)) + 0.2 * np.cos(0.5 * (i + j)) + 0.1 * np.sin(0.3 * (i * j))
        
        # Enhanced dynamic centers for radial basis functions
        self.centers = np.array([np.sin(i * 0.9) * np.cos(i * 0.6) + 0.1 * np.sin(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced periodic trigonometric component with more complex frequencies
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i) + 0.5 * np.cos(0.3 * i)
            f1 += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * (1.0 + 0.2 * np.sin(0.8 * i))
        
        # Enhanced radial basis functions with more variable widths and shifted centers
        f2 = 0.0
        for i in range(self.dim):
            center = self.centers[i] + 0.1 * np.cos(0.4 * i)
            width = 0.15 + 0.35 * np.sin(0.6 * i) + 0.1 * np.cos(0.2 * i)
            f2 += np.exp(-0.5 * ((x_norm[i] - center) / width) ** 2) * (1.0 + 0.1 * np.sin(0.7 * i))
        
        # Enhanced non-linear correlation component with additional interaction terms
        f3 = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    corr_term = self.correlation_matrix[i, j] * x_norm[i] * x_norm[j]
                    # Additional quadratic interaction term
                    corr_term += 0.1 * self.correlation_matrix[i, j] * (x_norm[i]**2) * (x_norm[j]**2)
                    f3 += corr_term
        
        # Enhanced mixed polynomial and exponential component with more complex terms
        f4 = 0.0
        for i in range(self.dim):
            poly_term = x_norm[i]**6 + 0.4 * x_norm[i]**3 + 0.2 * x_norm[i]**2
            exp_term = np.exp(-0.4 * x_norm[i]**2) * (1.0 + 0.1 * np.sin(0.9 * i))
            f4 += poly_term * exp_term
        
        # Combine all components with more dynamic weights
        weights = [0.35 + 0.08 * np.sin(0.7 * i) + 0.03 * np.cos(0.4 * i) for i in range(4)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4