import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Enhanced polynomial landscape with chaotic coefficients
        f1 = np.sum(0.8 * x_scaled**6 + 0.4 * x_scaled**5 - 0.3 * x_scaled**4 + 0.2 * x_scaled**3 + 0.1 * x_scaled**2 + 0.05 * x_scaled)
        
        # Chaotic trigonometric interference with non-linear frequency modulation
        f2 = np.sum(np.sin(20 * x_scaled + np.sin(10 * x_scaled)) * np.cos(18 * x_scaled + np.cos(9 * x_scaled)) * 
                   np.sin(14 * x_scaled + np.sin(7 * x_scaled)) * np.cos(11 * x_scaled + np.cos(5 * x_scaled)))
        
        # Adaptive radial basis function components with dynamic centers and widths
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = 0.5 * np.sin(i * 1.7) + 0.3 * np.cos(i * 2.3)
            width = 0.3 + 0.1 * np.sin(i * 0.9) + 0.05 * np.cos(i * 1.3)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**3)
        
        # Complex cross-dimensional interaction with chaotic coupling weights
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.sin(i * 0.7 + j * 0.5) * np.cos(i * 0.3 + j * 0.8)
                f4 += weight * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * (i + j)**1.5 / (self.dim**2)
        
        # Asymmetric chaotic saddle point structure with multiple exponent levels
        f5 = np.sum((x_scaled**3 - 0.3 * x_scaled)**2 + 0.2 * x_scaled**4)
        
        # Ultra-high frequency oscillation with fractal-like pattern
        f6 = np.sum(np.sin(100 * x_scaled) * np.cos(95 * x_scaled) * np.sin(90 * x_scaled))
        
        # Modified boundary penalty with logarithmic scaling
        f7 = 0.8 * np.sum(np.abs(x_scaled)**4 + np.log(1 + np.abs(x_scaled)**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7