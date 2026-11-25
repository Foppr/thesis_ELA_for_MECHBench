import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial harmonic potential
        r_squared = np.sum(x**2)
        result = 0.3 * r_squared * np.exp(-0.05 * r_squared)
        
        # Chaotic sine wave components with varying frequencies and amplitudes
        chaos_sum = 0
        for i in range(self.dim):
            freq = 2**(i % 5 + 1)
            amp = 1.5 + 0.5 * np.sin(0.7 * i)
            chaos_sum += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3) * np.tan(freq * x[i] * 0.1)
        result += 2.0 * chaos_sum
        
        # Adaptive conditioning based on dimension
        cond_factor = 1.0
        for i in range(self.dim):
            cond_factor *= (1 + 0.1 * np.abs(x[i]) * np.sin(3 * x[i]))
        result *= cond_factor
        
        # Multi-scale radial basis functions with chaotic centers
        rb_sum = 0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.5 * i) + 1.0 * np.cos(0.3 * i)
            width = 0.5 + 0.3 * np.sin(0.4 * i)
            rb_sum += 1.2 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        result += 1.5 * rb_sum
        
        # Nested optima with varying depths
        nested_term = 0
        for i in range(self.dim):
            nested_term += 0.8 * np.sin(4 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.1 * (x[i] - 1.5)**2)
        result += 1.0 * nested_term
        
        # Cross-dimensional coupling with dynamic weights
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.5 + 0.3 * np.sin(2 * (x[i] + x[j]))
                coupling_sum += weight * np.sin(6 * x[i]) * np.cos(5 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        result += 0.8 * coupling_sum
        
        # Fractal-like structure with recursive harmonic components
        fractal_term = 0
        for i in range(self.dim):
            term = np.sin(10 * x[i]) + 0.5 * np.cos(15 * x[i]) + 0.3 * np.sin(25 * x[i])
            fractal_term += term * np.exp(-0.2 * x[i]**2)
        result += 1.2 * fractal_term
        
        # Asymmetric harmonic penalties
        penalty_sum = 0
        for i in range(self.dim):
            if x[i] < 0:
                penalty_sum += 1.8 * np.sin(7 * x[i]) * np.exp(-0.3 * (x[i] + 5.0)**2)
            else:
                penalty_sum += 1.4 * np.cos(9 * x[i]) * np.exp(-0.4 * (x[i] - 5.0)**2)
        result += 0.6 * penalty_sum
        
        # Global modulation with time-like parameter
        t = np.sum(x) / self.dim
        result *= (1 + 0.3 * np.sin(8 * t) * np.cos(6 * t))
        
        return result