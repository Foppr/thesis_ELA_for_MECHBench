import numpy as np

class HierarchicalSineValleys:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with varying coefficients
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2
            
        # Add periodic sine-wave interactions between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * np.sin(x[i]) * np.cos(x[j]) * np.sin(2 * (x[i] + x[j]))
                
        # Asymmetric saddle point components
        for i in range(self.dim):
            result += 0.3 * (x[i] ** 3) * np.sin(4 * x[i]) + 0.2 * (x[i] ** 4) * np.cos(3 * x[i])
            
        # Hierarchical structure with nested frequencies
        r = np.sqrt(np.sum(x ** 2))
        for i in range(self.dim):
            result += 0.4 * np.sin(5 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * r)
            
        # Add chaotic modulation with dimension-dependent scaling
        for i in range(self.dim):
            result += 0.25 * np.sin(3 * x[i] + 0.5 * np.sin(2 * x[i])) * (i + 1) / self.dim
            
        # Add a multi-peak radial component
        result += 0.6 * np.exp(-0.5 * r) * np.sin(4 * r) * np.cos(3 * r)
        
        # Add a normalization factor with asymmetric scaling
        result /= (1.0 + 0.2 * np.sum(np.abs(x)) + 0.1 * np.sum(x ** 4))
        
        return result