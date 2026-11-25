import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Sinusoidal modulation with dynamic frequencies and amplitudes
        for i in range(self.dim):
            freq = 1.5 + 2.0 * np.sin(0.4 * i)
            amp = 0.8 + 1.2 * np.cos(0.3 * i)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Polynomial chaos component with modified terms
        for i in range(self.dim):
            poly_term = (x[i]**4 + 0.7 * x[i]**3 + 0.5 * x[i]**2 + 0.2 * x[i] + 0.1)
            result += 0.9 * poly_term * np.sin(1.5 * x[i])
            
        # Cross-dimensional interaction with altered coupling weights
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.8 + 0.7 * np.sin(0.3 * (i + j))
                coupling_sum += weight * x[i] * x[j]
            result += 0.8 * coupling_sum
            
        # Dynamic conditioning based on dimensionality
        cond_factor = 1.0 + 0.5 * np.sin(0.6 * self.dim)
        result *= cond_factor
        
        # Multi-scale chaotic modulation with varying periods
        for i in range(self.dim):
            mod_term = 0.0
            for k in range(1, 7):
                period = 1.5 + 0.8 * np.sin(0.4 * k)
                mod_term += np.sin(period * x[i]) * np.cos(period * x[i])
            result += 1.0 * mod_term
            
        # Fractal-like recursive interaction with modified coefficients
        for i in range(self.dim):
            recursive_sum = 0.0
            for j in range(1, min(4, self.dim)):
                coeff = 0.9 + 0.3 * np.sin(0.3 * (i + j))
                recursive_sum += coeff * np.sin(2.5 * x[i] + 0.6 * x[j])
            result += 0.6 * recursive_sum
            
        # Memory-based chaotic component
        if self.dim > 1:
            memory_sum = 0.0
            for i in range(self.dim - 1):
                memory_sum += (x[i] * x[i+1]) * np.sin(0.7 * (i + 1))
            result += 0.5 * memory_sum
            
        # High-frequency oscillatory component
        for i in range(self.dim):
            result += 0.4 * np.sin(9.0 * x[i]) * np.cos(9.0 * x[i])
            
        # Adaptive scaling factor based on input magnitude
        scale = 1.0 + 0.3 * np.mean(np.abs(x))
        result *= scale
        
        return result