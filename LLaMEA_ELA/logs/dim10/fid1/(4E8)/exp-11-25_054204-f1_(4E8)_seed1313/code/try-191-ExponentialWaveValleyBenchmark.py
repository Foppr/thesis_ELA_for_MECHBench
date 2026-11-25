import numpy as np

class ExponentialWaveValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute wave coefficients and decay rates
        self.wave_coeffs = np.cos(np.linspace(0, 2*np.pi, dim)) * 0.5 + 0.5
        self.decay_rates = np.exp(-np.arange(dim) / (dim + 1))
        self.noise_levels = np.logspace(-3, 0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with oscillatory modulation
        exp_decay = np.sum(self.decay_rates * np.exp(-0.1 * x**2) * np.sin(2.0 * x))
        
        # Trigonometric wave interference with adaptive frequencies
        wave_interference = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.5)
            wave_interference += self.wave_coeffs[i] * np.cos(freq * x[i]) * np.sin(freq * x[i])
        wave_term = 0.3 * wave_interference
        
        # Adaptive parabolic valleys with varying curvature
        valley_term = 0.0
        for i in range(self.dim):
            curvature = 1.0 + 0.2 * np.cos(i * 0.7)
            valley_term += curvature * (x[i] - 1.0)**2 * np.exp(-0.5 * x[i]**2)
        valley_term = 0.4 * valley_term
        
        # Multi-scale noise modulation with dimension-dependent sensitivity
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_levels[i] * np.sin(10.0 * x[i]) * np.cos(5.0 * x[i])
        noise_term = 0.2 * noise
        
        # Cross-dimensional coupling with exponential scaling
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.exp(-0.5 * (x[i] - x[i+1])**2) * np.sin(x[i] + x[i+1])
        coupling_term = 0.3 * coupling
        
        # Combined function with dynamic scaling based on dimensionality
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        return scale_factor * (exp_decay + wave_term + valley_term + noise_term + coupling_term)