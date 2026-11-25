import numpy as np

class SinusoidalPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced sinusoidal wave components with stronger chaotic modulation
        for i in range(self.dim):
            freq = 3 * (i + 1) + 0.8 * np.sin(0.4 * i)
            amp = 2.0 + 0.7 * np.cos(0.5 * i)
            wave = amp * np.sin(freq * x[i]) * np.exp(-0.15 * x[i]**2)
            result += 0.4 * wave**2
        
        # Modified polynomial interactions with higher-order terms
        for i in range(self.dim - 1):
            poly_term = (x[i]**4 + x[i+1]**4) * np.cos(3 * (x[i] - x[i+1]))
            result += 0.3 * poly_term
        
        # Enhanced cross-dimensional harmonic coupling with stronger chaotic phase shifts
        for i in range(self.dim - 2):
            phase_shift = 0.2 * np.sin(0.6 * i) + 0.1 * np.cos(0.4 * i)
            coupling = np.sin(4 * (x[i] + x[i+1]) + phase_shift) * np.cos(5 * (x[i+1] - x[i+2]))
            result += 0.2 * coupling
        
        # Improved asymmetric basin structure with stronger nonlinearity
        for i in range(self.dim):
            asym_term = x[i]**6 * np.sin(0.6 * x[i]) + 0.6 * x[i]**5 * np.cos(0.4 * x[i])
            result += 0.3 * asym_term
        
        # Multi-scale oscillatory behavior with increased complexity
        for i in range(self.dim):
            scale = 1.2 + 0.4 * np.sin(0.3 * i)
            oscillation = np.sin(12 * x[i]) * np.cos(10 * x[i]) * scale
            result += 0.15 * oscillation**2
        
        # Enhanced chaotic conditioning factor with stronger gradient influence
        grad_factor = 1.0 + 0.6 * np.sin(np.log(np.sum(np.abs(x)) + 1) + 0.3 * np.cos(self.dim))
        result *= grad_factor
        
        # Modified fractal-like scaling with more pronounced chaotic modulation
        fractal_scale = 1.0 + 0.3 * np.cos(np.log(self.dim + 4) + 0.2 * np.sin(self.dim))
        result *= fractal_scale
        
        # Improved noise term for better robustness testing
        noise = 0.08 * np.random.rand() * (1.0 + 0.2 * np.sin(np.log(self.dim + 3)))
        result += noise
        
        # Enhanced normalization by dimensionality
        result /= self.dim
        
        return result