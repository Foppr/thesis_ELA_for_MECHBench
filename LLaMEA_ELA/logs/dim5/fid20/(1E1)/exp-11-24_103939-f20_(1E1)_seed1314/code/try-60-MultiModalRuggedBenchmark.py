import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and interaction terms
        f1 = np.sum(x_scaled**6 + 0.7 * x_scaled**5 - 0.4 * x_scaled**4 + 0.2 * x_scaled**3 - 0.1 * x_scaled**2)
        
        # Trigonometric interference creating multiple local minima with varying frequencies
        f2 = np.sum(np.sin(12 * x_scaled) * np.cos(10 * x_scaled) * 
                   np.sin(8 * x_scaled) * np.cos(6 * x_scaled) * np.sin(4 * x_scaled))
        
        # Radial basis function components with varying centers, widths, and amplitudes
        centers = np.linspace(-0.9, 0.9, min(7, self.dim))
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.15 + 0.1 * np.sin(i * 0.5)
            amplitude = 1.0 + 0.5 * np.cos(i * 0.3)
            f3 += amplitude * np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Cross-dimensional interaction terms with non-linear coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f4 += np.sin(x_scaled[i] * x_scaled[j]) * (i + j) / (self.dim * (self.dim - 1) / 2)
        
        # Asymmetric saddle point structure with higher-order terms
        f5 = np.sum((x_scaled**2 - 0.3)**4)
        
        # High-frequency oscillation to increase ruggedness and non-linearity
        f6 = np.sum(np.sin(60 * x_scaled) * np.cos(55 * x_scaled) * np.sin(50 * x_scaled))
        
        # Combined penalty for boundary avoidance with asymmetric weighting
        f7 = 0.3 * np.sum(np.abs(x_scaled)**4 + 0.8 * np.abs(x_scaled)**2.5)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7