import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2) * 0.1
        
        # Radial basis function components with varying widths and centers
        rbf_sum = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.5 * i)
            width = 0.5 + 0.3 * np.cos(0.3 * i)
            rbf_sum += np.exp(-width * (x[i] - center)**2) * np.sin(2.0 * x[i])
        result += 2.0 * rbf_sum
        
        # Multi-scale sinusoidal oscillations with adaptive frequencies
        sin_sum = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.4 * i)
            amp = 1.5 + 0.5 * np.cos(0.3 * i)
            sin_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        result += 1.2 * sin_sum
        
        # Adaptive conditioning based on dimension index
        cond_sum = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.8 * np.sin(0.6 * i) + 0.4 * np.cos(0.4 * i)
            cond_sum += cond_factor * x[i]**4
        result += 0.8 * cond_sum
        
        # Cross-dimensional coupling with modified interaction strengths
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                strength = 0.7 + 0.3 * np.sin(0.2 * (i + j))  # Increased strength variability
                cross_sum += strength * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        result += 1.8 * cross_sum  # Increased weight
        
        # Fractal-like self-similarity through recursive polynomial terms with higher exponents
        poly_sum = 0.0
        for i in range(self.dim):
            val = x[i]
            for k in range(2, 5):  # Changed from 1 to 2, and 4 to 5
                poly_sum += (0.3 + 0.1 * np.sin(0.2 * i * k)) * val**(2*k)
                val = np.sin(val)
        result += 0.7 * poly_sum  # Slightly increased weight
        
        # Memory effect through weighted sum of previous dimensions
        if self.dim > 1:
            mem_sum = 0.0
            for i in range(1, self.dim):
                weight = 0.7 + 0.3 * np.sin(0.5 * i)
                mem_sum += weight * x[i-1] * x[i]
            result += 0.9 * mem_sum
            
        # Exponential modulation with adaptive parameters
        exp_mod = 0.0
        for i in range(self.dim):
            amp = 1.2 + 0.4 * np.cos(0.3 * i)
            freq = 0.8 + 0.2 * np.sin(0.4 * i)
            exp_mod += amp * np.exp(-freq * np.abs(x[i])) * np.sin(1.5 * x[i])
        result += 1.3 * exp_mod
        
        return result