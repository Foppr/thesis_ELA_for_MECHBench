import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency factors for sinusoidal components
        self.freq_factors = np.sqrt(np.arange(1, dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Sinusoidal oscillations with varying frequencies
        f2 = 0.5 * np.sum(np.sin(self.freq_factors * x) * np.cos(self.freq_factors * x))
        
        # Radial basis function component with adaptive scaling
        f3 = 0.3 * np.sum(np.exp(-0.1 * (x**2)) * np.sin(2.0 * x))
        
        # Cross-dimensional coupling with radial dependence
        cross_term = 0.0
        for i in range(self.dim - 1):
            r = np.sqrt(x[i]**2 + x[i+1]**2)
            cross_term += np.sin(r) * np.cos(x[i] * x[i+1])
        f4 = 0.25 * cross_term
        
        # Adaptive polynomial chaos with trigonometric modulation
        f5 = 0.4 * np.sum((x**3) * np.sin(1.5 * x))
        
        # Multi-scale sinusoidal component
        f6 = 0.35 * np.sum(np.sin(x / 2.0) * np.cos(x / 3.0))
        
        # Sigmoidal radial component
        f7 = 0.2 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.sin(x**2))
        
        # Higher-order harmonic with exponential decay
        f8 = 0.15 * np.sum(np.sin(3.0 * x) * np.exp(-x**2 / 10.0))
        
        # Fractal-like coupling with recursive structure
        fractal_term = 0.0
        for i in range(self.dim - 2):
            fractal_term += np.sin(x[i] * x[i+1] * x[i+2]) / (i + 1)
        f9 = 0.18 * fractal_term
        
        # Modified radial basis with inverse scaling
        f10 = 0.22 * np.sum(np.exp(-x**2) / (1.0 + np.abs(x)))
        
        # Complex cross-dimensional interaction
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += np.sin((x[i] - x[j])**2) * np.cos(x[i] * x[j])
        f11 = 0.12 * interaction
        
        # Adaptive frequency modulation based on dimension
        freq_mod = 1.0 + 0.3 * np.sin(np.sum(x**2) / (self.dim + 1))
        f12 = 0.25 * np.sum(np.sin(freq_mod * x) * np.cos(freq_mod * x))
        
        # Polynomial chaos with cosine modulation
        f13 = 0.18 * np.sum((x**4) * np.cos(2.0 * x))
        
        # Combined scaling factor
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Final function value with adjusted weights
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13)