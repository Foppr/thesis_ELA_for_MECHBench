import numpy as np

class AdaptivePolynomialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Polynomial terms with dimension-dependent exponents and coefficients
        for i in range(self.dim):
            power = 2 + (i % 4)  # Varying powers: 2,3,4,5
            coeff = 0.5 + 0.1 * i
            result += coeff * (x[i] ** power)
        
        # Exponential decay with adaptive rate based on dimension
        for i in range(self.dim):
            rate = 0.1 + 0.05 * (i / max(1, self.dim - 1))
            result += 0.3 * np.exp(-rate * abs(x[i])) * (1.0 + 0.2 * x[i]**2)
        
        # Sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 * (i + 1) * (1.0 + 0.1 * np.sin(i))
            amp = 0.4 * (1.0 + 0.1 * i)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
        
        # Cross-dimensional coupling with adaptive weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.2 * (1.0 + 0.05 * (i + j))
                result += weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Radial component with adaptive scaling
        if self.dim >= 2:
            r = np.sqrt(np.sum(x**2))
            result += 0.5 * np.sin(5.0 * r) * np.exp(-0.2 * r) * (1.0 + 0.1 * r**2)
        
        # Asymmetric penalty terms
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.25 * np.exp(-0.3 * x[i]) * (1.0 + 0.1 * x[i]**3)
            else:
                result += 0.2 * np.exp(-0.4 * abs(x[i])) * (1.0 + 0.15 * x[i]**3)
        
        # High-frequency oscillatory term
        for i in range(self.dim):
            result += 0.15 * np.sin(50.0 * x[i]) * np.cos(45.0 * x[i])
        
        # Global modulation based on dimensionality
        result *= (1.0 + 0.1 * self.dim)
        
        return result