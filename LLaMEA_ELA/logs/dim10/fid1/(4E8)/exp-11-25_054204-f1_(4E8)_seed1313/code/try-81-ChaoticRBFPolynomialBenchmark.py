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
        
        # Sine-based chaotic modulation
        f3 = 0.3 * np.sum(np.sin(x) * np.cos(3.0 * x))
        
        # Polynomial coupling with gradient-enhanced terms
        f4 = 0.1 * np.sum(x**3 * np.sin(x))
        
        # Cross-dimensional interaction with chaotic coupling
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += np.sin(x[i] * x[i+1]) * (i + 1)
        f5 = 0.2 * cross_interaction
        
        # Adaptive polynomial chaos expansion
        f6 = 0.05 * np.sum((x**4) * np.cos(x))
        
        # Enhanced harmonic oscillation with dynamic frequency
        freq = 1.0 + 0.5 * np.sin(np.sum(x**2) / 10.0)
        f7 = 0.15 * np.sum(np.sin(freq * x) * np.cos(2.0 * x))
        
        # Nonlinear correlation with exponential weighting
        f8 = 0.1 * np.sum(np.exp(-x**2) * x**3)
        
        # Additional higher-order terms for increased complexity (mutated)
        f9 = 0.07 * np.sum(x**5 * np.sin(x/2))  # Slightly increased coefficient
        f10 = 0.12 * np.sum(np.abs(x)**1.5)     # Slightly increased coefficient
        
        # Add a new term: fourth-order polynomial with cosine modulation
        f11 = 0.08 * np.sum((x**4) * np.cos(2.0 * x))
        
        # Combined scaling based on dimensionality
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)