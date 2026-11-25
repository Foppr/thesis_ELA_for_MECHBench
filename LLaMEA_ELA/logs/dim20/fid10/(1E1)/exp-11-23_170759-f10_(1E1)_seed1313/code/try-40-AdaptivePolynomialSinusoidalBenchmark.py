import numpy as np

class AdaptivePolynomialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial terms with dimension-dependent exponents and coefficients
        for i in range(self.dim):
            power = 2 + (i % 4)  # Exponents 2,3,4,5 cycle through dimensions
            coeff = 0.5 + 0.1 * i
            result += coeff * (x[i] ** power)
        
        # Logarithmic barrier terms near boundaries with varying strength
        for i in range(self.dim):
            if abs(x[i]) < 0.5:
                result += 2.0 * np.log(1.0 + 10.0 * x[i]**2)
            else:
                result += 0.8 * np.log(1.0 + 0.1 * (5.0 - abs(x[i]))**2)
        
        # Sinusoidal components with frequency that increases with dimension
        for i in range(self.dim):
            freq = 2.0 * (i + 1)
            result += 0.7 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Cross-dimensional coupling with adaptive weights based on dimension
        if self.dim >= 2:
            for i in range(self.dim):
                for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                    weight = 0.3 * (1.0 + 0.1 * (i + j))
                    result += weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Radial component with dimension-dependent scaling and nonlinearity
        r_squared = np.sum(x**2)
        if r_squared > 0:
            result += 0.5 * np.sin(10.0 * np.sqrt(r_squared)) * np.exp(-0.1 * r_squared)
        
        # Adaptive penalty for large values with dimension-dependent strength
        for i in range(self.dim):
            result += 0.2 * (abs(x[i]) / (1.0 + abs(x[i])))**3
        
        # High-frequency oscillatory component with amplitude modulation
        for i in range(self.dim):
            result += 0.4 * np.sin(20.0 * x[i] + 0.5 * np.sin(5.0 * x[i]))
        
        # Dimensionality-dependent global modulation term
        result *= (1.0 + 0.1 * self.dim)
        
        return result