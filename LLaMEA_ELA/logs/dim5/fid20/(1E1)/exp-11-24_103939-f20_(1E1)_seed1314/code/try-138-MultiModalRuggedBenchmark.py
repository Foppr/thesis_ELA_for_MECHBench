import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and exponential scaling
        f1 = np.sum(0.8 * x_scaled**4 + 0.5 * x_scaled**3 - 0.3 * x_scaled**2 + 0.2 * x_scaled)
        
        # Trigonometric interference creating multiple local minima with exponentially increasing frequencies
        f2 = np.sum(np.sin(20 * np.exp(1.5 * x_scaled)) * np.cos(18 * np.exp(1.3 * x_scaled)) * 
                   np.sin(16 * np.exp(1.2 * x_scaled)) * np.cos(14 * np.exp(1.1 * x_scaled)))
        
        # Radial basis function components with dynamic centers and widths
        centers = np.linspace(-0.8, 0.8, min(7, self.dim))
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.3 + 0.1 * np.sin(i * 0.7)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2) * (1.0 + 0.3 * np.sin(5 * x_scaled[i]))
        
        # Enhanced cross-dimensional interaction terms with exponential weights
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.1 * (i + j)) * (0.2 + 0.1 * np.sin(i * j))
                f4 += weight * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) + 0.2 * x_scaled[i] * x_scaled[j]
        
        # Asymmetric saddle point structure with exponential modification
        f5 = np.sum((x_scaled**2 - 0.3)**4 * np.exp(-0.5 * x_scaled**2))
        
        # High-frequency oscillation with exponential growth to increase ruggedness
        f6 = np.sum(np.sin(80 * np.exp(0.8 * x_scaled)) * np.cos(75 * np.exp(0.7 * x_scaled)))
        
        # Combined penalty for boundary avoidance with exponential exponents
        f7 = 0.8 * np.sum(np.abs(x_scaled)**4.2 + np.abs(x_scaled)**2.1)
        
        # Additional sharp ridge components to increase search difficulty
        f8 = 0.0
        for i in range(self.dim):
            f8 += 0.5 * np.sin(30 * x_scaled[i]) * np.cos(25 * x_scaled[i]) * np.exp(-0.1 * np.abs(x_scaled[i]))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8