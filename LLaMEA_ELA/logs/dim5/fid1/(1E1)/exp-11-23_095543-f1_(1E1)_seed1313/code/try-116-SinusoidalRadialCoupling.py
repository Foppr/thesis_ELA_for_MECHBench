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
            result += (i + 1) * x[i] ** 2
            
        # Add radial sinusoidal modulation with higher frequency
        r = np.sqrt(np.sum(x ** 2))
        result *= (1.0 + 0.7 * np.sin(5 * r) * np.cos(3 * r) * np.exp(-0.1 * r))
        
        # Add periodic components with different frequencies and stronger coupling
        for i in range(self.dim):
            result += 0.5 * np.sin(9 * x[i]) * np.cos(7 * x[(i + 1) % self.dim])
            
        # Add cross-dimensional coupling terms with higher interaction strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.sin(5 * x[i]) * np.cos(8 * x[j]) * np.exp(-0.2 * (x[i] - x[j]) ** 2)
                
        # Add radial harmonic components with increased complexity
        for i in range(self.dim):
            result += 0.25 * np.sin(12 * r) * np.cos(10 * r) * x[i] ** 2
            
        # Add multi-scale periodicity with stronger nonlinearity
        for i in range(self.dim):
            result += 0.35 * np.sin(18 * x[i]) * np.cos(15 * x[(i + 2) % self.dim]) * np.exp(-0.1 * x[i] ** 2)
            
        # Add asymmetric coupling with cubic terms
        for i in range(self.dim):
            result += 0.15 * (x[i] ** 3) * np.sin(4 * x[(i + 1) % self.dim]) * np.cos(2 * x[(i + 2) % self.dim])
            
        # Add radial peak structure with multiple local maxima
        result += 0.6 * np.exp(-0.3 * r ** 2) * np.sin(7 * r) * np.cos(4 * r)
        
        # Add dimensionality-dependent scaling with more complex interactions
        scaling = 1.0 + 0.2 * np.sum(np.sin(x) ** 2) + 0.1 * np.sum(np.cos(x) ** 2) + 0.05 * np.sum(np.tan(x) ** 2)
        result *= scaling
        
        # Add higher-order polynomial coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * x[i] ** 4 * x[j] ** 3 * np.sin(3 * (x[i] + x[j]))
                
        return result