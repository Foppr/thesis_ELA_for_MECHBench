import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees
        f1 = np.sum(x_scaled**4 + 0.5 * x_scaled**3 - 0.3 * x_scaled**2 + 0.1 * x_scaled)
        
        # Trigonometric interference creating multiple local minima with modified frequencies
        f2 = np.sum(np.sin(12 * x_scaled) * np.cos(10 * x_scaled) * 
                   np.sin(8 * x_scaled) * np.cos(6 * x_scaled))
        
        # Radial basis function components with varying centers and widths
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        f3 = 0.0
        for i in range(min(5, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.2 + 0.1 * np.sin(i)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Enhanced cross-dimensional interaction terms with non-linear coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * (i + j) / (self.dim * (self.dim - 1) / 2)
                interaction += 0.1 * x_scaled[i] * x_scaled[j]
                interaction += 0.05 * np.sin(x_scaled[i] * x_scaled[j])
                f4 += interaction
        
        # Asymmetric saddle point structure with higher-order terms
        f5 = np.sum((x_scaled**2 - 0.5)**3 + 0.1 * x_scaled**5)
        
        # High-frequency oscillation to increase ruggedness with random phase shifts
        f6 = 0.0
        for i in range(self.dim):
            freq = 55 + 5 * np.sin(i)
            f6 += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] + i * 0.1)
        
        # Novel asymmetric penalty term with exponential growth
        f7 = np.sum(np.exp(2 * np.abs(x_scaled)) - 2 * np.abs(x_scaled) - 1)
        
        # Add a global scaling factor to increase overall difficulty
        return 2.0 * (f1 + f2 + f3 + f4 + f5 + f6 + f7)