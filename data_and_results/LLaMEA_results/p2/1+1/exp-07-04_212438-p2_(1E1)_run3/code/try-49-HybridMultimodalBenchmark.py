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
        f1 = np.sum(x**19 - 11*x**10 + 15*x**8 - 9*x**6 + 7*x**4 - 4.0)
        
        # Modified trigonometric component with higher frequencies and phase shifts
        f2 = np.sum(np.sin(15.0 * x) * np.cos(17.0 * x) * np.sin(19.0 * x) * np.cos(25.0 * x) * np.sin(27.0 * x))
        
        # Advanced radial basis function with dynamic centers and variable widths
        centers = np.linspace(-4.8, 4.8, self.dim)
        widths = np.linspace(0.3, 3.8, self.dim)
        f3 = np.sum(np.exp(-0.5 * (x - centers)**2 / widths) * np.cos(7.0 * x))
        
        # Coupled oscillatory terms with variable coupling strength and time delays
        f4 = np.sum(np.sin(13.0 * x[:-1] * x[1:]) * np.cos(13.0 * (x[:-1] + x[1:])) * np.exp(-0.3 * np.abs(x[:-1] - x[1:])))
        
        # High-frequency chaotic-like component with feedback and modulation
        f5 = np.sum(np.sin(45.0 * x) * np.cos(50.0 * x) * np.exp(-0.15 * x**2) * np.sin(3.0 * np.sum(x**2)) * np.cos(1.5 * np.sum(x)))
        
        # Cross-term interaction with dynamic decay and multi-frequency modulation
        f6 = np.sum(np.exp(-0.8 * np.abs(x[:-1] - x[1:])) * np.sin(16.0 * (x[:-1] + x[1:])) * np.cos(11.0 * x[:-1]) * np.sin(9.0 * x[1:]))
        
        # Additional non-separable component with complex interactions and fractional powers
        f7 = np.sum((x[:-1] + x[1:])**13 * np.sin(14.0 * x[:-1]) * np.cos(14.0 * x[1:]) * np.exp(-0.6 * np.abs(x[:-1] - x[1:])))
        
        # Additional chaotic and fractal-like component with recursive structure
        f8 = np.sum(np.sin(35.0 * x) * np.cos(40.0 * x) * np.sin(45.0 * x) * np.cos(50.0 * x) * np.exp(-0.08 * x**3))
        
        # Combined function with updated weights, normalization, and chaotic amplification
        return 0.37 * f1 + 0.27 * f2 + 0.24 * f3 + 0.19 * f4 + 0.19 * f5 + 0.14 * f6 + 0.11 * f7 + 0.08 * f8