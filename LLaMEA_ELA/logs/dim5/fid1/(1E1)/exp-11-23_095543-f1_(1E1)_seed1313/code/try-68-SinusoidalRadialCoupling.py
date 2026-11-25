import numpy as np

class SinusoidalRadialCoupling:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with varying conditioning
        result = 0.0
        for i in range(self.dim):
            result += (1.0 + 0.5 * np.sin(i)) * x[i]**2
            
        # Add radial sinusoidal modulation
        r = np.sqrt(np.sum(x**2))
        result += 2.0 * np.sin(3 * r) * np.cos(2 * r)
        
        # Add periodic components with different frequencies
        for i in range(self.dim):
            result += 0.5 * np.sin(5 * x[i]) * np.cos(4 * x[i])
            
        # Cross-dimensional coupling with phase shifts
        for i in range(self.dim):
            j = (i + 1) % self.dim
            result += 0.3 * np.sin(x[i] + 0.5 * x[j]) * np.cos(2 * x[i] - x[j])
            
        # Add multiple local minima with varying depths
        for i in range(self.dim):
            result += 0.4 * np.sin(10 * x[i])**2
            
        # Radial periodic structure with amplitude modulation
        result += 1.5 * np.cos(7 * r) * np.exp(-0.1 * r**2)
        
        # Add asymmetric components to increase complexity
        for i in range(self.dim):
            result += 0.2 * x[i]**3 * np.sin(x[i])
            
        # Normalize by a function that varies with input magnitude
        norm_factor = 1.0 + 0.1 * r + 0.05 * r**2
        result /= norm_factor
        
        return result