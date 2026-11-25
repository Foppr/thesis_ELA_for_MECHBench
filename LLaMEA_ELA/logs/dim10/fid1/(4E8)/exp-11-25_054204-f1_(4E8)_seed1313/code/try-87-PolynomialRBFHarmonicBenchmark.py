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
        f3 = 0.7 * np.sum(x**3) + 0.15 * np.sum(x**4)
        
        # Harmonic oscillation modulated by gradient magnitude
        grad_magnitude = np.sqrt(np.sum(np.gradient(x)**2))
        f4 = 2.5 * np.sin(grad_magnitude) * np.cos(2.5 * np.sum(x))
        
        # Cross-dimension interaction with sine coupling
        cross_term = 0.4 * np.sum(np.sin(x[:-1] * x[1:]))
        
        # Nonlinear correlation term with increased amplitude
        f5 = 0.08 * np.sum((x**2) * np.sin(x))
        
        # Additional cubic interaction term for increased complexity
        f6 = 0.2 * np.sum(x[:-2] * x[1:-1] * x[2:])
        
        # Novel hyperbolic tangent coupling term
        f7 = 0.3 * np.sum(np.tanh(x) * np.sin(x))
        
        # Enhanced harmonic modulation with exponential decay
        f8 = 1.5 * np.exp(-0.1 * np.sum(x**2)) * np.cos(3.0 * np.sum(x))
        
        # Quadratic cross-term with variable coupling strength
        f9 = 0.25 * np.sum((x[:-1] - x[1:])**2)
        
        # Multi-scale sinusoidal modulation
        f10 = 0.6 * np.sum(np.sin(5.0 * x) + np.cos(3.0 * x))
        
        # Added cosine modulation with increased frequency and amplitude
        f11 = 0.8 * np.sum(np.cos(4.0 * x) * np.sin(x))
        
        # Chaotic modulation with logistic map dynamics
        chaotic_factor = 0.5
        for i in range(self.dim):
            if i > 0:
                chaotic_factor *= (4.0 * x[i-1] * (1 - x[i-1]))
        f12 = 0.3 * np.sum(chaotic_factor * np.sin(x))
        
        # Higher-order polynomial interaction
        f13 = 0.1 * np.sum(x**5)
        
        # Complex cross-dimensional coupling with exponential scaling
        exp_coupling = np.exp(-0.5 * np.sum((x[:-1] - x[1:])**2))
        f14 = 0.4 * np.sum(exp_coupling * x[:-1] * x[1:])
        
        # Sine-cosine hybrid modulation with varying frequencies
        f15 = 0.2 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Fractional polynomial chaos term
        f16 = 0.15 * np.sum(x**(1.5))
        
        # Increased complexity with nested harmonic oscillations
        nested_oscillation = 0.3 * np.sum(np.sin(np.cos(x)))
        f17 = nested_oscillation
        
        return f1 + f2 + f3 + f4 + cross_term + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17