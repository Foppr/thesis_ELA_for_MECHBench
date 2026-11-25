import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute correlation matrix with stronger interaction terms
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i == j:
                    self.correlation_matrix[i, j] = 1.0
                else:
                    self.correlation_matrix[i, j] = 0.7 * np.sin(0.8 * (i - j)) + 0.25 * np.cos(0.6 * (i + j))
        
        # Precompute dynamic centers for radial basis functions with more variation
        self.centers = np.array([np.sin(i * 1.0) * np.cos(i * 0.7) + 0.15 * np.sin(i * 0.4) for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced periodic trigonometric component with more complex frequencies
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.5 + 3.5 * np.sin(0.6 * i) + 0.6 * np.cos(0.4 * i)
            f1 += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * (1.0 + 0.35 * np.sin(2.5 * x_norm[i]))
        
        # Modified radial basis functions with adaptive widths and additional noise
        f2 = 0.0
        for i in range(self.dim):
            center = self.centers[i]
            width = 0.2 + 0.4 * np.sin(0.7 * i) + 0.06 * np.cos(0.5 * i)
            f2 += np.exp(-0.5 * ((x_norm[i] - center) / width) ** 2) * (1.0 + 0.15 * np.sin(3.5 * x_norm[i]))
        
        # Strengthened non-linear correlation component with interaction scaling
        f3 = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    corr_term = self.correlation_matrix[i, j] * x_norm[i] * x_norm[j] * (1.0 + 0.25 * np.sin(x_norm[i] + x_norm[j]))
                    f3 += corr_term
        
        # Modified polynomial and exponential component with higher-order terms
        f4 = 0.0
        for i in range(self.dim):
            poly_term = x_norm[i]**7 + 0.45 * x_norm[i]**3 + 0.25 * x_norm[i]**2
            exp_term = np.exp(-0.45 * x_norm[i]**2) * (1.0 + 0.15 * np.cos(2.5 * x_norm[i]))
            f4 += poly_term * exp_term
        
        # Combine all components with dynamic weights that emphasize different aspects
        weights = [0.37 + 0.04 * np.sin(0.8 * i) for i in range(4)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4