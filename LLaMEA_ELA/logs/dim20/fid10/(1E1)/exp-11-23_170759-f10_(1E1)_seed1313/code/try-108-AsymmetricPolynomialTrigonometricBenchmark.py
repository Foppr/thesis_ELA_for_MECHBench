import numpy as np

class AsymmetricPolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial base with asymmetric exponents and coefficients
        for i in range(self.dim):
            exp_factor = 2.0 + 0.5 * np.sin(i)
            coeff = 1.0 + 0.3 * np.cos(i)
            result += coeff * (x[i] ** exp_factor)
        
        # Exponential decay with directional bias
        for i in range(self.dim):
            if x[i] >= 0:
                result += 0.5 * np.exp(-0.3 * x[i]) * (1.0 + 0.2 * x[i]**2)
            else:
                result += 0.4 * np.exp(-0.4 * abs(x[i])) * (1.0 + 0.15 * x[i]**2)
        
        # Trigonometric components with varying frequencies and phase shifts
        for i in range(self.dim):
            freq = 3.0 + 0.5 * i
            result += 0.3 * np.sin(freq * x[i] + 0.1 * i) * np.cos(freq * x[i] - 0.2 * i)
        
        # Cross-dimensional coupling with directional weighting
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.2 + 0.1 * (i + j) / self.dim
                result += weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Radial symmetry with modified oscillation and exponential decay
        if self.dim >= 2:
            r = np.sqrt(np.sum(x[:2]**2))
            result += 0.4 * np.sin(5.0 * r) * np.exp(-0.2 * r)
        
        # Asymmetric interaction terms favoring certain dimensions
        for i in range(self.dim):
            if i % 2 == 0:
                result += 0.25 * np.sin(x[i]) * np.cos(2.0 * x[i]) * (1.0 + 0.1 * x[i]**2)
            else:
                result += 0.2 * np.sin(2.0 * x[i]) * np.cos(x[i]) * (1.0 + 0.15 * x[i]**2)
        
        # High-frequency oscillatory component with boundary effect
        for i in range(self.dim):
            result += 0.3 * np.sin(20.0 * x[i]) * np.exp(-0.1 * abs(x[i]))
        
        # Boundary attraction with asymmetric penalty
        for i in range(self.dim):
            if x[i] < 0:
                result += 0.2 * (5.0 + x[i])**2
            else:
                result += 0.25 * (5.0 - x[i])**2
        
        # Modified polynomial interaction with increasing complexity
        for i in range(min(self.dim, 3)):
            result += 0.15 * (x[i] ** 3) * np.sin(x[i]) * (1.0 + 0.05 * i)
        
        return result