import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Polynomial chaos term with varying exponents
        f1 = np.sum(np.abs(x_norm)**(3 + np.sin(x_norm * 20)))
        
        # Logarithmic barrier terms with multiple singularities
        f2 = np.sum(-np.log(1e-6 + np.abs(x_norm)) * np.exp(-x_norm**2))
        
        # Scale-invariant cosine modulations creating fractal-like structure
        f3 = np.sum(np.cos(50 * np.log(np.abs(x_norm) + 1e-6)) * np.exp(-0.5 * x_norm**2))
        
        # Multi-scale sine waves with exponentially increasing frequencies
        f4 = np.sum(np.sin(2**(np.floor(np.log2(np.abs(x_norm) + 1e-6))) * x_norm)**3)
        
        # Asymmetric Gaussian-like repulsion with fractal scaling
        f5 = np.sum(np.exp(-0.5 * (x_norm / (1 + np.abs(x_norm)))**2) * (1 + np.sin(10 * x_norm)))
        
        # Cross-dimensional coupling with recursive scaling
        f6 = 0.3 * np.sum(np.cos(17 * (x_norm[:-1] * x_norm[1:] + 0.1))**5)
        
        # Nested oscillatory patterns with varying amplitudes
        f7 = 0.2 * np.sum(np.sin(47 * x_norm) * np.cos(31 * x_norm)**2 + 0.5 * np.sin(63 * x_norm))
        
        # Non-smooth chaotic component with piecewise linear transformation
        f8 = 0.15 * np.sum(np.abs(x_norm - np.floor(x_norm + 0.5))**0.7)
        
        return f1 + 0.4 * f2 + 0.3 * f3 + 0.2 * f4 + 0.15 * f5 + 0.1 * f6 + 0.08 * f7 + 0.05 * f8