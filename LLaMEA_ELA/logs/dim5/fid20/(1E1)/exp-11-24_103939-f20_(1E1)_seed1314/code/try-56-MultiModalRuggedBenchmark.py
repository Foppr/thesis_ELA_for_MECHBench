import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Enhanced polynomial landscape with higher-order terms and mixed degrees
        f1 = np.sum(0.8 * x_scaled**6 + 0.4 * x_scaled**5 - 0.6 * x_scaled**4 + 0.3 * x_scaled**3 - 0.2 * x_scaled**2 + 0.1 * x_scaled)
        
        # Increased trigonometric interference with more frequencies and complex interactions
        f2 = np.sum(np.sin(15 * x_scaled) * np.cos(12 * x_scaled) * 
                   np.sin(10 * x_scaled) * np.cos(8 * x_scaled) * 
                   np.sin(6 * x_scaled) * np.cos(4 * x_scaled))
        
        # More aggressive radial basis function with non-uniform spacing and varying widths
        centers = np.linspace(-0.9, 0.9, min(7, self.dim))
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.15 + 0.2 * np.sin(i * 0.7)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2) * (1.0 + 0.5 * np.cos(3 * i))
        
        # Enhanced cross-dimensional interaction terms with stronger coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f4 += (np.sin(x_scaled[i]) * np.cos(x_scaled[j]) + 
                       np.cos(2 * x_scaled[i]) * np.sin(2 * x_scaled[j])) * (i + j) / (self.dim * (self.dim - 1) / 2)
        
        # Stronger asymmetric saddle point structure with higher-order terms
        f5 = np.sum((x_scaled**2 - 0.3)**4 + 0.5 * (x_scaled**2 - 0.3)**3)
        
        # Increased high-frequency oscillation for greater ruggedness
        f6 = np.sum(np.sin(60 * x_scaled) * np.cos(55 * x_scaled) + 
                   np.cos(50 * x_scaled) * np.sin(45 * x_scaled))
        
        # Enhanced boundary penalty with stronger nonlinearity
        f7 = 0.8 * np.sum(np.abs(x_scaled)**4 + np.abs(x_scaled)**2.5)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7