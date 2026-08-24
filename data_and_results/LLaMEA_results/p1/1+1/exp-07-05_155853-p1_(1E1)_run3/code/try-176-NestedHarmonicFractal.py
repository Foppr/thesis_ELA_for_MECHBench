import numpy as np

class NestedHarmonicFractal:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested harmonic oscillators with fractal frequency scaling
        harmonic_sum = 0
        for i in range(self.dim):
            # Fractal-like frequency modulation based on dimension index
            freq = 1.0 + 0.5 * np.sin(i * 0.3) + 0.3 * np.cos(i * 0.7) + 0.2 * np.sin(i * 0.1)
            # Nested harmonic components
            harmonic_sum += (np.sin(freq * x[i]) + 0.5 * np.sin(2 * freq * x[i]) + 
                           0.3 * np.sin(3 * freq * x[i]) + 0.1 * np.sin(4 * freq * x[i]))
        
        # Adaptive coupling terms with dimension-dependent strengths
        coupling_sum = 0
        for i in range(self.dim - 1):
            # Adaptive coupling strength based on position and dimension
            coupling_strength = 0.5 + 0.5 * np.sin(i * 0.4 + np.sum(x[:i+1]) * 0.1)
            coupling_sum += coupling_strength * np.sin(x[i] + x[i+1]) * np.cos(x[i] - x[i+1])
        
        # Fractal-like polynomial terms with self-similar scaling
        poly_sum = 0
        for i in range(self.dim):
            # Self-similar scaling factor
            scale = 0.1 + 0.9 * np.abs(np.sin(i * 0.2))
            poly_sum += scale * (x[i]**4 + 0.5 * x[i]**3 + 0.2 * x[i]**2 + 0.1 * x[i])
        
        # Multi-scale oscillation with chaotic phase shifts
        phase_sum = 0
        for i in range(self.dim):
            # Chaotic phase shift based on previous dimensions
            phase_shift = np.sum(x[:i]) * 0.3 + 0.2 * np.sin(i * 0.5)
            phase_sum += np.sin(x[i] + phase_shift) * np.cos(x[i] * 2 + phase_shift * 0.5)
        
        # Cross-dimensional interaction with fractal coupling weights
        cross_sum = 0
        for i in range(0, self.dim - 2, 3):
            if i + 2 < self.dim:
                weight = 0.3 + 0.7 * np.abs(np.sin(i * 0.6))
                cross_sum += weight * (x[i] * x[i+1] * x[i+2])**1.5
        
        # Global scaling with nested fractal modulation
        global_mod = np.sin(0.1 * np.sum(x**2)) * np.cos(0.05 * np.sum(x)) * np.sin(0.02 * np.sum(x**3))
        
        # Combined fitness with refined weights
        return (1.5 * harmonic_sum + 0.8 * coupling_sum + 0.6 * poly_sum + 
                0.4 * phase_sum + 0.3 * cross_sum + 0.2 * global_mod)