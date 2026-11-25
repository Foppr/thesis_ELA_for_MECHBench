import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and asymmetric coefficients
        f1 = np.sum(0.8 * x_scaled**6 + 0.4 * x_scaled**5 - 0.2 * x_scaled**4 + 0.1 * x_scaled**3 + 0.05 * x_scaled**2)
        
        # Enhanced trigonometric interference with variable frequencies and amplitudes
        f2 = np.sum(np.sin(20 * x_scaled) * np.cos(18 * x_scaled) * 
                   np.sin(16 * x_scaled) * np.cos(14 * x_scaled) * 
                   np.sin(12 * x_scaled) * np.cos(10 * x_scaled))
        
        # Multi-scale radial basis function components with dynamic centers and widths
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = 0.5 * np.sin(i * 0.7) if i < self.dim else 0.0
            width = 0.1 + 0.2 * np.cos(i * 0.5)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**3)
        
        # Stronger cross-dimensional interaction terms with non-linear coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f4 += (np.sin(x_scaled[i]) * np.cos(x_scaled[j]) + 
                       np.sin(x_scaled[j]) * np.cos(x_scaled[i])) * \
                      ((i + j) / (self.dim * (self.dim - 1) / 2))**2 + \
                      0.2 * x_scaled[i]**2 * x_scaled[j]**2
        
        # Asymmetric saddle point structure with higher-order terms
        f5 = np.sum((x_scaled**2 - 0.3)**4 + 0.3 * (x_scaled**2 - 0.3)**2)
        
        # Ultra-high frequency oscillation to increase ruggedness and create many local minima
        f6 = np.sum(np.sin(100 * x_scaled) * np.cos(95 * x_scaled) * 
                   np.sin(90 * x_scaled) * np.cos(85 * x_scaled))
        
        # Combined penalty for boundary avoidance with non-linear scaling
        f7 = 0.3 * np.sum(np.abs(x_scaled)**4 + np.abs(x_scaled)**2.5)
        
        # Additional asymmetric potential field to bias optimization towards certain regions
        f8 = np.sum(0.1 * x_scaled**7 + 0.05 * x_scaled**6 - 0.02 * x_scaled**5)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8