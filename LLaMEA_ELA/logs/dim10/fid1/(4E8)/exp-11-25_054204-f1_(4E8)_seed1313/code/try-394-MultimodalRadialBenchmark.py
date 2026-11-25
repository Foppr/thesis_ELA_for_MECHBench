import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial weights for interaction terms with enhanced fractal scaling
        self.radial_weights = np.exp(-np.arange(1, dim + 1) / (dim * 0.08))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced radial sinusoidal component with chaotic frequency modulation and dynamic amplitudes
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 3.0 * np.sin(i * 1.1 + 0.8 * np.cos(i * 0.5))  # Enhanced chaotic frequency modulation
            amp = 1.0 + 0.6 * np.sin(i * 0.9 + 0.7 * np.cos(i * 0.4))   # Enhanced dynamic amplitude
            f2 += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] / 3.0)
        
        # Radial basis function interactions with fractal scaling, phase shifts, and enhanced coupling
        f3 = 0.0
        for i in range(self.dim):
            radial_dist = np.sum((x - x[i])**2)  # Radial distance from point
            scale = 1.0 + 1.1 * np.sin(i * 0.7 + 0.6 * np.cos(i * 0.4))
            phase_shift = 0.6 * np.sin(i * 0.8 + 0.5 * np.cos(i * 0.3))
            f3 += 1.1 * np.exp(-radial_dist / (2.0 * (i + 1) * scale)) * np.sin(phase_shift)
        
        # Polynomial chaos with dynamic sinusoidal modulation, chaotic exponents, and enhanced scaling
        f4 = 1.0 * np.sum(x**6 * np.sin(4.2 * x) * np.exp(-np.sum(x**2) / 30.0))
        
        # Cross-dimensional coupling with enhanced radial weighting, phase shifts, and fractal scaling
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = self.radial_weights[i] * (1.0 + 0.7 * np.sin(i * 0.9))
            phase_shift = 0.7 * np.sin(i * 1.3 + 0.5 * np.cos(i * 0.5))
            cross_interaction += weight * np.sin(x[i] + x[i+1] + phase_shift)
        f5 = 1.5 * cross_interaction
        
        # Adaptive harmonic oscillation with multi-scale radial coupling, chaotic modulation, and enhanced complexity
        f6 = 0.9 * np.sum(np.sin(3.2 * x) * np.cos(2.5 * x) * np.exp(-np.sum(x**2) / 25.0))
        
        # Multi-peak radial component with dynamic peak positions, exponential decay, and enhanced fractal modulation
        f7 = 0.0
        for i in range(self.dim):
            peak_pos = 4.0 * np.sin(i * 0.9 + 0.7 * np.cos(i * 0.5))
            f7 += 1.5 * np.exp(-((x[i] - peak_pos)**2) / 2.0) * np.cos(7.0 * x[i])
        
        # Sine-cosine polynomial interaction with enhanced dynamic scaling and chaotic components
        f8 = 0.8 * np.sum(np.sin(x)**4 + np.cos(x)**4 + 0.4 * np.sin(3.1 * x) * np.cos(2.5 * x))
        
        # Radial power law scaling with harmonic modulation, adaptive exponents, and enhanced fractal components
        f9 = 1.1 * np.sum((x**5) * np.sin(2.2 * x) * np.exp(-np.sum(x**2) / 30.0))
        
        # Modified radial basis with cosine interaction, dynamic weights, and enhanced chaotic coupling
        f10 = 1.0 * np.sum(np.cos(x) * np.exp(-np.sum((x - 2.0)**2) / 7.0) * (1.0 + 0.6 * np.sin(x)))
        
        # Additional fractal-like radial component with enhanced coupling and chaotic scaling
        f11 = 0.9 * np.sum(np.sin(4.0 * x) * np.cos(3.2 * x) * np.exp(-np.sum(x**2) / 20.0))
        
        # Adaptive polynomial with radial coupling, dynamic exponents, and enhanced chaotic modulation
        f12 = 0.8 * np.sum((x**7) * np.cos(3.2 * x) * np.exp(-np.sum(x**2) / 30.0))
        
        # Enhanced scaling factor based on dimensionality, chaos, and fractal complexity
        scale_factor = 1.0 + 1.5 * np.log(self.dim + 1) + 0.7 * np.sin(self.dim * 0.7 + 0.5 * np.cos(self.dim * 0.3))
        
        # Final function with all components
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12)