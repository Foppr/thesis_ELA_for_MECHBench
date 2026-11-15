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
        f1 = np.sum(x**21 - 13*x**11 + 17*x**9 - 11*x**7 + 9*x**5 - 5.0)
        
        # Modified trigonometric component with higher frequencies and phase shifts
        f2 = np.sum(np.sin(17.0 * x) * np.cos(19.0 * x) * np.sin(21.0 * x) * np.cos(29.0 * x) * np.sin(31.0 * x))
        
        # Advanced radial basis function with dynamic centers and variable widths
        centers = np.linspace(-4.9, 4.9, self.dim)
        widths = np.linspace(0.4, 4.0, self.dim)
        f3 = np.sum(np.exp(-0.5 * (x - centers)**2 / widths) * np.cos(8.0 * x))
        
        # Coupled oscillatory terms with variable coupling strength and time delays
        f4 = np.sum(np.sin(15.0 * x[:-1] * x[1:]) * np.cos(15.0 * (x[:-1] + x[1:])) * np.exp(-0.4 * np.abs(x[:-1] - x[1:])))
        
        # High-frequency chaotic-like component with feedback and modulation
        f5 = np.sum(np.sin(50.0 * x) * np.cos(55.0 * x) * np.exp(-0.2 * x**2) * np.sin(3.5 * np.sum(x**2)) * np.cos(2.0 * np.sum(x)))
        
        # Cross-term interaction with dynamic decay and multi-frequency modulation
        f6 = np.sum(np.exp(-0.9 * np.abs(x[:-1] - x[1:])) * np.sin(18.0 * (x[:-1] + x[1:])) * np.cos(13.0 * x[:-1]) * np.sin(11.0 * x[1:]))
        
        # Additional non-separable component with complex interactions and fractional powers
        f7 = np.sum((x[:-1] + x[1:])**15 * np.sin(16.0 * x[:-1]) * np.cos(16.0 * x[1:]) * np.exp(-0.7 * np.abs(x[:-1] - x[1:])))
        
        # Additional chaotic and fractal-like component with recursive structure and increased complexity
        f8 = np.sum(np.sin(40.0 * x) * np.cos(45.0 * x) * np.sin(50.0 * x) * np.cos(55.0 * x) * np.exp(-0.1 * x**3) * np.sin(2.0 * np.sum(x**3)))
        
        # Combined function with updated weights, normalization, and chaotic amplification
        return 0.4 * f1 + 0.3 * f2 + 0.25 * f3 + 0.22 * f4 + 0.22 * f5 + 0.16 * f6 + 0.13 * f7 + 0.1 * f8