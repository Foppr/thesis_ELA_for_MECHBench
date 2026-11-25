import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slightly modified correlation matrix with increased interaction strength
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i == j:
                    self.correlation_matrix[i, j] = 1.0
                else:
                    self.correlation_matrix[i, j] = 0.7 * np.sin(0.8 * (i - j)) + 0.25 * np.cos(0.6 * (i + j))
        
        # Adjusted centers for radial basis functions with altered variation pattern
        self.centers = np.array([np.sin(i * 1.0) * np.cos(i * 0.7) + 0.12 * np.sin(i * 0.4) for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Modified trigonometric component with altered frequencies and added coupling
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.2 + 3.2 * np.sin(0.55 * i) + 0.55 * np.cos(0.35 * i)
            f1 += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * (1.0 + 0.32 * np.sin(2.1 * x_norm[i]))
        
        # Adjusted radial basis functions with modified widths and enhanced noise
        f2 = 0.0
        for i in range(self.dim):
            center = self.centers[i]
            width = 0.16 + 0.36 * np.sin(0.65 * i) + 0.055 * np.cos(0.45 * i)
            f2 += np.exp(-0.5 * ((x_norm[i] - center) / width) ** 2) * (1.0 + 0.11 * np.sin(3.1 * x_norm[i]))
        
        # Strengthened non-linear correlation component with modified interaction scaling
        f3 = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    corr_term = self.correlation_matrix[i, j] * x_norm[i] * x_norm[j] * (1.0 + 0.22 * np.sin(x_norm[i] + x_norm[j]))
                    f3 += corr_term
        
        # Modified polynomial and exponential component with adjusted higher-order terms
        f4 = 0.0
        for i in range(self.dim):
            poly_term = x_norm[i]**6.2 + 0.42 * x_norm[i]**3.1 + 0.21 * x_norm[i]**2.1
            exp_term = np.exp(-0.42 * x_norm[i]**2) * (1.0 + 0.11 * np.cos(2.1 * x_norm[i]))
            f4 += poly_term * exp_term
        
        # Combine all components with updated dynamic weights
        weights = [0.36 + 0.035 * np.sin(0.72 * i) for i in range(4)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4