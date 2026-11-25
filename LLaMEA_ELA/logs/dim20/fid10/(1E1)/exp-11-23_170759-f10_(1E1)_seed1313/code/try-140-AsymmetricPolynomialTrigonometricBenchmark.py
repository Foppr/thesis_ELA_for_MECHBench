import numpy as np

class AsymmetricPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial base terms with asymmetric coefficients
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.5 * (x[i] ** 3) * (1.0 + 0.1 * i)
            else:
                result += 0.3 * (x[i] ** 3) * (1.0 + 0.2 * i)
        
        # Exponential decay with directional bias
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.4 * np.exp(-0.5 * x[i]) * (1.0 + 0.1 * x[i]**2)
            else:
                result += 0.3 * np.exp(-0.7 * abs(x[i])) * (1.0 + 0.15 * x[i]**2)
        
        # Trigonometric components with varying frequencies and phases
        for i in range(self.dim):
            freq = 2.0 * (i + 1)
            result += 0.25 * np.sin(freq * x[i] + 0.3 * i) * np.cos(freq * x[i] - 0.2 * i)
        
        # Cross-dimensional interaction with directional coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(x[i]) * np.cos(x[j]) * (1.0 + 0.05 * (x[i]**2 + x[j]**2))
        
        # Asymmetric exponential interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if x[i] > 0 and x[j] > 0:
                    result += 0.1 * np.exp(-0.3 * (x[i]**2 + x[j]**2)) * (x[i] + x[j])
                else:
                    result += 0.08 * np.exp(-0.4 * (x[i]**2 + x[j]**2)) * (abs(x[i]) + abs(x[j]))
        
        # Radial symmetry with modified oscillation
        if self.dim >= 2:
            r = np.sqrt(np.sum(x[:2]**2))
            result += 0.35 * np.sin(5.0 * r + 0.1 * r**2) * np.exp(-0.2 * r)
        
        # High-frequency oscillatory component
        for i in range(self.dim):
            result += 0.2 * np.sin(20.0 * x[i]) * (1.0 + 0.05 * abs(x[i]))
        
        # Boundary attraction with asymmetric penalty
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.15 * (5.0 - x[i])**2.5
            else:
                result += 0.2 * (5.0 + x[i])**2.5
        
        # Directional bias terms
        for i in range(self.dim):
            result += 0.1 * x[i] * np.sin(3.0 * x[i]) * (1.0 + 0.02 * i)
        
        # Higher-order polynomial interaction
        if self.dim >= 3:
            for i in range(3):
                result += 0.05 * (x[i] ** 4) * np.cos(x[i])
        
        return result