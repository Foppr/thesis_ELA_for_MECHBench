import numpy as np

class AdaptivePolynomialLogarithmicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial terms with varying degrees and dimensionality scaling
        for i in range(self.dim):
            degree = 2 + (i % 4)  # Degrees 2,3,4,5 repeating
            coeff = 1.0 + 0.2 * i
            result += coeff * (x[i] ** degree)
        
        # Logarithmic components with adaptive scaling based on dimensionality
        for i in range(self.dim):
            if abs(x[i]) > 1e-8:  # Avoid log(0)
                result += 0.5 * np.log(abs(x[i]) + 1.0) * (1.0 + 0.1 * i)
        
        # Spherical component with adaptive radius scaling
        r_squared = np.sum(x**2)
        result += 0.3 * r_squared
        
        # Adaptive dimensionality-dependent interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-dimensionality
                interaction = (x[i] * x[j]) / (1.0 + abs(x[i]) + abs(x[j]))
                result += 0.2 * interaction * (1.0 + 0.05 * (i + j))
        
        # High-frequency oscillatory component with adaptive frequency
        for i in range(self.dim):
            freq = 10.0 * (1.0 + 0.1 * i)
            result += 0.4 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Asymmetric penalty terms with dimensionality-dependent weights
        for i in range(self.dim):
            if x[i] > 2.0:
                result += 0.8 * (x[i] - 2.0)**3
            elif x[i] < -2.0:
                result += 0.7 * (x[i] + 2.0)**3
        
        # Global modulation based on dimensionality and sum of squares
        dim_factor = np.sqrt(self.dim)
        result *= (1.0 + 0.1 * dim_factor + 0.05 * r_squared)
        
        # Boundary attraction with enhanced penalty near boundaries
        for i in range(self.dim):
            boundary_dist = min(abs(x[i] - 5.0), abs(x[i] + 5.0))
            result += 0.3 * boundary_dist**2
        
        return result