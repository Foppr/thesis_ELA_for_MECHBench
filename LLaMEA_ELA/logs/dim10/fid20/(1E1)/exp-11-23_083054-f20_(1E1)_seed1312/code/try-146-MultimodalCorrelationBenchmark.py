import numpy as np

class MultimodalCorrelationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic correlation matrix with fractal-like structure
        self.correlation_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i == j:
                    self.correlation_matrix[i, j] = 1.0
                else:
                    # Chaotic correlation with fractal-like behavior
                    corr_val = 0.3 * np.sin(0.7 * (i - j)) + 0.2 * np.cos(0.5 * (i + j)) + \
                              0.1 * np.sin(0.3 * i * j) + 0.1 * np.cos(0.4 * (i**2 + j**2))
                    self.correlation_matrix[i, j] = corr_val
        
        # Precompute fractal-like centers for radial basis functions
        self.centers = np.array([np.sin(i * 0.8 + np.sin(i * 0.3)) * np.cos(i * 0.5 + np.cos(i * 0.4)) 
                                for i in range(dim)])
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Chaotic trigonometric component with fractal-like frequencies
        f1 = 0.0
        for i in range(self.dim):
            # Fractal-like frequency modulation
            freq = 2.0 + 3.0 * np.sin(0.5 * i + np.cos(0.3 * i)) + \
                   0.5 * np.sin(0.8 * i**1.5)
            f1 += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * \
                  np.exp(-0.1 * np.abs(x_norm[i]))
        
        # Fractal-like radial basis functions with chaotic widths
        f2 = 0.0
        for i in range(self.dim):
            center = self.centers[i]
            # Chaotic width modulation
            width = 0.05 + 0.3 * np.sin(0.4 * i + np.cos(0.6 * i)) + \
                   0.1 * np.sin(0.7 * i**1.2)
            f2 += np.exp(-0.5 * ((x_norm[i] - center) / width) ** 3) * \
                  (1.0 + 0.2 * np.sin(0.9 * i))
        
        # Non-linear chaotic correlation component
        f3 = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Chaotic correlation coefficient
                    corr_term = self.correlation_matrix[i, j] * x_norm[i] * x_norm[j] * \
                               (1.0 + 0.3 * np.sin(0.6 * (i + j)))
                    f3 += corr_term
        
        # Mixed polynomial and exponential component with chaotic exponents
        f4 = 0.0
        for i in range(self.dim):
            # Chaotic exponent modulation
            exp_mod = 0.2 + 0.3 * np.sin(0.5 * i + np.cos(0.4 * i))
            poly_term = x_norm[i]**(3.0 + exp_mod) + 0.4 * x_norm[i]**(1.5 + np.sin(0.7 * i))
            exp_term = np.exp(-0.2 * x_norm[i]**(2.0 + np.cos(0.6 * i)))
            f4 += poly_term * exp_term
        
        # Combine all components with chaotic weights
        weights = [0.25 + 0.03 * np.sin(0.7 * i + np.cos(0.5 * i)) for i in range(4)]
        
        return weights[0] * f1 + weights[1] * f2 + weights[2] * f3 + weights[3] * f4