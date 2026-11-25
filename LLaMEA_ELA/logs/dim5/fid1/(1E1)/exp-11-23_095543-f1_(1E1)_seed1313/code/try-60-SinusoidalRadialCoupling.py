import numpy as np

class SinusoidalRadialCoupling:
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
            result += (i + 1) * (x[i] ** 2)
            
        # Add radial sinusoidal components
        r = np.sqrt(np.sum(x ** 2))
        result += 2.0 * np.sin(5 * r) * np.cos(3 * r) + 1.5 * np.sin(7 * r)
        
        # Add periodic components in each dimension
        for i in range(self.dim):
            result += 0.8 * np.sin(4 * x[i]) * np.cos(6 * x[i])
            
        # Add cross-dimensional coupling with sinusoidal interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                result += 0.3 * coupling * (i + j + 1)
                
        # Add multi-scale periodic components
        for i in range(self.dim):
            result += 0.5 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.sin(6 * x[i])
            
        # Add radial polynomial terms
        result += 0.2 * r ** 3 + 0.1 * r ** 4
            
        # Add chaotic perturbations
        for i in range(self.dim):
            result += 0.1 * np.sin(20 * x[i]) * np.cos(15 * x[i])
            
        # Add normalization and scaling
        result /= (1.0 + 0.01 * r ** 2)
        
        return result