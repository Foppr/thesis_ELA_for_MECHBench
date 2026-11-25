import numpy as np

class ExponentialTrigonometricValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute exponential decay weights and wave coefficients
        self.exp_weights = np.exp(-np.arange(dim) / (dim + 1))
        self.wave_coeffs = np.sin(np.linspace(0, 2*np.pi, dim)) * 0.3 + 0.7
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with oscillating base
        exp_term = np.sum(self.exp_weights * np.exp(-0.5 * (x**2)) * np.cos(2.0 * x))
        
        # Trigonometric wave interference with adaptive frequencies
        wave_term = np.sum(np.sin(self.wave_coeffs * x) * np.cos(1.5 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Adaptive parabolic valleys with varying depths and widths
        valley_term = 0.0
        for i in range(self.dim):
            depth = 0.5 + 0.5 * np.sin(i * 0.5)
            width = 0.3 + 0.7 * np.cos(i * 0.3)
            valley_term += depth * (x[i] - 1.0)**2 * np.exp(-0.5 * ((x[i] - 1.0)**2) / width**2)
        valley_term *= 0.4
        
        # Cross-dimensional coupling with exponential interaction
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.exp(-0.5 * (x[i] - x[i+1])**2) * np.sin(x[i] + x[i+1])
        coupling_term = 0.3 * coupling
        
        # Multi-scale harmonic oscillations with varying amplitudes
        harmonic = 0.0
        for i in range(self.dim):
            amplitude = 1.0 + 0.5 * np.sin(i * 0.7)
            frequency = 1.0 + 0.8 * np.cos(i * 0.4)
            harmonic += amplitude * np.sin(frequency * x[i]) * np.cos(0.5 * x[i])
        harmonic_term = 0.25 * harmonic
        
        # Dynamic conditioning with dimensionality-dependent scaling
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * 0.3)
        
        return scale_factor * (exp_term + wave_term + valley_term + coupling_term + harmonic_term)