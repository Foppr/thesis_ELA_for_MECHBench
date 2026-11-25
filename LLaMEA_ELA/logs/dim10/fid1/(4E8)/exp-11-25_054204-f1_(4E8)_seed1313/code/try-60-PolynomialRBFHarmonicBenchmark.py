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
        
        # Cross-dimension interaction with quaternion-inspired coupling
        quaternion_term = 0.0
        for i in range(self.dim - 3):
            quaternion_term += (x[i] * x[i+1] * x[i+2] * x[i+3])
        f5 = 0.3 * quaternion_term
        
        # Fractional Brownian motion-like noise component
        fbm_noise = 0.0
        for i in range(self.dim):
            fbm_noise += np.sin((i + 1) * np.sum(x)) * np.cos((i + 1) * np.sum(x**2))
        f6 = 0.25 * fbm_noise
        
        # Enhanced nonlinearity with hyperbolic tangent
        f7 = 0.4 * np.sum(np.tanh(x)**3)
        
        # Cubic interaction term with adaptive weights
        cubic_interaction = 0.0
        for i in range(self.dim - 2):
            cubic_interaction += (x[i] * x[i+1] * x[i+2]) * np.sin(i + 1)
        f8 = 0.15 * cubic_interaction
        
        # Additional sine coupling with varying frequencies
        freq_coupling = 0.0
        for i in range(self.dim - 1):
            freq_coupling += np.sin((i + 1) * x[i]) * np.cos((i + 2) * x[i+1])
        f9 = 0.3 * freq_coupling
        
        # Fractional polynomial expansion with variable exponents
        fractional_term = 0.0
        for i in range(self.dim):
            fractional_term += (x[i] ** (1.5 + np.sin(i))) * np.cos(x[i])
        f10 = 0.2 * fractional_term
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10