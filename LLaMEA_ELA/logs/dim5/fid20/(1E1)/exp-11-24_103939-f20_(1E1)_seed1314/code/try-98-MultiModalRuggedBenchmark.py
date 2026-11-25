import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and exponential growth
        f1 = np.sum(np.exp(2 * np.abs(x_scaled)) * (x_scaled**4 + 0.3 * x_scaled**3 - 0.2 * x_scaled**2 + 0.05 * x_scaled))
        
        # Trigonometric interference creating multiple local minima with exponentially increasing frequencies
        f2 = np.sum(np.sin(20 * np.exp(0.5 * x_scaled)) * np.cos(15 * np.exp(0.3 * x_scaled)) * 
                   np.sin(10 * np.exp(0.7 * x_scaled)) * np.cos(8 * np.exp(0.4 * x_scaled)))
        
        # Radial basis function components with varying centers, widths, and exponential weights
        centers = np.linspace(-0.9, 0.9, min(7, self.dim))
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.1 + 0.05 * np.sin(i * 0.5)
            weight = np.exp(2 * i / self.dim)
            f3 += weight * np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Enhanced cross-dimensional interaction terms with exponential coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(0.3 * (i + j) / self.dim)
                f4 += coupling * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * np.tanh(x_scaled[i] * x_scaled[j])
        
        # Asymmetric saddle point structure with exponential modification
        f5 = np.sum(np.exp(3 * (x_scaled**2 - 0.5)**2) * (x_scaled**2 - 0.5))
        
        # High-frequency oscillation with exponentially increasing complexity
        f6 = np.sum(np.sin(100 * np.exp(0.8 * x_scaled)) * np.cos(90 * np.exp(0.6 * x_scaled)))
        
        # Combined penalty for boundary avoidance with exponential weighting
        f7 = 0.3 * np.sum(np.exp(3 * np.abs(x_scaled)) * (np.abs(x_scaled)**2.5 + np.abs(x_scaled)**1.2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7