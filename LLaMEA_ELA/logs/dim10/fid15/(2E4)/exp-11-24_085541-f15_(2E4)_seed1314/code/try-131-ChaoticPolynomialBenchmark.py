import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        result = np.sum(x**2) * (1.0 + 0.1 * np.sin(0.5 * self.dim))
        
        # Enhanced sinusoidal modulation with chaotic frequency variations
        for i in range(self.dim):
            freq = 2.0 + 2.0 * np.sin(0.3 * i + 0.1 * self.dim)
            amp = 1.0 + 0.5 * np.cos(0.4 * i + 0.2 * self.dim)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Polynomial chaos component with higher-order terms and dynamic coefficients
        for i in range(self.dim):
            poly_term = (x[i]**4 + 0.6 * x[i]**3 + 0.4 * x[i]**2 + 0.2 * x[i] + 0.1)
            result += 0.8 * poly_term * np.sin(1.5 * x[i])
            
        # Stronger cross-dimensional interaction with varying coupling weights
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(i+1, min(i+5, self.dim)):
                weight = 1.5 + 0.8 * np.sin(0.2 * (i + j) + 0.3 * self.dim)
                coupling_sum += weight * x[i] * x[j]
            result += 0.7 * coupling_sum
            
        # Enhanced dynamic conditioning with multi-scale factors
        cond_factor = 1.0 + 0.4 * np.sin(0.5 * self.dim) * np.cos(0.3 * self.dim)
        result *= cond_factor
        
        # Multi-scale chaotic modulation with fractal-like behavior
        for i in range(self.dim):
            mod_term = 0.0
            for k in range(1, 8):
                period = 1.5 + 0.8 * np.sin(0.3 * k + 0.1 * self.dim)
                mod_term += np.sin(period * x[i]) * np.cos(period * x[i])
            result += 1.0 * mod_term
            
        # Recursive interaction with enhanced non-separability
        for i in range(self.dim):
            recursive_sum = 0.0
            for j in range(1, min(6, self.dim)):
                coeff = 0.9 + 0.3 * np.sin(0.2 * (i + j) + 0.1 * self.dim)
                recursive_sum += coeff * np.sin(2.5 * x[i] + 0.4 * x[j])
            result += 0.6 * recursive_sum
            
        # Memory-based chaotic component with enhanced coupling
        if self.dim > 1:
            memory_sum = 0.0
            for i in range(self.dim - 1):
                memory_sum += (x[i] * x[i+1]) * np.sin(0.7 * (i + 1) + 0.2 * self.dim)
            result += 0.5 * memory_sum
            
        # High-frequency oscillatory component with varying amplitudes
        for i in range(self.dim):
            result += 0.4 * np.sin(10.0 * x[i]) * np.cos(10.0 * x[i])
            
        # Adaptive scaling factor based on input magnitude and dimensionality
        scale = 1.0 + 0.3 * np.mean(np.abs(x)) * (1.0 + 0.2 * np.sin(0.4 * self.dim))
        result *= scale
        
        return result