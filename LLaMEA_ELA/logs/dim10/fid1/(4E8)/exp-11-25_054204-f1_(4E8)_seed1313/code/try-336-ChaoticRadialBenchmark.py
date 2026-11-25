import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic coupling parameters
        self.coupling_params = np.sin(np.arange(dim) * np.pi / (dim + 1)) * 0.5 + 0.5
        # Precompute adaptive scaling factors
        self.scale_factors = 1.0 + 0.2 * np.log(np.arange(1, dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis components
        rb1 = np.sum(np.exp(-np.sum((x[:, None] - x[None, :])**2, axis=0) / (2.0 * (self.dim / 4.0)**2)))
        
        # Chaotic sine-cosine coupling with adaptive parameters
        chaotic_coupling = 0.0
        for i in range(self.dim - 1):
            chaotic_coupling += self.coupling_params[i] * np.sin(x[i]) * np.cos(x[i+1])
        f2 = 0.3 * chaotic_coupling
        
        # Polynomial interactions with adaptive scaling
        f3 = 0.25 * np.sum((x**4) + (x**3) - 2*(x**2) + x)
        
        # Multi-scale Gaussian components with varying widths
        f4 = 0.15 * np.sum(np.exp(-0.5 * ((x - 1.0)**2 + (x + 1.0)**2) / (self.dim / 8.0)))
        
        # Fractal-like nested structure with recursive scaling
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += np.sin(x[i] * np.cos(x[i])) * np.exp(-np.abs(x[i]) / (self.dim + 1))
        f5 = 0.2 * nested_term
        
        # Adaptive dimensional coupling with chaotic modulation
        dim_coupling = 0.0
        for i in range(self.dim):
            dim_coupling += self.scale_factors[i] * np.sin(x[i]**2) * np.cos(x[i])
        f6 = 0.18 * dim_coupling
        
        # Hybrid polynomial-Gaussian interactions
        hybrid_term = 0.0
        for i in range(self.dim):
            hybrid_term += (x[i]**3) * np.exp(-x[i]**2 / (self.dim + 1))
        f7 = 0.12 * hybrid_term
        
        # Cross-dimensional chaotic resonance
        resonance = 0.0
        for i in range(1, self.dim):
            resonance += np.sin(x[i-1] * x[i]) * np.cos(x[i-1] + x[i])
        f8 = 0.1 * resonance
        
        # Combined adaptive scaling factor
        scale_factor = 1.0 + 0.25 * np.log(self.dim + 1)
        
        # Return final function value with combined terms
        return scale_factor * (rb1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)