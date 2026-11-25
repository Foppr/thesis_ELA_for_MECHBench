import numpy as np

class AdaptivePolynomialLogarithmicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial terms with dimensionality scaling
        for i in range(self.dim):
            result += 0.5 * (x[i] ** 4) * (1.0 + 0.1 * i)
            
        # Logarithmic components with adaptive scaling
        for i in range(self.dim):
            if abs(x[i]) > 1e-8:
                result += 0.3 * np.log(1.0 + abs(x[i])) * (1.0 + 0.05 * i)
            else:
                result += 0.3 * abs(x[i]) * (1.0 + 0.05 * i)
                
        # Spherical component with adaptive radius
        r_squared = np.sum(x**2)
        result += 0.4 * r_squared * (1.0 + 0.02 * self.dim)
        
        # Cross-dimensional coupling with varying strength
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling_strength = 0.1 * (1.0 + 0.05 * (i + j))
                result += coupling_strength * x[i] * x[j] * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Adaptive noise terms with dimensionality dependence
        for i in range(self.dim):
            noise = 0.05 * np.sin(10.0 * x[i]) * np.cos(8.0 * x[i]) * (1.0 + 0.03 * i)
            result += noise
            
        # Asymmetric penalty terms
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.2 * x[i]**3 * np.exp(-0.05 * x[i])
            else:
                result += 0.25 * abs(x[i])**2.5 * np.exp(-0.03 * abs(x[i]))
                
        # Global modulation with dimensionality-dependent frequency
        if self.dim > 1:
            result += 0.3 * np.sin(2.0 * np.sqrt(r_squared)) * np.cos(1.5 * np.sqrt(r_squared))
            
        # Boundary attraction with adaptive strength
        boundary_penalty = 0.0
        for i in range(self.dim):
            boundary_penalty += 0.15 * (5.0 - abs(x[i]))**2.5
        result += boundary_penalty
        
        return result