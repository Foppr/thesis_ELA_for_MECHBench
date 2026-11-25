import numpy as np

class PolynomialRBFHyperbolicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial chaos expansion terms with varying degrees and coefficients
        for i in range(self.dim):
            result += 0.3 * (x[i]**6 + 0.5 * x[i]**4 + 0.2 * x[i]**2) * np.exp(-0.1 * abs(x[i]))
        
        # Radial basis function components with Gaussian and multiquadric kernels
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                r = np.sqrt((x[i] - x[j])**2 + 0.01)
                result += 0.2 * np.exp(-5.0 * r**2) * (1.0 + 0.1 * r**2)
        
        # Asymmetric hyperbolic sine components with coordinate-dependent scaling
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.4 * np.sinh(1.5 * x[i]) * (1.0 + 0.2 * x[i]**2)
            else:
                result += 0.3 * np.sinh(2.0 * x[i]) * (1.0 + 0.15 * x[i]**2)
        
        # Multidimensional coupling through cross-product interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # High-order polynomial interactions with exponential modulation
        for i in range(min(self.dim, 3)):
            for j in range(i+1, min(self.dim, 4)):
                result += 0.2 * (x[i]**3 + x[j]**3) * np.exp(-0.1 * abs(x[i] - x[j]))
        
        # Radial symmetry with modified Bessel function components
        if self.dim >= 2:
            r = np.sqrt(np.sum(x[:2]**2))
            result += 0.5 * r * np.exp(-0.3 * r) * np.sin(4.0 * r)
        
        # Boundary repulsion terms with variable strength
        for i in range(self.dim):
            result += 0.25 * (5.0 - abs(x[i]))**4
        
        # Multi-scale oscillatory components with frequency modulation
        for i in range(self.dim):
            freq = 10.0 + 5.0 * np.sin(0.5 * i)
            result += 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * (1.0 + 0.05 * x[i]**2)
        
        # Cross-dimensional coupling with trigonometric products
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.cos(x[i] + x[j]) * np.sin(x[i] - x[j]) * np.exp(-0.2 * abs(x[i] * x[j]))
        
        # Asymmetric exponential terms with polynomial modulation
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.35 * np.exp(-0.8 * x[i]) * (1.0 + 0.3 * x[i]**3)
            else:
                result += 0.25 * np.exp(-1.2 * abs(x[i])) * (1.0 + 0.2 * x[i]**3)
        
        # Global modulation with sum of powers and exponential decay
        sum_powers = np.sum(np.abs(x)**3)
        result += 0.4 * np.exp(-0.15 * sum_powers) * np.sin(2.0 * sum_powers)
        
        return result