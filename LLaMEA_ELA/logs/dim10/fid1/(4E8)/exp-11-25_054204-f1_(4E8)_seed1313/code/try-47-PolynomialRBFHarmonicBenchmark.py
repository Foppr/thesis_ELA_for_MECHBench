import numpy as np

class PolynomialRBFHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Radial Basis Function component with Gaussian peaks
        centers = np.linspace(-5, 5, self.dim)
        rbfs = []
        for i in range(self.dim):
            rbfs.append(np.exp(-0.5 * (x - centers[i])**2 / 1.0))
        f2 = -np.sum(rbfs)
        
        # Polynomial chaos expansion with mixed monomials
        f3 = 0.5 * np.sum(x**3) + 0.1 * np.sum(x**4)
        
        # Harmonic oscillation modulated by gradient magnitude
        grad_magnitude = np.sqrt(np.sum(np.gradient(x)**2))
        f4 = 2.0 * np.sin(grad_magnitude) * np.cos(2.0 * np.sum(x))
        
        # Cross-dimension interaction with sine coupling
        cross_term = 0.3 * np.sum(np.sin(x[:-1] * x[1:]))
        
        # Nonlinear correlation term
        f5 = 0.05 * np.sum((x**2) * np.sin(x))
        
        # Additional high-frequency oscillation component
        f6 = 1.5 * np.sum(np.sin(5.0 * x) * np.cos(3.0 * x))
        
        # Cross-dimensional polynomial coupling with higher order terms
        poly_coupling = 0.2 * np.sum(x**5) + 0.1 * np.sum(x**6)
        
        # Gradient-dependent harmonic modulation with multiple frequencies
        grad_mod = np.sin(np.sum(x)**2) * np.cos(3.0 * grad_magnitude)
        
        # Multi-scale RBF with varying widths and amplitudes
        rbf_multi = 0.8 * np.sum(np.exp(-0.1 * (x - 2.0)**2) + np.exp(-0.3 * (x + 2.0)**2))
        
        return f1 + f2 + f3 + f4 + cross_term + f5 + f6 + poly_coupling + grad_mod + rbf_multi