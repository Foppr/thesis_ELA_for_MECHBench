import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors
        self.scales = np.array([2**(i) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.3 * np.sum(x**2) / self.dim
        
        # Fractal exponential potential with varying scales
        f2 = 0.4 * np.sum(np.exp(-self.scales * np.abs(x)) * np.sin(self.scales * x))
        
        # Directional gradient modulation with adaptive weights
        grad_weights = np.exp(-0.1 * np.abs(x))
        f3 = 0.25 * np.sum(grad_weights * (x**3 + 0.5 * x**2 - 0.3 * x))
        
        # Ridge structure with multi-scale harmonic modulation
        ridge_term = np.sin(10.0 * x) * np.cos(8.0 * x)
        f4 = 0.2 * np.sum(ridge_term * np.exp(-0.5 * x**2))
        
        # Adaptive curvature with fractal scaling
        curvature = 1.0 + 0.5 * np.sin(self.scales * np.log(np.abs(x) + 1e-8))
        f5 = 0.15 * np.sum(curvature * x**4)
        
        # Multi-fractal interference pattern
        f6 = 0.18 * np.sum(np.sin(15.0 * np.sin(3.0 * x)) * np.cos(12.0 * np.cos(2.5 * x)))
        
        # Asymmetric saddle points with exponential coupling
        f7 = 0.12 * np.sum(np.exp(-0.5 * x**2) * np.sin(20.0 * x) * np.cos(15.0 * x))
        
        # Scale-invariant ridge valleys
        f8 = 0.1 * np.sum(np.abs(x) * np.sin(25.0 * x) * np.cos(20.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8