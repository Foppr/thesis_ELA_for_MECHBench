import numpy as np

class AdaptiveMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial base with varying exponents and adaptive coefficients
        f1 = np.sum((x_scaled**6 + 0.8 * x_scaled**5 - 0.3 * x_scaled**4 + 0.2 * x_scaled**3) * 
                   (1 + 0.2 * np.sin(2 * np.pi * x_scaled)))
        
        # Multi-scale sinusoidal interference creating multiple local minima
        f2 = np.sum(np.sin(20 * x_scaled) * np.cos(15 * x_scaled) * 
                   np.sin(10 * x_scaled) * np.cos(8 * x_scaled) * 
                   (1 + 0.1 * np.cos(5 * x_scaled)))
        
        # Radial basis function with adaptive centers and widths
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = 0.5 * np.sin(i * 0.5)
            width = 0.3 + 0.1 * np.cos(i * 0.3)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Cross-dimensional interaction with varying coupling strength
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (i + j) / (self.dim * (self.dim - 1) / 2)
                f4 += coupling * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * \
                      (np.sin(3 * x_scaled[i] + 2 * x_scaled[j]) + 0.5)
        
        # Asymmetric saddle with variable exponent
        f5 = np.sum((x_scaled**2 - 0.5)**4 + 0.1 * x_scaled**6)
        
        # High-frequency oscillation with adaptive amplitude
        f6 = np.sum(np.sin(80 * x_scaled) * np.cos(75 * x_scaled) * 
                   (1 + 0.3 * np.sin(25 * x_scaled)))
        
        # Boundary penalty with variable exponent
        f7 = 0.5 * np.sum((np.abs(x_scaled)**4 + np.abs(x_scaled)**2.5) * 
                         (1 + 0.1 * np.cos(3 * np.pi * x_scaled)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7