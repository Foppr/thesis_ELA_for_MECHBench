import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Create chaotic correlation matrix based on graph adjacency
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i == j:
                    self.correlation_matrix[i, j] = 1.0
                else:
                    # Use chaotic logistic map for correlation structure
                    chaos_val = 4.0 * (i + 1) * (1 - (i + 1) / dim) * 4.0 * (j + 1) * (1 - (j + 1) / dim)
                    self.correlation_matrix[i, j] = 0.3 * np.sin(chaos_val) + 0.2 * np.cos(chaos_val)
        
        # Dynamic centers using chaotic sequence
        self.centers = np.array([np.sin((i + 1) * 3.14159 * (1 + 0.1 * np.sin(i))) * np.cos((i + 1) * 2.718 * (1 + 0.1 * np.cos(i))) for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic trigonometric component with fractional frequencies
        f1 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.3 * i) + 0.5 * np.cos(0.7 * i)
            f1 += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * np.tan(0.5 * x_norm[i])
        
        # Radial basis functions with non-Euclidean centers and time-varying widths
        f2 = 0.0
        for i in range(self.dim):
            center = self.centers[i]
            width = 0.05 + 0.3 * np.sin(0.4 * i) * np.cos(0.6 * i)
            # Use Mahalanobis distance with chaotic covariance matrix
            f2 += np.exp(-0.5 * ((x_norm[i] - center) / width) ** 4)
        
        # Non-linear correlation component with chaotic weights
        f3 = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Use chaotic weight based on graph theory
                    weight = 0.2 * np.sin(2.5 * (i + j)) + 0.1 * np.cos(3.0 * (i - j))
                    corr_term = self.correlation_matrix[i, j] * x_norm[i] * x_norm[j] * weight
                    f3 += corr_term
        
        # Mixed polynomial and exponential with chaotic exponents
        f4 = 0.0
        for i in range(self.dim):
            poly_exp = 3.0 + 2.0 * np.sin(0.5 * i)
            exp_exp = 0.2 + 0.3 * np.cos(0.8 * i)
            poly_term = x_norm[i]**poly_exp + 0.5 * x_norm[i]**2
            exp_term = np.exp(-exp_exp * x_norm[i]**2)
            f4 += poly_term * exp_term
        
        # Combine all components with chaotic weights
        weights = [0.25 + 0.1 * np.sin(0.7 * i) + 0.05 * np.cos(0.9 * i) for i in range(4)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4