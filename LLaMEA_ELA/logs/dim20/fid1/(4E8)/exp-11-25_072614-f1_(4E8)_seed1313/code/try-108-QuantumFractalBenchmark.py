import numpy as np

class QuantumFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like hierarchical structure with recursive cosine components
        fractal_term = np.sum(np.cos(2.0**np.arange(1, self.dim + 1) * x) * np.exp(-x**2 / 20.0)) / self.dim
        
        # Quantum interference pattern with complex amplitude modulation
        quantum_term = np.sum(np.sin(x * np.pi / 3.0) * np.cos(x * np.pi / 5.0) * np.exp(-np.abs(x) / 5.0)) / self.dim
        
        # Adaptive ridge complexity with dimension-dependent polynomial exponents
        ridge_term = np.sum(x**4 * np.sin(x)**2 + x**6 * np.cos(x)**2 - x**3 * np.tan(x/4.0)) / (self.dim * 25.0)
        
        # Multi-scale oscillation with varying frequencies and decay rates
        multi_scale_term = np.sum(np.sin(10.0 * x) * np.exp(-x**2 / 15.0) + np.cos(7.0 * x) * np.exp(-x**2 / 10.0)) / self.dim
        
        # Entropy-based complexity with logarithmic scaling
        entropy_term = np.sum(np.log(1.0 + np.abs(x)) * np.sin(x * 2.0) * np.cos(x * 1.5)) / (self.dim * 8.0)
        
        # Dimensional coupling with cross-term interactions
        coupling_term = np.sum((x[:-1] - x[1:]) ** 2 * np.exp(-np.abs(x[:-1] + x[1:]) / 3.0)) / (self.dim - 1) if self.dim > 1 else 0
        
        # Chaos-enhanced saddle structure with fractional Brownian motion inspired components
        chaos_term = np.sum(np.sin(x * 3.0) * np.cos(x * 0.5) * np.log(2.0 + np.abs(x))) / (self.dim * 6.0)
        
        # Combined weighted landscape with adaptive scaling
        total = 0.22 * fractal_term + 0.18 * quantum_term + 0.25 * ridge_term + 0.15 * multi_scale_term + 0.10 * entropy_term + 0.07 * coupling_term + 0.03 * chaos_term
        
        return total