import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Enhanced polynomial landscape with variable exponents and mixed terms
        f1 = np.sum(0.8 * x_scaled**6 + 0.5 * x_scaled**5 - 0.3 * x_scaled**4 + 0.2 * x_scaled**3 + 0.1 * x_scaled**2)
        
        # Modified trigonometric interference with variable frequencies and amplitudes
        f2 = np.sum(np.sin(20 * x_scaled) * np.cos(15 * x_scaled) * 
                   np.sin(10 * x_scaled) * np.cos(8 * x_scaled) * 
                   (np.abs(x_scaled) + 0.5))
        
        # Adaptive radial basis function components with dynamic centers and widths
        centers = np.linspace(-0.8, 0.8, min(6, self.dim))
        f3 = 0.0
        for i in range(min(6, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.3 + 0.1 * np.sin(i * 0.5)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2) * (1.0 + 0.2 * np.cos(i))
        
        # Enhanced cross-dimensional interaction terms with variable weights and higher-order products
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = (i + j) / (self.dim * (self.dim - 1) / 2)
                f4 += np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * weight + 0.2 * x_scaled[i]**2 * x_scaled[j]**2
        
        # Asymmetric saddle point structure with modified exponents and additional terms
        f5 = np.sum((x_scaled**3 - 0.3 * x_scaled)**2)
        
        # High-frequency oscillation with varying amplitude for increased ruggedness
        f6 = np.sum(np.sin(80 * x_scaled) * np.cos(75 * x_scaled) * (1.0 + 0.1 * np.abs(x_scaled)))
        
        # Combined penalty for boundary avoidance with modified exponents and additional terms
        f7 = 0.7 * np.sum(np.abs(x_scaled)**4.0 + np.abs(x_scaled)**2.0 + 0.5 * x_scaled**2)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7