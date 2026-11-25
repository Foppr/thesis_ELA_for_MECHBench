import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees
        f1 = np.sum(x_scaled**6 + 0.7 * x_scaled**5 - 0.4 * x_scaled**4 + 0.2 * x_scaled**3)
        
        # Trigonometric interference creating multiple local minima with varying frequencies
        f2 = np.sum(np.sin(15 * x_scaled) * np.cos(13 * x_scaled) * 
                   np.sin(11 * x_scaled) * np.cos(9 * x_scaled))
        
        # Radial basis function components with varying centers and widths
        centers = np.linspace(-0.9, 0.9, min(6, self.dim))
        f3 = 0.0
        for i in range(min(6, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.15 + 0.05 * np.sin(i)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Enhanced cross-dimensional interaction terms with coupling strength
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f4 += np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * (i + j) / (self.dim * (self.dim - 1) / 2) + 0.05 * x_scaled[i] * x_scaled[j]
        
        # Asymmetric saddle point structure
        f5 = np.sum((x_scaled**2 - 0.3)**4)
        
        # High-frequency oscillation to increase ruggedness
        f6 = np.sum(np.sin(60 * x_scaled) * np.cos(55 * x_scaled))
        
        # Combined penalty for boundary avoidance
        f7 = 0.3 * np.sum(np.abs(x_scaled)**2.5 + np.abs(x_scaled)**1.2)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7