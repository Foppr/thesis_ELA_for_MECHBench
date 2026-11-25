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
        
        # Enhanced cross-dimension interaction with cosine coupling
        cross_term = 0.5 * np.sum(np.cos(x[:-1] * x[1:]))
        
        # Nonlinear correlation term with enhanced sensitivity
        f5 = 0.1 * np.sum((x**2) * np.sin(x))
        
        # Additional cubic interaction terms for increased complexity
        f6 = 0.05 * np.sum(x**3 * np.cos(x))
        
        # Mixed polynomial and trigonometric coupling
        f7 = 0.2 * np.sum(np.sin(x) * x**2)
        
        # Novel perturbation term with chaotic sine modulation
        f8 = 0.3 * np.sum(np.sin(3.0 * x + np.sin(2.0 * x)))
        
        # Adaptive scaling factor based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # High-frequency oscillation component for increased complexity
        f9 = 0.4 * np.sum(np.sin(5.0 * x) * np.cos(3.0 * x))
        
        # Cross-dimensional coupling with exponential decay
        exp_coupling = 0.2 * np.sum(np.exp(-np.abs(x[:-1] - x[1:]) / 2.0))
        
        # Combined result with added noise-like perturbations
        return scale_factor * (f1 + f2 + f3 + f4 + cross_term + f5 + f6 + f7 + f8 + f9 + exp_coupling)