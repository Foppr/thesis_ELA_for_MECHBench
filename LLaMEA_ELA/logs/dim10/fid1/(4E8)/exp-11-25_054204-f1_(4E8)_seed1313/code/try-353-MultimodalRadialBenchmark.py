import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial weights for interaction terms
        self.radial_weights = np.exp(-np.arange(1, dim + 1) / (dim * 0.3))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Radial sinusoidal component with varying frequencies and adaptive amplitudes
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.8 * np.sin(i * 0.6)  # Varying frequency modulation
            amp = 0.7 + 0.3 * np.cos(i * 0.4)    # Adaptive amplitude
            f2 += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Radial basis function interactions with dynamic scaling
        f3 = 0.0
        for i in range(self.dim):
            radial_dist = np.sum((x - x[i])**2)  # Radial distance from point
            scale = 1.0 + 0.5 * np.sin(i * 0.3)
            f3 += 0.6 * np.exp(-radial_dist / (2.0 * (i + 1) * scale))
        
        # Polynomial chaos with dynamic sinusoidal modulation
        f4 = 0.5 * np.sum(x**4 * np.sin(3.0 * x) * np.exp(-np.sum(x**2) / 20.0))
        
        # Cross-dimensional coupling with enhanced radial weighting and phase shifts
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = self.radial_weights[i]
            phase_shift = 0.5 * np.sin(i * 0.8)
            cross_interaction += weight * np.sin(x[i] + x[i+1] + phase_shift)
        f5 = 0.7 * cross_interaction
        
        # Adaptive harmonic oscillation with multi-scale radial coupling
        f6 = 0.4 * np.sum(np.sin(2.0 * x) * np.cos(1.5 * x) * np.exp(-np.sum(x**2) / 15.0))
        
        # Multi-peak radial component with dynamic peak positions and exponential decay
        f7 = 0.0
        for i in range(self.dim):
            peak_pos = 2.0 * np.sin(i * 0.5 + 0.3 * np.cos(i * 0.2))
            f7 += 0.9 * np.exp(-((x[i] - peak_pos)**2) / 2.0) * np.cos(4.0 * x[i])
        
        # Sine-cosine polynomial interaction with dynamic scaling
        f8 = 0.3 * np.sum(np.sin(x)**2 + np.cos(x)**2 + 0.1 * np.sin(2.0 * x))
        
        # Radial power law scaling with harmonic modulation and adaptive exponents
        f9 = 0.6 * np.sum((x**3) * np.sin(1.2 * x) * np.exp(-np.sum(x**2) / 18.0))
        
        # Modified radial basis with cosine interaction and dynamic weights
        f10 = 0.5 * np.sum(np.cos(x) * np.exp(-np.sum((x - 1.0)**2) / 4.0) * (1.0 + 0.2 * np.sin(x)))
        
        # Additional fractal-like radial component with enhanced coupling
        f11 = 0.4 * np.sum(np.sin(2.5 * x) * np.cos(1.8 * x) * np.exp(-np.sum(x**2) / 12.0))
        
        # Adaptive polynomial with radial coupling and dynamic exponents
        f12 = 0.3 * np.sum((x**5) * np.cos(2.0 * x) * np.exp(-np.sum(x**2) / 22.0))
        
        # Enhanced scaling factor based on dimensionality and complexity
        scale_factor = 1.0 + 0.7 * np.log(self.dim + 1) + 0.2 * np.sin(self.dim * 0.3)
        
        # Final function with all components
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12)