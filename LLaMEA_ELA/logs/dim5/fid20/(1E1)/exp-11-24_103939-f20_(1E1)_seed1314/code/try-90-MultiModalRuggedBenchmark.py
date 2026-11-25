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
        f2 = np.sum(np.sin(20 * x_scaled) * np.cos(18 * x_scaled) * 
                   np.sin(16 * x_scaled) * np.cos(14 * x_scaled))
        
        # Radial basis function components with varying centers and widths
        centers = np.linspace(-0.8, 0.8, min(7, self.dim))
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.15 + 0.05 * np.sin(i)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Enhanced cross-dimensional interaction terms with stronger coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f4 += (np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * 
                       (i + j) / (self.dim * (self.dim - 1) / 2) + 
                       0.2 * x_scaled[i] * x_scaled[j] * np.sin(i * j))
        
        # Asymmetric saddle point structure
        f5 = np.sum((x_scaled**2 - 0.5)**3)
        
        # High-frequency oscillation to increase ruggedness
        f6 = np.sum(np.sin(80 * x_scaled) * np.cos(75 * x_scaled))
        
        # Combined penalty for boundary avoidance with increased weight
        f7 = 0.8 * np.sum(np.abs(x_scaled)**3 + np.abs(x_scaled)**1.5)
        
        # Additional noise term to increase problem difficulty
        noise = 0.05 * np.sum(np.sin(100 * x_scaled) * np.cos(95 * x_scaled))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + noise