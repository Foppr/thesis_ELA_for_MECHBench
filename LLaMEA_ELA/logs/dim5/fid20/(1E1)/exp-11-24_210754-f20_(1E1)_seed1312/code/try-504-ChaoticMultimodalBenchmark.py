import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with quadratic growth
        f1 = 0.5 * np.sum(x**2) / self.dim
        
        # Exponential decay modulated by trigonometric interference
        f2 = 0.3 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(10.0 * x) * np.cos(7.0 * x))
        
        # Polynomial modulation with fractional powers and asymmetric coefficients
        f3 = 0.2 * np.sum((x**4.2 + 0.7 * x**3.5 + 0.3 * x**2.8 + 0.1 * x**1.9) / self.dim)
        
        # Saddle point structure with chaotic sine-cosine coupling
        f4 = 0.25 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x) * np.exp(-0.3 * x**2))
        
        # Cross-dimensional interaction with asymmetric coupling
        f5 = 0.1 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(0.8 * x[:-1] + 1.2 * x[1:]))
        
        # Fractal-like recursive interference with varying scales
        f6 = 0.15 * np.sum(np.sin(25.0 * np.sin(5.0 * x)) * np.cos(20.0 * np.cos(4.0 * x)))
        
        # Asymmetric polynomial with exponential weighting
        f7 = 0.18 * np.sum((x**3.7 + 0.5 * x**2.6 - 0.3 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Multi-scale harmonic modulation with varying frequencies and amplitudes
        f8 = 0.12 * np.sum(np.sin(30.0 * x + np.sin(15.0 * x)) * np.cos(25.0 * x + np.cos(10.0 * x)))
        
        # Enhanced chaotic interference with dynamic scaling factors
        f9 = 0.22 * np.sum(np.sin(40.0 * np.sin(8.0 * x)) * np.cos(35.0 * np.cos(6.0 * x)) * np.exp(-0.1 * x**2))
        
        # Adaptive dimension coupling with dynamic weights
        f10 = 0.15 * np.sum(np.sin(x * np.sin(2.0 * x)) * np.cos(x * np.cos(1.5 * x)) * (1 + 0.1 * np.sin(5.0 * x)))
        
        # Dynamic exponential modulation with varying decay rates
        f11 = 0.13 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(20.0 * x) * np.cos(18.0 * x))
        
        # Multi-modal resonance with frequency-dependent amplitude
        f12 = 0.17 * np.sum(np.sin(50.0 * x + np.sin(25.0 * x)) * np.cos(45.0 * x + np.cos(20.0 * x)) * (1 + 0.2 * np.sin(30.0 * x)))
        
        # Combine all components with carefully tuned weights for enhanced complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12