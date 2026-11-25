import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with quadratic growth
        f1 = 0.5 * np.sum(x**2) / self.dim
        
        # Enhanced exponential decay modulated by trigonometric interference
        f2 = 0.4 * np.sum(np.exp(-0.7 * np.abs(x)) * np.sin(12.0 * x) * np.cos(9.0 * x))
        
        # Polynomial modulation with fractional powers and asymmetric coefficients
        f3 = 0.25 * np.sum((x**4.5 + 0.8 * x**3.7 + 0.4 * x**2.9 + 0.2 * x**2.1) / self.dim)
        
        # Saddle point structure with chaotic sine-cosine coupling
        f4 = 0.3 * np.sum(np.sin(18.0 * x) * np.cos(15.0 * x) * np.exp(-0.4 * x**2))
        
        # Cross-dimensional interaction with asymmetric coupling and dynamic scaling
        f5 = 0.15 * np.sum(np.sin(x[:-1] * x[1:] * np.exp(-0.1 * np.abs(x[:-1]))) * 
                          np.cos(0.9 * x[:-1] + 1.3 * x[1:] * np.exp(0.05 * x[1:])))
        
        # Fractal-like recursive interference with varying scales and chaotic modulation
        f6 = 0.2 * np.sum(np.sin(30.0 * np.sin(6.0 * x)) * np.cos(25.0 * np.cos(5.0 * x)) * 
                         np.exp(-0.1 * np.abs(x)))
        
        # Asymmetric polynomial with exponential weighting and chaotic perturbation
        f7 = 0.2 * np.sum((x**4.0 + 0.6 * x**2.8 - 0.4 * x) * np.exp(-0.25 * np.abs(x)) * 
                         np.sin(20.0 * x))
        
        # Multi-scale harmonic modulation with varying frequencies, amplitudes, and chaotic phase shifts
        f8 = 0.15 * np.sum(np.sin(35.0 * x + np.sin(20.0 * x)) * np.cos(30.0 * x + np.cos(15.0 * x)) * 
                          np.exp(-0.05 * x**2))
        
        # Additional chaotic perturbation with dynamic frequency modulation
        f9 = 0.1 * np.sum(np.sin(40.0 * x * np.sin(5.0 * x)) * np.cos(35.0 * x * np.cos(3.0 * x)))
        
        # Combine all components with carefully tuned weights for enhanced complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9