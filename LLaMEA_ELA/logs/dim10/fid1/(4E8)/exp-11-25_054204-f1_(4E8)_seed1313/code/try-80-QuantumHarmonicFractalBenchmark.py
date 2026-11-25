import numpy as np

class QuantumHarmonicFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quantum harmonic frequencies and fractal scaling factors
        self.frequencies = np.sqrt(np.arange(1, dim + 1) * 0.5)
        self.fractal_factors = np.power(0.7, np.arange(dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component
        f1 = 0.5 * np.sum(self.frequencies * (x**2 + 1.0 / self.frequencies**2))
        
        # Adaptive neural network-like coupling with fractal weights
        f2 = 0.0
        for i in range(self.dim):
            weight = self.fractal_factors[i] * (1.0 + 0.3 * np.sin(x[i]))
            f2 += weight * np.sin(2.0 * x[i]) * np.cos(x[i])
        
        # Fractal-based dimension coupling with recursive scaling
        f3 = 0.0
        for i in range(self.dim):
            scaled_x = x[i] * (1.0 + 0.1 * np.sin(np.sum(x[:i+1])))
            f3 += np.sin(scaled_x) * np.cos(3.0 * scaled_x)
        
        # Rugged terrain with multiple local minima
        f4 = 0.2 * np.sum(np.abs(x) * np.sin(10.0 * x))
        
        # Nonlinear energy landscape with exponential decay
        f5 = 0.15 * np.sum(np.exp(-x**2 / 5.0) * (x**4 - 2.0 * x**2 + 1.0))
        
        # Cross-dimensional quantum entanglement terms
        f6 = 0.0
        for i in range(self.dim - 1):
            f6 += np.sin(x[i] * x[i+1]) * (i + 1) * np.cos(0.5 * (x[i]**2 + x[i+1]**2))
        
        # Multi-scale oscillatory pattern with dynamic amplitude
        f7 = 0.1 * np.sum(np.sin(5.0 * x) * np.cos(2.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Combined fractal scaling factor based on dimensionality
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7)