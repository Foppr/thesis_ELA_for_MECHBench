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
        f2 = 0.4 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(12.0 * x) * np.cos(9.0 * x))
        
        # Polynomial modulation with fractional powers and asymmetric coefficients
        f3 = 0.3 * np.sum((x**5.1 + 0.8 * x**4.3 + 0.4 * x**3.6 + 0.2 * x**2.9) / self.dim)
        
        # Saddle point structure with chaotic sine-cosine coupling
        f4 = 0.3 * np.sum(np.sin(18.0 * x) * np.cos(15.0 * x) * np.exp(-0.35 * x**2))
        
        # Cross-dimensional interaction with asymmetric coupling
        f5 = 0.15 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(1.0 * x[:-1] + 1.5 * x[1:]))
        
        # Fractal-like recursive interference with varying scales
        f6 = 0.2 * np.sum(np.sin(30.0 * np.sin(6.0 * x)) * np.cos(25.0 * np.cos(5.0 * x)))
        
        # Asymmetric polynomial with exponential weighting
        f7 = 0.22 * np.sum((x**4.1 + 0.6 * x**3.3 - 0.4 * x) * np.exp(-0.25 * np.abs(x)))
        
        # Multi-scale harmonic modulation with varying frequencies and amplitudes
        f8 = 0.15 * np.sum(np.sin(35.0 * x + np.sin(18.0 * x)) * np.cos(30.0 * x + np.cos(12.0 * x)))
        
        # Additional chaotic coupling with higher frequency oscillations
        f9 = 0.28 * np.sum(np.sin(45.0 * x) * np.cos(40.0 * x) * np.exp(-0.15 * np.abs(x)))
        
        # Fractional power cross-dimensional interactions
        f10 = 0.2 * np.sum((x[:-1]**2.1 * x[1:]**2.8 + x[:-1]**3.0 * x[1:]**1.8) / self.dim)
        
        # Combined chaotic interference with dynamic scaling
        f11 = 0.15 * np.sum(np.sin(55.0 * np.sin(9.0 * x)) * np.cos(45.0 * np.cos(7.0 * x)) * np.exp(-0.25 * x**2))
        
        # Asymmetric fractional polynomial with mixed curvature
        f12 = 0.2 * np.sum((x**4.3 + 0.7 * x**3.5 - 0.5 * x**2.7 + 0.3 * x**1.6) * np.exp(-0.2 * np.abs(x)))
        
        # Enhanced cross-dimensional coupling with sine-cosine modulation
        f13 = 0.18 * np.sum(np.sin(25.0 * x[:-1] + 20.0 * x[1:]) * np.cos(22.0 * x[:-1] - 15.0 * x[1:]))
        
        # Multi-scale chaotic interference with exponential weighting
        f14 = 0.23 * np.sum(np.exp(-0.3 * np.abs(x)) * np.sin(40.0 * x) * np.cos(35.0 * x))
        
        # Additional chaotic sine-cosine coupling with higher frequency modulation
        f15 = 0.17 * np.sum(np.sin(50.0 * x) * np.cos(45.0 * x) * np.exp(-0.2 * x**2))
        
        # Enhanced fractional polynomial with increased complexity
        f16 = 0.25 * np.sum((x**5.5 + 0.9 * x**4.7 + 0.5 * x**3.9 + 0.3 * x**3.1) / self.dim)
        
        # Increased cross-dimensional interference with additional coupling terms
        f17 = 0.2 * np.sum(np.sin(1.2 * x[:-1] * x[1:]) * np.cos(1.5 * x[:-1] + 1.8 * x[1:]))
        
        # Combined chaotic interference with even stronger dynamic scaling
        f18 = 0.2 * np.sum(np.sin(60.0 * np.sin(10.0 * x)) * np.cos(50.0 * np.cos(8.0 * x)) * np.exp(-0.3 * x**2))
        
        # Multi-scale polynomial modulation with increased curvature
        f19 = 0.18 * np.sum((x**4.8 + 0.7 * x**4.0 - 0.5 * x**3.2 + 0.2 * x**2.4) * np.exp(-0.2 * np.abs(x)))
        
        # Additional exponential weighting with enhanced chaotic interference
        f20 = 0.21 * np.sum(np.exp(-0.35 * np.abs(x)) * np.sin(45.0 * x) * np.cos(40.0 * x))
        
        # Combine all components with carefully tuned weights for enhanced complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20