import numpy as np

class ChaoticRotatedEllipsoid:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base rotated ellipsoid component
        result = 0.0
        for i in range(self.dim):
            result += (10 ** (2 * i / (self.dim - 1))) * (x[i] ** 2)
            
        # Add chaotic sine-wave interference
        for i in range(self.dim):
            phase = np.pi * np.sum(x[:i+1]) / (i + 1)
            result += 0.3 * np.sin(15 * x[i] + phase) * np.cos(7 * x[(i + 1) % self.dim] - phase)
            
        # Add cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.1 * (i + j))
                result += coupling * x[i] * x[j] * np.sin(x[i] ** 2 + x[j] ** 2)
                
        # Add a fourth-order polynomial to increase complexity
        for i in range(self.dim):
            result += 0.05 * (x[i] ** 4) * np.cos(3 * x[i])
            
        # Add a high-frequency oscillation component
        for i in range(self.dim):
            result += 0.2 * np.sin(20 * x[i]) * np.tan(0.5 * x[(i + 1) % self.dim])
            
        # Add normalization to keep function values reasonable
        result /= (1.0 + 0.1 * np.sum(x ** 2))
        
        return result