import numpy as np

class PolynomialLogSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial terms with varying degrees and coefficients
        for i in range(self.dim):
            result += 0.5 * (x[i] ** 4) + 0.3 * (x[i] ** 3) - 0.2 * (x[i] ** 2) + 0.1 * x[i]
        
        # Logarithmic components with offset to avoid singularities
        for i in range(self.dim):
            result += 0.4 * np.log(abs(x[i]) + 1.0) * np.exp(-0.1 * abs(x[i]))
        
        # Sine-based oscillatory terms with frequency modulation
        for i in range(self.dim):
            freq = 2.0 * (i + 1)
            result += 0.6 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Cross-dimensional interaction terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x[i] - x[j])
                result += 0.3 * np.sin(dist) * np.exp(-0.2 * dist) * (i + j + 1)
        
        # Radial sine component with variable amplitude
        if self.dim >= 2:
            r = np.sqrt(np.sum(x**2))
            result += 0.5 * np.sin(4.0 * r) * (1.0 + 0.2 * r)
        
        # Asymmetric exponential terms
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.25 * np.exp(-0.3 * x[i]) * (1.0 + 0.1 * x[i]**3)
            else:
                result += 0.2 * np.exp(-0.4 * abs(x[i])) * (1.0 + 0.15 * x[i]**3)
        
        # High-frequency oscillatory component
        for i in range(self.dim):
            result += 0.3 * np.sin(30.0 * x[i]) * np.cos(25.0 * x[i])
        
        # Global quadratic modulation
        sum_squares = np.sum(x**2)
        result += 0.4 * sum_squares * np.exp(-0.1 * sum_squares)
        
        # Boundary attraction term
        for i in range(self.dim):
            result += 0.2 * (5.0 - abs(x[i]))**3
        
        return result