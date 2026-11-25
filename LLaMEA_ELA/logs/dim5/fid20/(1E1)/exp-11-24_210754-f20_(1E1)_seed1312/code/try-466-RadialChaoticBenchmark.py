import numpy as np

class RadialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.c1 = 3.8
        self.c2 = 0.1
        self.c3 = 2.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function components with varying widths and centers
        rb1 = np.sum(np.exp(-0.5 * ((x - 2.0)**2 + (x + 2.0)**2) / 1.5))
        rb2 = np.sum(np.exp(-0.3 * ((x - 1.0)**2 + (x + 1.0)**2) / 2.0))
        rb3 = np.sum(np.exp(-0.7 * (x**2) / 3.0))
        
        # Adaptive conditioning based on chaotic logistic map
        adaptive_factor = 1.0 + 0.5 * np.sin(self.c1 * np.log(np.abs(x) + 1e-8)) * np.cos(self.c2 * x)
        
        # Chaotic phase shifts with dimension coupling
        phase_shifts = np.sin(self.c3 * x + np.sin(2 * x))
        
        # Gaussian peaks with varying heights and widths
        peaks = np.sum(0.5 * np.exp(-0.5 * ((x - 1.5)**2) / 0.8) + 
                       0.3 * np.exp(-0.5 * ((x + 1.5)**2) / 1.2) +
                       0.4 * np.exp(-0.5 * (x**2) / 0.6))
        
        # Cross-dimensional coupling with chaotic modulation
        coupling = np.sum(np.sin(x[:-1] * x[1:]) * np.cos(0.5 * x[:-1] + 0.8 * x[1:]))
        
        # Asymmetric exponential decay with polynomial modulation
        asym_exp = np.sum((np.exp(-0.3 * np.abs(x)) * (x**2.5 + 0.5 * x**1.8)) / self.dim)
        
        # Fractal-like harmonic interference
        fractal = np.sum(np.sin(10.0 * np.sin(3.0 * x)) * np.cos(7.0 * np.cos(2.0 * x)))
        
        # Combine all components with carefully tuned weights
        return 0.4 * rb1 + 0.3 * rb2 + 0.2 * rb3 + 0.15 * peaks + \
               0.1 * coupling + 0.08 * asym_exp + 0.07 * fractal + \
               np.sum(adaptive_factor * phase_shifts) / self.dim