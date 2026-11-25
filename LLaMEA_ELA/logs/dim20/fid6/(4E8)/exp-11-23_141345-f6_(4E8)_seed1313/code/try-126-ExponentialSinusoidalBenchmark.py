import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponentially modulated sinusoidal base with varying frequencies
        exp_sin_term = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(2.0 * np.pi * x) * np.cos(1.5 * np.pi * x))
        
        # Radial symmetry breaking with modified distance metrics
        radial_term = np.sum(np.exp(-0.5 * (x**2 + 0.3 * np.abs(x)**1.7)) * np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Cross-dimensional coupling with adaptive scaling factors
        cross_coupling = np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2) * np.sin(1.8 * x[:-1]) * np.cos(1.2 * x[1:]))
        
        # Multi-scale harmonic modulation with varying amplitudes
        multi_harmonic = np.sum(np.sin(4.0 * x) * np.cos(3.0 * x) * (1.0 + 0.2 * np.sin(2.0 * x)) * np.exp(-0.15 * x**2))
        
        # Adaptive fractal-like interaction with exponential decay
        fractal_interaction = np.sum(np.exp(-np.abs(x)**1.3) * np.sin(2.5 * x) * np.cos(1.7 * x) + 0.1 * np.log(1.0 + np.abs(x)))
        
        # Asymmetric gradient modulation with hyperbolic tangent
        asym_grad = np.sum(np.tanh(1.5 * x) * np.exp(-0.25 * x**2) * np.sin(3.5 * x))
        
        # Combined function with optimized weights
        return 0.28 * exp_sin_term + 0.22 * radial_term + 0.18 * cross_coupling + 0.14 * multi_harmonic + 0.10 * fractal_interaction + 0.08 * asym_grad