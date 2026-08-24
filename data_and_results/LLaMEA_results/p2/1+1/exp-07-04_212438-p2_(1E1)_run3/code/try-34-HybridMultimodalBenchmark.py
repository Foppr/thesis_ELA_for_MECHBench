import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degrees and cross-terms
        f1 = np.sum(x**13 - 7*x**7 + 9*x**5 - 5*x**4 + 3*x**2 - 1.5)
        
        # Modified trigonometric component with higher frequencies and phase shifts
        f2 = np.sum(np.sin(9.0 * x) * np.cos(11.0 * x) * np.sin(13.0 * x) * np.cos(17.0 * x) * np.sin(19.0 * x))
        
        # Advanced radial basis function with dynamic centers and variable widths
        centers = np.linspace(-4.5, 4.5, self.dim)
        widths = np.linspace(0.2, 3.0, self.dim)
        f3 = np.sum(np.exp(-0.4 * (x - centers)**2 / widths) * np.cos(4.0 * x))
        
        # Coupled oscillatory terms with variable coupling strength and time delays
        f4 = np.sum(np.sin(7.0 * x[:-1] * x[1:]) * np.cos(7.0 * (x[:-1] + x[1:])) * np.exp(-0.15 * np.abs(x[:-1] - x[1:])))
        
        # High-frequency chaotic-like component with feedback and modulation - MUTATED
        f5 = np.sum(np.sin(30.0 * x) * np.cos(35.0 * x) * np.exp(-0.09 * x**2) * np.sin(1.5 * np.sum(x**2)) * np.cos(0.7 * np.sum(x)) * np.sin(0.3 * np.sum(np.sin(x))))
        
        # Cross-term interaction with dynamic decay and multi-frequency modulation
        f6 = np.sum(np.exp(-0.5 * np.abs(x[:-1] - x[1:])) * np.sin(10.0 * (x[:-1] + x[1:])) * np.cos(7.0 * x[:-1]) * np.sin(5.0 * x[1:]))
        
        # Additional non-separable component with complex interactions and fractional powers
        f7 = np.sum((x[:-1] + x[1:])**7 * np.sin(8.0 * x[:-1]) * np.cos(8.0 * x[1:]) * np.exp(-0.3 * np.abs(x[:-1] - x[1:])))
        
        # Additional chaotic and fractal-like component with recursive structure
        f8 = np.sum(np.sin(22.0 * x) * np.cos(28.0 * x) * np.sin(32.0 * x) * np.cos(36.0 * x) * np.exp(-0.05 * x**3))
        
        # Combined function with updated weights, normalization, and chaotic amplification
        return 0.30 * f1 + 0.22 * f2 + 0.19 * f3 + 0.14 * f4 + 0.13 * f5 + 0.09 * f6 + 0.07 * f7 + 0.06 * f8