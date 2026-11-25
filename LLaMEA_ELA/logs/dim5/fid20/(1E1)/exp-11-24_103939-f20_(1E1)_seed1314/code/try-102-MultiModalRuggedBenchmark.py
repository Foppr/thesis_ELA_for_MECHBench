import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Higher-order polynomial landscape with mixed degrees and cross-terms
        f1 = np.sum(x_scaled**6 + 0.7 * x_scaled**5 - 0.4 * x_scaled**4 + 0.2 * x_scaled**3 - 0.1 * x_scaled**2 + 0.05 * x_scaled)
        
        # Enhanced trigonometric interference with non-uniform frequencies and phase shifts
        f2 = np.sum(np.sin(15 * x_scaled) * np.cos(13 * x_scaled) * 
                   np.sin(11 * x_scaled) * np.cos(9 * x_scaled) * 
                   np.sin(7 * x_scaled) * np.cos(5 * x_scaled))
        
        # Multi-scale radial basis function components with dynamic centers and widths
        centers = np.linspace(-0.9, 0.9, min(7, self.dim))
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.15 + 0.2 * np.sin(i * 0.5)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**3)
        
        # Complex cross-dimensional interaction terms with nonlinear coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x_scaled[i]**2) * np.cos(x_scaled[j]**2) * (i + j) / (self.dim * (self.dim - 1) / 2)
                f4 += interaction + 0.15 * x_scaled[i]**3 * x_scaled[j]**2
        
        # Asymmetric saddle point structure with cubic and quartic components
        f5 = np.sum((x_scaled**2 - 0.3)**4 + (x_scaled**3 - 0.2)**2)
        
        # Ultra-high-frequency oscillation to increase ruggedness
        f6 = np.sum(np.sin(80 * x_scaled) * np.cos(75 * x_scaled) * np.sin(70 * x_scaled))
        
        # Novel asymmetric penalty structure with mixed norms
        f7 = 0.3 * np.sum(np.abs(x_scaled)**4 + np.abs(x_scaled)**2.5 + 0.5 * np.abs(x_scaled)**1.8)
        
        # Additional non-separable coupling through exponential interactions
        f8 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f8 += np.exp(-np.abs(x_scaled[i] - x_scaled[j]) * (i + j) / self.dim)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8