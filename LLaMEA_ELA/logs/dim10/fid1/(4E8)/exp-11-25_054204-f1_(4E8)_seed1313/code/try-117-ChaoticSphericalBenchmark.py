import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling with increased complexity
        self.chaotic_sequence = np.sin(np.sqrt(np.arange(1, dim + 1))) * np.log(dim + 1) / np.log(2 * dim + 1)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Chaotic spherical harmonic component with enhanced frequency modulation
        f2 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.2 * self.chaotic_sequence[i]  # Increased frequency modulation
            f2 -= 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Spherical harmonic interactions with adaptive coupling and increased complexity
        f3 = 0.4 * np.sum(np.sin(x) * np.cos(3.0 * x))  # Increased coefficient
        
        # Logistic map chaotic modulation with higher-order terms
        f4 = 0.25 * np.sum(np.sin(np.pi * np.log(1 + np.abs(x))) * np.cos(4.0 * x))
        
        # Cross-dimensional coupling with exponential weighting and novel interaction
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-i / (self.dim + 3))  # Slightly different weighting
            cross_interaction += weight * np.sin(x[i] * x[i+1]) * np.cos(0.5 * x[i])
        f5 = 0.4 * cross_interaction  # Increased coefficient
        
        # Adaptive polynomial chaos with fractal-like behavior and enhanced nonlinearity
        f6 = 0.2 * np.sum((x**5) * np.sin(3.0 * x))  # Slightly increased coefficient
        
        # Sigmoidal scaling with chaotic modulation and additional sinusoidal component
        f7 = 0.3 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.cos(x) * np.sin(0.5 * x))  # Increased coefficient
        
        # Enhanced harmonic oscillation with dynamic frequency and higher harmonics
        freq = 2.0 + 0.5 * np.sin(np.sum(x**2) / 15.0)  # Altered base frequency
        f8 = 0.2 * np.sum(np.sin(freq * x) * np.cos(3.0 * x))  # Increased coefficient
        
        # Nonlinear correlation with exponential weighting and additional polynomial term
        f9 = 0.15 * np.sum(np.exp(-x**2) * x**4)  # Increased coefficient
        
        # Additional higher-order terms for increased complexity (mutated)
        f10 = 0.1 * np.sum(x**7 * np.cos(x/2))  # Slightly increased coefficient
        f11 = 0.18 * np.sum(np.abs(x)**3)      # Increased coefficient
        
        # New term: seventh-order polynomial with cosine modulation and chaotic amplitude
        amplitude = 1.0 + 0.2 * np.sin(np.sum(x**2) / 20.0)
        f12 = 0.1 * np.sum((x**7) * np.cos(1.5 * x) * amplitude)  # New term added
        
        # Additional interaction term: coupled sine waves with dynamic phase
        phase = np.sum(np.sin(x)) / self.dim
        f13 = 0.12 * np.sum(np.sin(x + phase) * np.cos(2.0 * x + phase))
        
        # Combined scaling based on dimensionality with enhanced nonlinearity
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 2)  # Slightly increased scaling
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13)