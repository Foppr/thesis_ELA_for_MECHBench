import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial with fractional powers and cross-terms
        f1 = np.sum(x**11 - 6*x**6 + 8*x**4 - 4*x**3 + 2*x**2 - 1.2)
        
        # Multi-frequency trigonometric with chaotic modulation
        f2 = np.sum(np.sin(10.0 * x) * np.cos(12.0 * x) * np.sin(14.0 * x) * np.cos(16.0 * x) * np.sin(18.0 * x) * np.cos(20.0 * x))
        
        # Dynamic radial basis with time-varying centers and widths
        centers = np.linspace(-4.8, 4.8, self.dim)
        widths = np.linspace(0.1, 2.5, self.dim)
        f3 = np.sum(np.exp(-0.3 * (x - centers)**2 / (widths + 0.1)) * np.cos(5.0 * x) * np.sin(3.0 * x))
        
        # Coupled oscillatory terms with variable coupling and delay
        f4 = np.sum(np.sin(8.0 * x[:-1] * x[1:]) * np.cos(8.0 * (x[:-1] + x[1:])) * np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * np.sin(0.5 * x[:-1]) * np.cos(0.5 * x[1:]))
        
        # High-frequency chaotic component with recursive feedback
        f5 = np.sum(np.sin(35.0 * x) * np.cos(40.0 * x) * np.exp(-0.08 * x**2) * np.sin(2.0 * np.sum(x**2)) * np.cos(0.8 * np.sum(x)) * np.sin(0.3 * np.prod(x)))
        
        # Cross-term interaction with dynamic decay and multi-frequency modulation
        f6 = np.sum(np.exp(-0.6 * np.abs(x[:-1] - x[1:])) * np.sin(12.0 * (x[:-1] + x[1:])) * np.cos(8.0 * x[:-1]) * np.sin(6.0 * x[1:]) * np.cos(4.0 * x[:-1] * x[1:]))
        
        # Non-separable component with complex interactions and fractional powers
        f7 = np.sum((x[:-1] + x[1:])**6 * np.sin(9.0 * x[:-1]) * np.cos(9.0 * x[1:]) * np.exp(-0.25 * np.abs(x[:-1] - x[1:])) * np.sin(0.2 * x[:-1]) * np.cos(0.2 * x[1:]))
        
        # Fractal-like component with recursive structure and dynamic scaling
        f8 = np.sum(np.sin(25.0 * x) * np.cos(30.0 * x) * np.sin(35.0 * x) * np.cos(40.0 * x) * np.exp(-0.06 * x**3) * np.sin(0.4 * np.sum(x**3)))
        
        # Combined function with updated weights, normalization, and chaotic amplification
        return 0.28 * f1 + 0.20 * f2 + 0.18 * f3 + 0.15 * f4 + 0.12 * f5 + 0.10 * f6 + 0.08 * f7 + 0.07 * f8