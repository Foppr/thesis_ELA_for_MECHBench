import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and adaptive coefficients
        f1 = np.sum(0.8 * x_scaled**6 + 0.4 * x_scaled**5 - 0.3 * x_scaled**4 + 0.2 * x_scaled**3 + 0.1 * x_scaled**2)
        
        # Highly oscillatory trigonometric interference with exponentially increasing frequencies
        f2 = np.sum(np.sin(2**(10 * np.abs(x_scaled))) * np.cos(2**(9 * np.abs(x_scaled))) * 
                   np.sin(2**(8 * np.abs(x_scaled))) * np.cos(2**(7 * np.abs(x_scaled))))
        
        # Radial basis function components with exponentially varying centers and widths
        centers = np.linspace(-0.9, 0.9, min(7, self.dim))
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.1 + 0.05 * np.sin(i * 1.2)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**4)
        
        # Enhanced cross-dimensional interaction terms with exponentially increasing weights
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = (i + j) / (self.dim * (self.dim - 1) / 2) * np.exp(0.5 * (i + j))
                f4 += np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * weight + 0.3 * x_scaled[i] * x_scaled[j] * np.exp(-0.1 * (i + j))
        
        # Asymmetric saddle point structure with exponential modification
        f5 = np.sum((x_scaled**2 - 0.3)**5)
        
        # Ultra-high-frequency oscillation creating extremely rugged landscape
        f6 = np.sum(np.sin(100 * x_scaled) * np.cos(95 * x_scaled) * np.sin(90 * x_scaled))
        
        # Novel penalty mechanism with adaptive exponents and exponential scaling
        f7 = 0.8 * np.sum(np.abs(x_scaled)**4.2 + np.abs(x_scaled)**2.8 + 0.5 * np.abs(x_scaled)**1.5)
        
        # Additional sharp ridge structure
        f8 = 0.5 * np.sum(np.sin(30 * x_scaled) * np.cos(25 * x_scaled) * np.sin(20 * x_scaled))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8