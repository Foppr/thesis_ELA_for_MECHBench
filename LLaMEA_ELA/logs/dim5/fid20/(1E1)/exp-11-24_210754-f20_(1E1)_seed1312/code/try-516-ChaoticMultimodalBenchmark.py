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
        
        # Additional chaotic coupling with higher frequency oscillations
        f9 = 0.22 * np.sum(np.sin(40.0 * x) * np.cos(35.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Fractional power cross-dimensional interactions with enhanced coupling
        f10 = 0.15 * np.sum((x[:-1]**1.8 * x[1:]**2.3 + x[:-1]**2.7 * x[1:]**1.5) / self.dim)
        
        # Combined chaotic interference with dynamic scaling and modified weights
        f11 = 0.1 * np.sum(np.sin(50.0 * np.sin(8.0 * x)) * np.cos(40.0 * np.cos(6.0 * x)) * np.exp(-0.2 * x**2))
        
        # Asymmetric fractional polynomial with mixed curvature and enhanced nonlinearity
        f12 = 0.17 * np.sum((x**3.9 + 0.6 * x**3.1 - 0.4 * x**2.2 + 0.2 * x**1.3) * np.exp(-0.15 * np.abs(x)))
        
        # Enhanced cross-dimensional coupling with sine-cosine modulation and additional interference
        f13 = 0.13 * np.sum(np.sin(20.0 * x[:-1] + 15.0 * x[1:]) * np.cos(18.0 * x[:-1] - 12.0 * x[1:]) * np.exp(-0.1 * x[:-1]**2))
        
        # Multi-scale chaotic interference with exponential weighting and modified frequency
        f14 = 0.19 * np.sum(np.exp(-0.25 * np.abs(x)) * np.sin(35.0 * x) * np.cos(30.0 * x) * np.sin(5.0 * x))
        
        # Additional chaotic modulation with asymmetric scaling and higher frequency components
        f15 = 0.14 * np.sum(np.sin(45.0 * x) * np.cos(42.0 * x) * np.exp(-0.1 * x**2) * np.sin(8.0 * x))
        
        # Modified fractional polynomial with enhanced curvature and nonlinearity
        f16 = 0.16 * np.sum((x**3.8 + 0.55 * x**3.2 - 0.35 * x**2.1 + 0.15 * x**1.4) * np.exp(-0.12 * np.abs(x)))
        
        # Enhanced cross-dimensional interactions with increased coupling strength
        f17 = 0.11 * np.sum((x[:-1]**2.5 * x[1:]**1.9 + x[:-1]**1.7 * x[1:]**2.8) / self.dim)
        
        # Combined chaotic interference with dynamic scaling and additional nonlinear terms
        f18 = 0.13 * np.sum(np.sin(60.0 * np.sin(9.0 * x)) * np.cos(50.0 * np.cos(7.0 * x)) * np.exp(-0.25 * x**2) * np.cos(3.0 * x))
        
        # Final enhanced multimodal landscape with improved complexity and fitness
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18