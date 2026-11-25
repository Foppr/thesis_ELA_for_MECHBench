import numpy as np

class FractalChaoticCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like chaotic sequence for dynamic scaling
        self.fractal_sequence = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Fractal-like chaotic component with varying exponents
        f2 = 0.0
        for i in range(self.dim):
            exp = 2.0 + 1.5 * self.fractal_sequence[i]  # Dynamic exponent modulation
            f2 += np.sin(x[i] ** exp) * np.cos(x[i])
        
        # Cross-dimensional coupling with fractal weights
        f3 = 0.0
        for i in range(self.dim - 1):
            weight = np.abs(np.sin((i + 1) * np.pi / (self.dim + 1)))  # Fractal weight
            f3 += weight * np.sin(x[i] * x[i+1])
        
        # Sine-cosine coupled harmonic oscillation
        f4 = 0.3 * np.sum(np.sin(x) * np.cos(2.0 * x) * np.exp(-x**2 / 20.0))
        
        # Multi-scale chaotic modulation with dynamic frequency
        f5 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(x[i] * 0.3)  # Frequency modulation
            f5 += np.cos(freq * x[i]) * np.sin(freq * x[i]**2)
        
        # Polynomial chaos with fractal-like behavior
        f6 = 0.4 * np.sum(x**4 * np.sin(1.5 * x) * np.cos(0.5 * x))
        
        # Hyperbolic tangent coupling with exponential decay
        f7 = 0.2 * np.sum(np.tanh(x) * np.exp(-x**2 / 10.0))
        
        # Complex fractal coupling with cubic interactions
        f8 = 0.0
        for i in range(self.dim - 2):
            f8 += np.sin(x[i] * x[i+1] * x[i+2]) * np.cos(0.5 * x[i])
        f8 *= 0.3
        
        # Dynamic coupling with modified chaotic sequence
        f9 = 0.0
        for i in range(self.dim - 1):
            freq_mod = 1.0 + 0.7 * self.fractal_sequence[i] * np.cos(x[i])
            f9 += np.sin(freq_mod * x[i]) * np.cos(x[i+1])
        
        # Sigmoidal scaling with chaotic modulation
        f10 = 0.25 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.sin(x))
        
        # Higher-order polynomial with trigonometric modulation
        f11 = 0.3 * np.sum(x**6 * np.cos(1.2 * x) * np.sin(0.8 * x))
        
        # Additional chaotic interaction with cubic roots
        f12 = 0.15 * np.sum(np.cbrt(x) * np.sin(x**2) * np.cos(x))
        
        # Multi-fractal coupling with dynamic weights
        f13 = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-i / (self.dim + 2)) * np.sin(i * np.pi / (self.dim + 1))
            f13 += weight * np.sin(x[i] * x[i+1])
        
        # Combined scaling based on dimensionality
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Final function value with all components
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13)