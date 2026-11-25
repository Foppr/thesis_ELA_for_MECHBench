import numpy as np

class RadialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial weights and chaotic multipliers
        self.radial_weights = np.linspace(0.5, 2.0, dim)
        self.chaotic_multipliers = 1.0 + 0.5 * np.sin(np.arange(dim) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial quadratic component
        r2 = np.sum(x**2)
        f1 = 0.5 * r2
        
        # Sinusoidal radial oscillation with chaotic modulation
        f2 = 0.3 * np.sin(3.0 * np.sqrt(r2)) * np.cos(2.0 * np.sqrt(r2))
        
        # Polynomial chaos with adaptive exponents
        f3 = 0.2 * np.sum((x**4) * np.cos(1.5 * x) * self.chaotic_multipliers)
        
        # Cross-dimensional interaction with radial coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) / (1.0 + abs(x[i] - x[j]))
        f4 = 0.25 * cross_term
        
        # Radial harmonic with variable frequency
        freq = 2.0 + 1.5 * np.cos(r2 / 10.0)
        f5 = 0.18 * np.sum(np.sin(freq * x) * np.cos(3.0 * x))
        
        # Adaptive scaling based on dimensionality and position
        scale = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.abs(np.mean(x))
        f6 = 0.22 * np.sum(np.exp(-x**2 / 5.0) * x**3)
        
        # Fractal-like coupling with multi-scale interactions
        f7 = 0.15 * np.sum(np.sin(4.0 * x) * np.cos(5.0 * x) * np.tanh(x))
        
        # Multi-modal component with chaotic peaks
        f8 = 0.2 * np.sum(np.sin(6.0 * x) * np.cos(7.0 * x) * np.exp(-x**2 / 8.0))
        
        # Sigmoidal radial modulation
        f9 = 0.1 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.sin(2.0 * x))
        
        # Higher-order polynomial with sinusoidal modulation
        f10 = 0.12 * np.sum((x**5) * np.cos(2.0 * x))
        
        # Complex radial coupling with exponential decay
        f11 = 0.18 * np.sum(np.exp(-r2 / 20.0) * np.sin(x)**2)
        
        # Final combined function
        return scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)