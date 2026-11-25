import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute scaling factors for power-law behavior
        self.scaling_factors = np.power(np.arange(1, dim + 1), 1.5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base exponential decay term
        f1 = np.sum(np.exp(-0.5 * x**2))
        
        # Trigonometric coupling with varying frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(i * 0.7)  # Varying frequency per dimension
            f2 += np.cos(freq * x[i]) * np.sin(freq * x[i])
        
        # Power-law weighted interactions
        f3 = 0.5 * np.sum(self.scaling_factors * (x**3) * np.sin(x))
        
        # Cross-dimensional exponential coupling
        cross_exp = 0.0
        for i in range(self.dim - 1):
            cross_exp += np.exp(-0.1 * (x[i] - x[i+1])**2)
        f4 = 0.3 * cross_exp
        
        # Sine-cosine hybrid with dynamic amplitude
        f5 = 0.4 * np.sum(np.sin(x) * np.cos(2.0 * x) * (1.0 + 0.2 * np.abs(x)))
        
        # Polynomial with logarithmic scaling
        f6 = 0.2 * np.sum((x**4) * np.log(1.0 + np.abs(x)))
        
        # Gaussian-like peaks with varying heights
        f7 = 0.3 * np.sum(np.exp(-0.5 * (x - 1.0)**2) + np.exp(-0.5 * (x + 1.0)**2))
        
        # Fractional power interactions
        f8 = 0.25 * np.sum(np.abs(x)**1.3 * np.sin(3.0 * x))
        
        # Multi-scale harmonic components
        f9 = 0.15 * np.sum(np.sin(0.5 * x) + np.cos(0.3 * x) + np.sin(0.7 * x))
        
        # Modified sigmoidal scaling with trigonometric modulation
        f10 = 0.2 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.cos(1.5 * x))
        
        # Combined scaling factor based on dimensionality
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Final function value with adjusted weights
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)