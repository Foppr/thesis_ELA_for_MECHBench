import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute dimension-dependent parameters for scaling
        self.scaling_factors = np.logspace(0, 1, dim, base=2)
        self.frequency_modulators = np.sin(np.linspace(0, np.pi, dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base exponential decay term
        f1 = np.sum(np.exp(-x**2 / 10.0))
        
        # Trigonometric coupling with varying frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 3.0 * self.frequency_modulators[i]
            f2 += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        f2 *= 0.5
        
        # Power-law scaling with exponential interactions
        f3 = 0.0
        for i in range(self.dim):
            f3 += self.scaling_factors[i] * (x[i]**3) * np.exp(-x[i]**2 / 5.0)
        f3 *= 0.3
        
        # Cross-dimensional exponential coupling
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += np.exp(-np.abs(x[i] - x[i+1]) / 2.0) * np.sin(x[i] * x[i+1])
        f4 *= 0.4
        
        # Nested harmonic oscillations with adaptive amplitudes
        f5 = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i / (self.dim + 1) * np.pi)
            f5 += amp * np.cos(2.0 * x[i]) * np.sin(3.0 * x[i])
        f5 *= 0.2
        
        # Fractional polynomial with sinusoidal modulation
        f6 = 0.0
        for i in range(self.dim):
            f6 += (x[i]**1.5) * np.sin(x[i] / 2.0)
        f6 *= 0.3
        
        # Gaussian-like radial basis with multi-scale interactions
        f7 = 0.0
        for i in range(self.dim):
            f7 -= np.exp(-((x[i] - 1.0)**2 + (x[i] + 1.0)**2) / 4.0)
        f7 *= 0.5
        
        # Adaptive conditioning through dimension-wise scaling
        f8 = 0.0
        for i in range(self.dim):
            f8 += self.scaling_factors[i] * np.sin(x[i] / (i + 1))
        f8 *= 0.2
        
        # Higher-order trigonometric coupling
        f9 = 0.0
        for i in range(self.dim - 2):
            f9 += np.sin(x[i]) * np.cos(x[i+1]) * np.sin(x[i+2])
        f9 *= 0.3
        
        # Combined function with dimension-dependent scaling
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9)