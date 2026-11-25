import numpy as np

class ChaoticCrossDimensionalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial term with high-order scaling
        result = np.sum(x**6) / 6.0
        
        # Exponential coupling terms with adaptive strengths
        for i in range(self.dim):
            strength = 2.0 / (1.0 + np.exp(-0.5 * x[i]))
            result += strength * np.exp(-0.5 * x[i]**2) * np.sin(3.0 * x[i])
            
        # Logarithmic interaction terms with varying base
        for i in range(self.dim):
            if abs(x[i]) > 1e-6:
                result += 0.5 * np.log(abs(x[i]) + 1.0) * np.cos(2.0 * x[i])
                
        # Chaotic cross-dimensional coupling using sine and cosine
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 / (1.0 + abs(x[i] - x[j]))
                result += coupling * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                
        # Adaptive penalty based on exponential decay with oscillation
        dist = np.sqrt(np.sum(x**2))
        result += 1.5 * np.exp(-dist / 3.0) * np.sin(4.0 * dist)
        
        # Fractional polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.3 * (x[i]**1.5 + x[i]**2.5)
            
        # Multi-scale sinusoidal modulation
        for i in range(self.dim):
            result += 0.4 * np.sin(8.0 * x[i]) * np.cos(5.0 * x[i]) * np.exp(-0.1 * abs(x[i]))
            
        # Cross-dimensional chaotic interaction with variable coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i + j < self.dim:
                    coupling = 0.8 / (1.0 + np.abs(np.sin(x[i]) * np.cos(x[j])))
                    result += coupling * np.tan(0.5 * x[i] * x[j])
                    
        # Central repulsion term to create multiple local minima
        result += 0.6 * np.exp(-np.sum((x - 0.5)**2) / 1.0)
        
        return result