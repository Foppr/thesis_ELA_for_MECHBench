import numpy as np

class HybridRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Separable polynomial component with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            degree = 2 + int(3 * (i % 4))  # Varying degrees: 2, 5, 2, 5, ...
            poly_term += (x_scaled[i] ** degree) / degree
        
        # Non-separable cosine correlation with adaptive frequency
        cos_corr = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 4.0 + 2.0 * np.sin(0.5 * i)
                cos_corr += np.cos(freq * (x_scaled[i] + x_scaled[j])) * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Adaptive noise component with spatial correlation
        noise = 0.0
        r = np.sqrt(np.sum(x_scaled**2))
        for i in range(self.dim):
            noise += np.sin(10.0 * x_scaled[i]) * np.cos(8.0 * x_scaled[i]) * np.exp(-0.3 * r)
        
        # Combined ruggedness with smooth basins
        ruggedness = 0.5 * np.sin(12.0 * r) * np.cos(7.0 * r) + 0.3 * np.sin(20.0 * r**2)
        
        # Final function value with dynamic weighting
        result = poly_term + 0.8 * cos_corr + 0.3 * noise + 0.6 * ruggedness
        
        return result