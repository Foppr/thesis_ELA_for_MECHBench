import numpy as np

class ChaoticPolynomialCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters for each dimension
        self.chaotic_params = np.array([0.5 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        
        # Precompute adaptive polynomial degrees
        self.degrees = np.array([2 + int(3 * np.sin(0.6 * i)) for i in range(dim)])
        
        # Precompute correlation matrix for spherical interactions
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i == j:
                    self.correlation_matrix[i, j] = 1.0
                else:
                    dist = np.sqrt((i - j) ** 2)
                    self.correlation_matrix[i, j] = np.exp(-0.1 * dist) * np.cos(0.3 * dist)
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic sine component with dynamic parameters
        f1 = 0.0
        for i in range(self.dim):
            chaotic_val = self.chaotic_params[i] * np.sin(10 * x_norm[i]) + \
                         (1 - self.chaotic_params[i]) * np.cos(5 * x_norm[i])
            f1 += chaotic_val ** 2
        
        # Adaptive polynomial component
        f2 = 0.0
        for i in range(self.dim):
            poly_term = x_norm[i] ** self.degrees[i]
            f2 += poly_term * (1 + 0.3 * np.sin(2 * x_norm[i]))
        
        # Spherical correlation component
        f3 = 0.0
        for i in range(self.dim):
            corr_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    corr_sum += self.correlation_matrix[i, j] * x_norm[j]
            f3 += (x_norm[i] + corr_sum) ** 2
        
        # Mixed exponential and logarithmic component
        f4 = 0.0
        for i in range(self.dim):
            exp_term = np.exp(-0.5 * x_norm[i]**2)
            log_term = np.log(1 + 0.5 * np.abs(x_norm[i]))
            f4 += exp_term * log_term
        
        # Combine all components with varying weights
        weights = [0.3 + 0.1 * np.sin(0.4 * i) for i in range(4)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4