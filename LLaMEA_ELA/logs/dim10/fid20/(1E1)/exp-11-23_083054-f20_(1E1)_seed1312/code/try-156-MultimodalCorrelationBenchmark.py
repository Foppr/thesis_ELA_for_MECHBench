import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute correlation matrix with stronger interaction terms and adaptive weights
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i == j:
                    self.correlation_matrix[i, j] = 1.0
                else:
                    self.correlation_matrix[i, j] = 0.7 * np.sin(0.8 * (i - j)) + 0.25 * np.cos(0.6 * (i + j)) + 0.05 * np.sin(0.4 * i * j)
        
        # Precompute dynamic centers for radial basis functions with more variation
        self.centers = np.array([np.sin(i * 0.9) * np.cos(i * 0.6) + 0.1 * np.sin(i * 0.3) + 0.05 * np.cos(i * 0.2) for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced periodic trigonometric component with more complex frequencies and modulations
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i) + 0.5 * np.cos(0.3 * i) + 0.2 * np.sin(0.8 * i**1.5)
            f1 += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * (1.0 + 0.3 * np.sin(2.0 * x_norm[i]) + 0.1 * np.cos(3.0 * x_norm[i]))
        
        # Modified radial basis functions with adaptive widths and additional noise
        f2 = 0.0
        for i in range(self.dim):
            center = self.centers[i]
            width = 0.15 + 0.35 * np.sin(0.6 * i) + 0.05 * np.cos(0.4 * i) + 0.03 * np.sin(0.9 * i**1.2)
            f2 += np.exp(-0.5 * ((x_norm[i] - center) / width) ** 2) * (1.0 + 0.1 * np.sin(3.0 * x_norm[i]) + 0.05 * np.cos(4.0 * x_norm[i]))
        
        # Strengthened non-linear correlation component with interaction scaling and additional sinusoidal terms
        f3 = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    corr_term = self.correlation_matrix[i, j] * x_norm[i] * x_norm[j] * (1.0 + 0.2 * np.sin(x_norm[i] + x_norm[j]) + 0.1 * np.cos(x_norm[i] - x_norm[j]))
                    f3 += corr_term
        
        # Modified polynomial and exponential component with higher-order terms and additional trigonometric modulation
        f4 = 0.0
        for i in range(self.dim):
            poly_term = x_norm[i]**6 + 0.4 * x_norm[i]**3 + 0.2 * x_norm[i]**2 + 0.1 * x_norm[i]**5
            exp_term = np.exp(-0.4 * x_norm[i]**2) * (1.0 + 0.1 * np.cos(2.0 * x_norm[i]) + 0.05 * np.sin(3.0 * x_norm[i]))
            f4 += poly_term * exp_term
        
        # Combine all components with dynamic weights that emphasize different aspects
        weights = [0.35 + 0.03 * np.sin(0.7 * i) + 0.02 * np.cos(0.5 * i) for i in range(4)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4