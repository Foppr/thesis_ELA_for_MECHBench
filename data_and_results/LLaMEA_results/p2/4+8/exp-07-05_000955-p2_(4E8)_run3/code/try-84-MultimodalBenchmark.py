import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global convergence
        f1 = np.sum(x**2)
        
        # Nested trigonometric functions creating fractal-like structure
        f2 = 0.5 * np.sum(np.sin(3.0 * np.sin(2.0 * x)) * np.cos(4.0 * np.cos(3.0 * x)))
        
        # Polynomial chaos expansion with mixed monomials
        f3 = 0.3 * np.sum((x**2 + x**3 + x**4) * np.sin(5.0 * x))
        
        # Adaptive gradient modulation with exponential scaling
        f4 = 0.25 * np.sum(np.exp(-0.2 * np.abs(x)) * np.sin(10.0 * x))
        
        # Non-separable interaction terms with higher-order coupling
        f5 = 0.2 * np.sum(x * np.sin(2.0 * x) * np.cos(3.0 * x) * np.exp(-0.1 * np.sum(x**2)))
        
        # Multi-scale Gaussian-based modulation for enhanced multimodality
        f6 = 0.15 * np.sum(np.exp(-0.5 * (x - np.sin(x))**2) * np.sin(8.0 * x))
        
        # Coupled sine-cosine waves with dynamic amplitude
        f7 = 0.1 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x) * (1.0 + 0.3 * np.sin(7.0 * x)))
        
        # Fractional polynomial coupling with variable exponents
        f8 = 0.12 * np.sum(x**(1.5) * np.sin(6.0 * x) * np.cos(9.0 * x))
        
        # Saddle point enhancement through mixed trigonometric interactions
        f9 = 0.08 * np.sum(np.sin(x) * np.cos(2.0 * x) * np.sin(3.0 * x) * np.exp(-0.3 * np.sum(x**2)))
        
        # Complex nonlinearity through nested exponential and polynomial terms
        f10 = 0.09 * np.sum(np.exp(-0.1 * np.abs(x)) * (x**3 + x**5) * np.sin(4.0 * x))
        
        # Combined effect of multiple interacting components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10