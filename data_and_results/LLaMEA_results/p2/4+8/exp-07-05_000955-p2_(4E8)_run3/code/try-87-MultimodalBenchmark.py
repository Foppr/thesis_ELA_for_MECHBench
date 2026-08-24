import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global convergence
        f1 = np.sum(x**2)
        
        # Nested trigonometric fractal-like structure with increasing frequency
        f2 = 0.5 * np.sum(np.sin(10.0 * np.sin(5.0 * x)) * np.cos(8.0 * np.cos(3.0 * x)))
        
        # Polynomial chaos expansion with mixed monomials
        f3 = 0.3 * np.sum((x**2 + x**3 + x**4) * np.sin(2.0 * x) * np.cos(3.0 * x))
        
        # Adaptive gradient modulation with exponential scaling
        f4 = 0.25 * np.sum(np.exp(-0.5 * np.sum(x**2)) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Cross-dimensional coupling with higher-order polynomial interactions
        f5 = 0.2 * np.sum((x**5 + x**6) * np.sin(4.0 * x) * np.cos(6.0 * x))
        
        # Sine-cosine wave interference with Gaussian envelope
        f6 = 0.15 * np.sum(np.sin(12.0 * x) * np.cos(9.0 * x) * np.exp(-0.2 * np.sum(x**2)))
        
        # Multi-scale chaotic modulation with fractal-like behavior
        f7 = 0.1 * np.sum(np.sin(25.0 * x) * np.cos(20.0 * x) * np.sin(15.0 * x) * np.cos(10.0 * x))
        
        # Non-separable polynomial coupling with exponential decay
        f8 = 0.12 * np.sum(np.exp(-0.1 * np.sum(x**2)) * (x**3 + x**4) * np.sin(7.0 * x))
        
        # Additional multimodal term with nested sine and cosine functions
        f9 = 0.08 * np.sum(np.sin(20.0 * np.cos(5.0 * x)) * np.cos(15.0 * np.sin(3.0 * x)))
        
        # Combined fractal and polynomial structure with adaptive scaling
        f10 = 0.05 * np.sum((x**7 + x**8) * np.sin(5.0 * x) * np.cos(4.0 * x) * np.exp(-0.3 * np.sum(x**2)))
        
        # Final combined landscape with balanced complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10