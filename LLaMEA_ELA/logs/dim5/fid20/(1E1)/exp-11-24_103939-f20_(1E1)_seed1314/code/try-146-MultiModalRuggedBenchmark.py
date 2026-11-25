import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and chaotic coefficients
        f1 = np.sum(0.8 * x_scaled**6 + 0.4 * x_scaled**5 - 0.3 * x_scaled**4 + 0.2 * x_scaled**3 + 0.1 * x_scaled**2 + 0.05 * x_scaled)
        
        # Chaotic trigonometric interference creating highly complex local minima
        f2 = np.sum(np.sin(25 * x_scaled) * np.cos(20 * x_scaled) * 
                   np.sin(18 * x_scaled) * np.cos(16 * x_scaled) * 
                   np.sin(14 * x_scaled) * np.cos(12 * x_scaled))
        
        # Adaptive radial basis function components with dynamic centers and widths
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = 0.5 * np.sin(i * 1.7) + 0.3 * np.cos(i * 2.3)
            width = 0.3 + 0.1 * np.sin(i * 0.9) + 0.05 * np.cos(i * 1.3)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**3)
        
        # Enhanced cross-dimensional interaction with chaotic weights
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.2 * np.sin(i * j * 0.8) + 0.15 * np.cos(i + j * 0.6)
                f4 += weight * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) + 0.2 * x_scaled[i] * x_scaled[j]
        
        # Saddle point structure with exponential curvature
        f5 = np.sum(np.exp(3 * (x_scaled**2 - 0.5)**2) - 1)
        
        # Ultra-high frequency oscillation to increase ruggedness
        f6 = np.sum(np.sin(100 * x_scaled) * np.cos(95 * x_scaled) * np.sin(90 * x_scaled))
        
        # Combined penalty for boundary avoidance with exponential weights
        f7 = 0.8 * np.sum(np.abs(x_scaled)**4.2 + np.abs(x_scaled)**2.7)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7