import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic coupling coefficients with fractal scaling
        self.coupling_coeffs = np.sin(np.arange(1, dim + 1) * np.pi / (dim * 2.0)) * np.exp(-np.arange(1, dim + 1) / (dim * 0.5))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical base with chaotic scaling
        f1 = np.sum(x**2) * (1.0 + 0.3 * np.sin(np.sum(x**2) / 10.0))
        
        # Multi-scale chaotic sine-cosine components with dynamic exponents
        f2 = 0.0
        for i in range(self.dim):
            exp_factor = 2.0 + 1.5 * np.sin(i * 0.6 + 0.4 * np.cos(i * 0.3))
            freq = 1.0 + 2.0 * np.sin(i * 0.8 + 0.6 * np.cos(i * 0.4))
            f2 += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0) * (x[i]**exp_factor)
        
        # Fractal-inspired radial interaction with chaotic coupling
        f3 = 0.0
        for i in range(self.dim):
            dist = np.sum((x - x[i])**2)
            coupling = self.coupling_coeffs[i] * (1.0 + 0.5 * np.sin(i * 0.7))
            f3 += coupling * np.exp(-dist / (2.0 * (i + 1))) * np.cos(dist / (i + 1))
        
        # Polynomial chaos with dynamic modulation and fractal components
        f4 = 0.8 * np.sum(x**4 * np.sin(2.5 * x) * np.exp(-np.sum(x**2) / 20.0))
        
        # Cross-dimensional coupling with chaotic scaling and phase shifts
        cross_term = 0.0
        for i in range(self.dim - 1):
            scale = 1.0 + 0.6 * np.sin(i * 0.5 + 0.3 * np.cos(i * 0.2))
            phase_shift = 0.3 * np.sin(i * 0.8 + 0.2 * np.cos(i * 0.4))
            cross_term += scale * np.sin(x[i] + x[i+1] + phase_shift)
        f5 = 1.2 * cross_term
        
        # Adaptive harmonic oscillation with chaotic modulation and radial scaling
        f6 = 0.7 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.exp(-np.sum(x**2) / 15.0))
        
        # Multi-peak exponential decay with fractal positioning
        f7 = 0.0
        for i in range(self.dim):
            peak_pos = 2.0 * np.sin(i * 0.6 + 0.4 * np.cos(i * 0.3))
            f7 += 1.5 * np.exp(-((x[i] - peak_pos)**2) / 2.0) * np.sin(5.0 * x[i])
        
        # Sine-cosine polynomial with dynamic exponents and chaotic modulation
        f8 = 0.6 * np.sum(np.sin(x)**4 + np.cos(x)**4 + 0.3 * np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Radial power law with harmonic modulation and fractal scaling
        f9 = 0.9 * np.sum((x**5) * np.cos(1.8 * x) * np.exp(-np.sum(x**2) / 25.0))
        
        # Modified radial basis with sine interaction and chaotic coupling
        f10 = 0.8 * np.sum(np.sin(x) * np.exp(-np.sum((x - 1.2)**2) / 4.0) * (1.0 + 0.3 * np.cos(x)))
        
        # Additional fractal-like component with enhanced coupling and chaotic scaling
        f11 = 0.7 * np.sum(np.cos(2.8 * x) * np.sin(1.9 * x) * np.exp(-np.sum(x**2) / 18.0))
        
        # Adaptive polynomial with radial coupling and chaotic modulation
        f12 = 0.6 * np.sum((x**7) * np.sin(2.0 * x) * np.exp(-np.sum(x**2) / 30.0))
        
        # Enhanced scaling factor based on dimensionality, chaos, and fractal complexity
        scale_factor = 1.0 + 1.5 * np.log(self.dim + 1) + 0.5 * np.sin(self.dim * 0.6 + 0.4 * np.cos(self.dim * 0.2))
        
        # Final function with all components
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12)