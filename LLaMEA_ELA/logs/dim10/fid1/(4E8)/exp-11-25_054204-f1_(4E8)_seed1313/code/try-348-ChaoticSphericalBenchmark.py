import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial weights for interaction terms
        self.radial_weights = np.exp(-np.arange(1, dim + 1) / (dim * 0.3))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Radial sinusoidal component with varying frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(i * 0.9)  # Varying frequency modulation
            f2 += 1.2 * np.sin(freq * x[i]) * np.cos(freq * x[i] / 1.5)
        
        # Radial basis function interactions with adaptive scaling
        f3 = 0.0
        for i in range(self.dim):
            radial_dist = np.sum((x - x[i])**2)  # Radial distance from point
            f3 += 0.9 * np.exp(-radial_dist / (2.0 * (i + 1)))
        
        # Polynomial chaos with sinusoidal modulation
        f4 = 0.7 * np.sum(x**4 * np.sin(2.5 * x))
        
        # Cross-dimensional coupling with radial weighting
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = self.radial_weights[i]
            cross_interaction += weight * np.sin(x[i] + x[i+1])
        f5 = 0.9 * cross_interaction
        
        # Adaptive harmonic oscillation with radial coupling
        f6 = 0.5 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.exp(-np.sum(x**2) / 15.0))
        
        # Multi-peak radial component with exponential decay
        f7 = 0.0
        for i in range(self.dim):
            peak_pos = 3.0 * np.sin(i * 0.6)
            f7 += 1.1 * np.exp(-((x[i] - peak_pos)**2) / 2.0) * np.cos(3.5 * x[i])
        
        # Sine-cosine polynomial interaction
        f8 = 0.4 * np.sum(np.sin(x)**2 + np.cos(x)**2)
        
        # Radial power law scaling with harmonic modulation
        f9 = 0.8 * np.sum((x**3) * np.sin(1.5 * x) * np.exp(-np.sum(x**2) / 12.0))
        
        # Modified radial basis with cosine interaction
        f10 = 0.7 * np.sum(np.cos(x) * np.exp(-np.sum((x - 1.5)**2) / 4.0))
        
        # Additional fractal-like radial component
        f11 = 0.6 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.exp(-np.sum(x**2) / 8.0))
        
        # Adaptive polynomial with radial coupling
        f12 = 0.4 * np.sum((x**5) * np.cos(2.5 * x) * np.exp(-np.sum(x**2) / 20.0))
        
        # Combined scaling factor based on dimensionality
        scale_factor = 1.0 + 0.7 * np.log(self.dim + 1)
        
        # Final function with all components
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12)