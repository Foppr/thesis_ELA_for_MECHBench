import numpy as np

class AdaptiveTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute trigonometric coefficients for dynamic modulation
        self.coeffs = np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Trigonometric chaos component with dynamic frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * self.coeffs[i]
            f2 += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        f2 *= 0.25
        
        # Radial basis function with adaptive centers and widths
        f3 = 0.0
        for i in range(self.dim):
            center = 1.5 * np.sin(i * np.pi / (self.dim + 1))
            width = 0.5 + 0.2 * np.cos(i * np.pi / (self.dim + 1))
            f3 += np.exp(-0.5 * ((x[i] - center) / width)**2)
        f3 *= 0.3
        
        # Adaptive gradient modulation with chaotic perturbation
        f4 = 0.0
        for i in range(self.dim):
            perturb = 0.1 * np.sin(x[i] + i * np.pi / (self.dim + 1))
            grad_mod = 1.0 + 0.2 * np.sin(perturb)
            f4 += grad_mod * np.sin(x[i]) * np.cos(x[i])
        f4 *= 0.2
        
        # Cross-dimensional coupling with sine modulation
        f5 = 0.0
        for i in range(self.dim - 1):
            coupling = np.sin(x[i] * x[i+1])
            freq_mod = 1.0 + 0.1 * np.cos(i * np.pi / (self.dim + 1))
            f5 += freq_mod * coupling
        f5 *= 0.25
        
        # Hyperbolic tangent interactions with dimension-dependent scaling
        f6 = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.1 * np.sin(i * np.pi / (self.dim + 1))
            f6 += np.tanh(scale * x[i]) * np.cos(x[i])
        f6 *= 0.15
        
        # Fractional polynomial with chaotic scaling
        f7 = 0.0
        for i in range(self.dim):
            frac_exp = 1.5 + 0.3 * np.sin(i * np.pi / (self.dim + 1))
            f7 += (x[i]**frac_exp) * np.sin(x[i])
        f7 *= 0.2
        
        # Multi-scale oscillation with dynamic amplitude
        f8 = 0.0
        for i in range(self.dim):
            amp = 0.5 + 0.3 * np.cos(i * np.pi / (self.dim + 1))
            freq = 2.0 + 0.4 * np.sin(i * np.pi / (self.dim + 1))
            f8 += amp * np.sin(freq * x[i])
        f8 *= 0.18
        
        # Logarithmic interaction with chaotic modulation
        f9 = 0.0
        for i in range(self.dim):
            perturb = 0.2 * np.sin(np.log(i + 1) + x[i])
            f9 += np.log(1.0 + np.abs(x[i])) * np.cos(perturb)
        f9 *= 0.12
        
        # Combined scaling based on dimensionality
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9)