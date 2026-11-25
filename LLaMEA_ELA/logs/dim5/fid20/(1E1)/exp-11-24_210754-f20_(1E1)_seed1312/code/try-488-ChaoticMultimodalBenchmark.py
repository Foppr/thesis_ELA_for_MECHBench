import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic conditioning term
        f1 = 0.4 * np.sum(x**2) / self.dim
        
        # Enhanced exponential decay with chaotic sine-cosine interference
        f2 = 0.35 * np.sum(np.exp(-0.7 * np.abs(x)) * np.sin(12.0 * x) * np.cos(9.0 * x))
        
        # Fractional polynomial modulation with asymmetric weights and higher-order terms
        f3 = 0.25 * np.sum((x**5.1 + 0.8 * x**4.3 + 0.6 * x**3.7 + 0.4 * x**2.9 + 0.2 * x**1.8) / self.dim)
        
        # Chaotic saddle point structure with multi-scale coupling
        f4 = 0.3 * np.sum(np.sin(18.0 * x) * np.cos(14.0 * x) * np.exp(-0.4 * x**2))
        
        # Cross-dimensional interaction with non-uniform coupling coefficients
        f5 = 0.15 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(0.9 * x[:-1] + 1.3 * x[1:]))
        
        # Fractal-like recursive interference with multi-scale modulation
        f6 = 0.2 * np.sum(np.sin(30.0 * np.sin(6.0 * x)) * np.cos(25.0 * np.cos(5.0 * x)))
        
        # Asymmetric polynomial with exponential weighting and additional sinusoidal perturbation
        f7 = 0.22 * np.sum((x**4.1 + 0.6 * x**3.2 - 0.4 * x**2.1 + 0.1 * x) * np.exp(-0.25 * np.abs(x)) * np.sin(8.0 * x))
        
        # Multi-scale harmonic modulation with varying frequencies and complex amplitude envelopes
        f8 = 0.18 * np.sum(np.sin(35.0 * x + np.sin(18.0 * x)) * np.cos(30.0 * x + np.cos(12.0 * x)))
        
        # Additional chaotic interference term with hyperbolic tangent modulation
        f9 = 0.12 * np.sum(np.tanh(20.0 * x) * np.sin(28.0 * x) * np.cos(22.0 * x))
        
        # Combine all components with enhanced complexity and varied influence
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9