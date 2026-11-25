import numpy as np

class ChaoticRBFPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for adaptive center placement
        self.chaotic_sequence = np.sin(np.arange(dim) * np.pi / (dim + 1)) * 2.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Chaotic radial basis function component with adaptive centers
        f2 = 0.0
        for i in range(self.dim):
            center = self.chaotic_sequence[i] + 2.5
            f2 -= 0.5 * np.exp(-0.5 * (x[i] - center)**2 / 0.5)
        
        # Sine-based chaotic modulation with modified frequency
        f3 = 0.35 * np.sum(np.sin(1.5 * x) * np.cos(2.5 * x))
        
        # Polynomial coupling with gradient-enhanced terms
        f4 = 0.12 * np.sum(x**3 * np.sin(x))
        
        # Cross-dimensional interaction with chaotic coupling
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += np.sin(x[i] * x[i+1]) * (i + 1) * 0.5
        f5 = 0.25 * cross_interaction
        
        # Adaptive polynomial chaos expansion with modified exponent
        f6 = 0.07 * np.sum((x**5) * np.cos(x))
        
        # Enhanced harmonic oscillation with dynamic frequency
        freq = 1.2 + 0.3 * np.sin(np.sum(x**2) / 8.0)
        f7 = 0.18 * np.sum(np.sin(freq * x) * np.cos(1.5 * x))
        
        # Nonlinear correlation with exponential weighting
        f8 = 0.12 * np.sum(np.exp(-x**2) * x**3)
        
        # Combined scaling based on dimensionality
        scale_factor = 1.0 + 0.25 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)