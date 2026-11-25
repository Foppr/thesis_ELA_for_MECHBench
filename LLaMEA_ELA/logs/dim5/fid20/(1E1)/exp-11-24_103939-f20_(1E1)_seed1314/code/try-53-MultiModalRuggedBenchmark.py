import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees
        f1 = np.sum(x_scaled**4 + 0.5 * x_scaled**3 - 0.3 * x_scaled**2 + 0.1 * x_scaled)
        
        # Trigonometric interference creating multiple local minima
        f2 = np.sum(np.sin(10 * x_scaled) * np.cos(8 * x_scaled) * 
                   np.sin(6 * x_scaled) * np.cos(4 * x_scaled))
        
        # Radial basis function components with varying centers and widths
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        f3 = 0.0
        for i in range(min(5, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.2 + 0.1 * np.sin(i)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Cross-dimensional interaction terms
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f4 += np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * (i + j) / (self.dim * (self.dim - 1) / 2)
        
        # Asymmetric saddle point structure
        f5 = np.sum((x_scaled**2 - 0.5)**3)
        
        # High-frequency oscillation to increase ruggedness
        f6 = np.sum(np.sin(50 * x_scaled) * np.cos(45 * x_scaled))
        
        # Combined penalty for boundary avoidance
        f7 = 0.5 * np.sum(np.abs(x_scaled)**3 + np.abs(x_scaled)**1.5)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7