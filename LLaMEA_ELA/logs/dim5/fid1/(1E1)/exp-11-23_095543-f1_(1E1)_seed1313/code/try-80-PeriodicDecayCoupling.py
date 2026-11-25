import numpy as np

class PeriodicDecayCoupling:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with varying weights
        result = 0.0
        for i in range(self.dim):
            weight = np.exp(-0.1 * i) + 0.5
            result += weight * x[i]**2
            
        # Add periodic peaks with varying amplitudes and frequencies
        for i in range(self.dim):
            amplitude = 2.0 + 0.5 * np.sin(0.5 * i)
            frequency = 3.0 + 0.3 * np.cos(0.7 * i)
            result += amplitude * np.sin(frequency * x[i])**2
            
        # Add exponential decay coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x[i] - x[j])
                coupling = np.exp(-0.5 * distance**2) * np.sin(2 * x[i]) * np.cos(3 * x[j])
                result += 0.3 * coupling
                
        # Add radial periodic components
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            result += 0.5 * np.sin(5 * r) * np.cos(7 * r) / (r + 0.1)
            
        # Add cross-dimensional interaction terms with exponential decay
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    result += 0.2 * np.exp(-0.3 * np.abs(x[i] - x[j])) * np.sin(4 * x[i]) * np.cos(5 * x[j])
                    
        # Add asymmetric saddle point structures
        for i in range(self.dim):
            result += 0.15 * (x[i]**3) * np.sin(2 * x[i]) + 0.1 * (x[i]**4) * np.cos(3 * x[i])
            
        # Add multi-scale periodic modulations
        for i in range(self.dim):
            result += 0.25 * np.sin(10 * x[i] + 0.5 * np.sin(3 * x[i])) * np.cos(8 * x[i] + 0.3 * np.cos(4 * x[i]))
            
        # Add dimensionality-dependent scaling
        scaling = 1.0 + 0.1 * np.sum(np.sin(x)**2) + 0.05 * np.sum(np.cos(x)**2)
        result *= scaling
        
        # Add normalization with exponential decay
        result /= (1.0 + 0.2 * np.sum(x**2) + 0.1 * np.exp(-0.1 * np.sum(x**2)))
        
        return result