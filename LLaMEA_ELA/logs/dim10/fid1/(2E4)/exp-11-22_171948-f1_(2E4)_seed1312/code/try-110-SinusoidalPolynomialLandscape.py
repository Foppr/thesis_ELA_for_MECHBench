import numpy as np

class SinusoidalPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Sinusoidal wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2 * (i + 1) + 0.5 * np.sin(0.3 * i)
            amp = 1.5 + 0.5 * np.cos(0.4 * i)
            wave = amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
            result += 0.3 * wave**2
        
        # Polynomial interactions between dimensions
        for i in range(self.dim - 1):
            poly_term = (x[i]**3 + x[i+1]**3) * np.cos(2 * (x[i] - x[i+1]))
            result += 0.2 * poly_term
        
        # Cross-dimensional harmonic coupling with chaotic phase shifts
        for i in range(self.dim - 2):
            phase_shift = 0.1 * np.sin(0.5 * i) + 0.05 * np.cos(0.3 * i)
            coupling = np.sin(3 * (x[i] + x[i+1]) + phase_shift) * np.cos(4 * (x[i+1] - x[i+2]))
            result += 0.15 * coupling
        
        # Asymmetric basin structure with polynomial and exponential components
        for i in range(self.dim):
            asym_term = x[i]**5 * np.sin(0.5 * x[i]) + 0.5 * x[i]**4 * np.cos(0.3 * x[i])
            result += 0.25 * asym_term
        
        # Multi-scale oscillatory behavior with varying amplitudes
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.2 * i)
            oscillation = np.sin(10 * x[i]) * np.cos(8 * x[i]) * scale
            result += 0.1 * oscillation**2
        
        # Chaotic conditioning factor based on local gradient information
        grad_factor = 1.0 + 0.4 * np.sin(np.log(np.sum(np.abs(x)) + 1))
        result *= grad_factor
        
        # Fractal-like scaling with chaotic modulation
        fractal_scale = 1.0 + 0.2 * np.cos(np.log(self.dim + 3) + 0.1 * np.sin(self.dim))
        result *= fractal_scale
        
        # Add noise term for robustness testing
        noise = 0.05 * np.random.rand() * (1.0 + 0.1 * np.sin(np.log(self.dim + 2)))
        result += noise
        
        # Normalize by dimensionality
        result /= self.dim
        
        return result