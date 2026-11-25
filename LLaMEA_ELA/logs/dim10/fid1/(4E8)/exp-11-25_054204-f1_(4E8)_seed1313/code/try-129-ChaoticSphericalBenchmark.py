import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_sequence = np.log(np.arange(1, dim + 1)) / np.log(dim + 1)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Chaotic spherical harmonic component with dynamic frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * self.chaotic_sequence[i]
            f2 -= 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Spherical harmonic interactions with adaptive coupling
        f3 = 0.2 * np.sum(np.sin(x) * np.cos(2.0 * x))
        
        # Logistic map chaotic modulation
        f4 = 0.15 * np.sum(np.sin(np.pi * np.log(1 + np.abs(x))) * np.cos(3.0 * x))
        
        # Cross-dimensional coupling with exponential weighting
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-i / (self.dim + 1))
            cross_interaction += weight * np.sin(x[i] * x[i+1])
        f5 = 0.25 * cross_interaction
        
        # Adaptive polynomial chaos with fractal-like behavior
        f6 = 0.1 * np.sum((x**4) * np.sin(2.0 * x))
        
        # Sigmoidal scaling with chaotic modulation
        f7 = 0.18 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.cos(x))
        
        # Enhanced harmonic oscillation with dynamic frequency
        freq = 1.5 + 0.3 * np.sin(np.sum(x**2) / 10.0)
        f8 = 0.12 * np.sum(np.sin(freq * x) * np.cos(2.0 * x))
        
        # Nonlinear correlation with exponential weighting
        f9 = 0.08 * np.sum(np.exp(-x**2) * x**3)
        
        # Additional higher-order terms for increased complexity (mutated)
        f10 = 0.06 * np.sum(x**7 * np.cos(x/3))  # Slightly increased coefficient and exponent
        f11 = 0.12 * np.sum(np.abs(x)**2.7)       # Slightly increased coefficient and exponent
        
        # New term: quintic polynomial with chaotic sine modulation
        f12 = 0.08 * np.sum((x**5) * np.sin(1.5 * x + np.sin(x[0] if self.dim > 0 else 0)))
        
        # New term: Gaussian-based multi-modal component with dynamic centers
        gaussian_term = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(i * np.pi / (self.dim + 1))
            gaussian_term += np.exp(-0.5 * ((x[i] - center) / 1.5)**2)
        f13 = 0.16 * gaussian_term
        
        # New term: Wavelet-like interaction with frequency modulation
        wavelet_interaction = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.2 * np.sin(x[i])
            wavelet_interaction += np.sin(freq_mod * x[i]) * np.cos(2.0 * x[i])
        f14 = 0.14 * wavelet_interaction
        
        # New term: Hyperbolic tangent coupling with dimension-dependent scaling
        tanh_coupling = 0.0
        for i in range(self.dim - 1):
            tanh_coupling += np.tanh(x[i] + x[i+1]) * np.exp(-i / self.dim)
        f15 = 0.12 * tanh_coupling
        
        # New term: Logarithmic interaction with chaotic perturbation
        log_interaction = 0.0
        for i in range(self.dim):
            perturb = 0.1 * np.sin(np.log(i + 1) + x[i])
            log_interaction += np.log(1.0 + np.abs(x[i])) * np.cos(perturb)
        f16 = 0.10 * log_interaction
        
        # New term: Modified chaotic cosine interaction with adaptive scaling
        chaotic_cosine = 0.0
        for i in range(self.dim):
            chaotic_factor = 0.5 + 0.5 * np.sin(np.log(i + 2) + x[i])
            chaotic_cosine += np.cos(chaotic_factor * x[i]) * np.sin(x[i]**2)
        f17 = 0.18 * chaotic_cosine
        
        # New term: Fractional polynomial with dynamic exponents
        fractional_poly = 0.0
        for i in range(self.dim):
            exponent = 2.5 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            fractional_poly += x[i]**exponent * np.cos(x[i])
        f18 = 0.14 * fractional_poly
        
        # Combined scaling based on dimensionality
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18)