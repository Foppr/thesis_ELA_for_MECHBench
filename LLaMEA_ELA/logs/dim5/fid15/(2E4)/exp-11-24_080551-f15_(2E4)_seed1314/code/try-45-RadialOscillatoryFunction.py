import numpy as np

class RadialOscillatoryFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base radial term with polynomial barrier
        r = np.sqrt(np.sum(x**2))
        result = r**4 / 4.0 + 0.5 * r**2
        
        # Sinusoidal oscillations in each dimension
        for i in range(self.dim):
            result += 2.0 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
        # Cross-dimensional coupling with varying amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 / (1.0 + (i + j) * 0.1)
                result += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Radial oscillation component
        result += 1.5 * np.sin(5.0 * r) * np.cos(3.0 * r)
        
        # Polynomial barrier terms with different exponents
        for i in range(self.dim):
            result += 0.3 * (x[i]**6 + x[i]**4) * np.exp(-abs(x[i]))
            
        # Additional high-frequency cross-dimensional interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(15.0 * x[i] * x[j]) * (1.0 / (i + j + 1)**0.8)
                
        # Central repulsion term to increase challenge
        result += 0.8 * np.exp(-r**2 / 2.0) * np.sin(r)
        
        return result