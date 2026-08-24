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
        f1 = np.sum(x**23 - 15*x**13 + 19*x**11 - 13*x**9 + 11*x**7 - 7.0)
        
        # Modified trigonometric component with higher frequencies and phase shifts
        f2 = np.sum(np.sin(19.0 * x) * np.cos(21.0 * x) * np.sin(23.0 * x) * np.cos(33.0 * x) * np.sin(37.0 * x))
        
        # Advanced radial basis function with dynamic centers and variable widths
        centers = np.linspace(-4.8, 4.8, self.dim)
        widths = np.linspace(0.3, 3.8, self.dim)
        f3 = np.sum(np.exp(-0.5 * (x - centers)**2 / widths) * np.cos(9.0 * x))
        
        # Coupled oscillatory terms with variable coupling strength and time delays
        f4 = np.sum(np.sin(17.0 * x[:-1] * x[1:]) * np.cos(17.0 * (x[:-1] + x[1:])) * np.exp(-0.3 * np.abs(x[:-1] - x[1:])))
        
        # High-frequency chaotic-like component with feedback and modulation
        f5 = np.sum(np.sin(55.0 * x) * np.cos(60.0 * x) * np.exp(-0.25 * x**2) * np.sin(4.0 * np.sum(x**2)) * np.cos(2.5 * np.sum(x)))
        
        # Cross-term interaction with dynamic decay and multi-frequency modulation
        f6 = np.sum(np.exp(-0.85 * np.abs(x[:-1] - x[1:])) * np.sin(20.0 * (x[:-1] + x[1:])) * np.cos(15.0 * x[:-1]) * np.sin(13.0 * x[1:]))
        
        # Additional non-separable component with complex interactions and fractional powers
        f7 = np.sum((x[:-1] + x[1:])**17 * np.sin(18.0 * x[:-1]) * np.cos(18.0 * x[1:]) * np.exp(-0.6 * np.abs(x[:-1] - x[1:])))
        
        # Additional chaotic and fractal-like component with recursive structure and increased complexity
        f8 = np.sum(np.sin(45.0 * x) * np.cos(50.0 * x) * np.sin(55.0 * x) * np.cos(60.0 * x) * np.exp(-0.15 * x**3) * np.sin(2.5 * np.sum(x**3)))
        
        # Combined function with updated weights, normalization, and chaotic amplification
        return 0.40 * f1 + 0.30 * f2 + 0.25 * f3 + 0.22 * f4 + 0.22 * f5 + 0.16 * f6 + 0.14 * f7 + 0.10 * f8