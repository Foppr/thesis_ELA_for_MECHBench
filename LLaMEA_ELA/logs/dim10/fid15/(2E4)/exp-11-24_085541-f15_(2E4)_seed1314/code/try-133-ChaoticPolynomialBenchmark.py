import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with chaotic modulation
        result = np.sum(x**4) * 0.05
        
        # Chaotic sinusoidal components with dynamic frequencies
        chaos_sum = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(0.5 * i + 1.0) * np.cos(0.3 * i + 0.5)
            amp = 1.2 + 0.4 * np.sin(0.4 * i + 0.7)
            chaos_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.8)
        result += 2.0 * chaos_sum
        
        # Polynomial chaos expansion with varying degrees
        poly_sum = 0.0
        for i in range(self.dim):
            deg = 2 + int(3 * np.sin(0.6 * i) ** 2)
            coeff = 0.8 + 0.4 * np.cos(0.5 * i)
            poly_sum += coeff * x[i]**deg
        result += 1.5 * poly_sum
        
        # Dynamic conditioning with time-like parameter
        cond_sum = 0.0
        for i in range(self.dim):
            t_param = 0.5 + 0.5 * np.sin(0.3 * i + 1.2)
            cond_factor = 1.0 + 0.6 * np.sin(0.7 * i + 0.9) * t_param
            cond_sum += cond_factor * x[i]**3
        result += 1.0 * cond_sum
        
        # Cross-dimensional coupling with chaotic interaction strengths
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                strength = 0.5 + 0.3 * np.sin(0.2 * (i + j) + 0.8)
                cross_sum += strength * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        result += 1.8 * cross_sum
        
        # Fractal-like recursive structure with exponential decay
        fractal_sum = 0.0
        for i in range(self.dim):
            val = x[i]
            for k in range(1, 5):
                decay = np.exp(-0.2 * k)
                fractal_sum += decay * (val**(2*k) + 0.3 * np.sin(k * val))
                val = np.cos(val)
        result += 0.7 * fractal_sum
        
        # Memory effect with weighted dimension interactions
        if self.dim > 1:
            mem_sum = 0.0
            for i in range(1, self.dim):
                weight = 0.6 + 0.4 * np.cos(0.4 * i + 0.3)
                mem_sum += weight * x[i-1] * x[i] * np.sin(x[i-1] + x[i])
            result += 1.2 * mem_sum
            
        # Exponential modulation with chaotic parameters
        exp_mod = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.3 * i + 0.6)
            freq = 0.8 + 0.2 * np.cos(0.4 * i + 0.9)
            exp_mod += amp * np.exp(-freq * np.abs(x[i])) * np.cos(1.2 * x[i])
        result += 1.4 * exp_mod
        
        return result