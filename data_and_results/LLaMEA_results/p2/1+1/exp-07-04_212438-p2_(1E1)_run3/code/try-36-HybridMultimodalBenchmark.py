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
        f1 = np.sum(x**15 - 9*x**8 + 11*x**6 - 7*x**4 + 5*x**2 - 2.0)
        
        # Modified trigonometric component with higher frequencies and phase shifts
        f2 = np.sum(np.sin(11.0 * x) * np.cos(13.0 * x) * np.sin(15.0 * x) * np.cos(19.0 * x) * np.sin(21.0 * x))
        
        # Advanced radial basis function with dynamic centers and variable widths
        centers = np.linspace(-4.8, 4.8, self.dim)
        widths = np.linspace(0.3, 3.5, self.dim)
        f3 = np.sum(np.exp(-0.5 * (x - centers)**2 / widths) * np.cos(5.0 * x))
        
        # Coupled oscillatory terms with variable coupling strength and time delays
        f4 = np.sum(np.sin(9.0 * x[:-1] * x[1:]) * np.cos(9.0 * (x[:-1] + x[1:])) * np.exp(-0.2 * np.abs(x[:-1] - x[1:])))
        
        # High-frequency chaotic-like component with feedback and modulation
        f5 = np.sum(np.sin(35.0 * x) * np.cos(40.0 * x) * np.exp(-0.08 * x**2) * np.sin(2.0 * np.sum(x**2)) * np.cos(0.8 * np.sum(x)))
        
        # Cross-term interaction with dynamic decay and multi-frequency modulation
        f6 = np.sum(np.exp(-0.6 * np.abs(x[:-1] - x[1:])) * np.sin(12.0 * (x[:-1] + x[1:])) * np.cos(9.0 * x[:-1]) * np.sin(7.0 * x[1:]))
        
        # Additional non-separable component with complex interactions and fractional powers
        f7 = np.sum((x[:-1] + x[1:])**9 * np.sin(10.0 * x[:-1]) * np.cos(10.0 * x[1:]) * np.exp(-0.4 * np.abs(x[:-1] - x[1:])))
        
        # Additional chaotic and fractal-like component with recursive structure
        f8 = np.sum(np.sin(25.0 * x) * np.cos(30.0 * x) * np.sin(35.0 * x) * np.cos(40.0 * x) * np.exp(-0.06 * x**3))
        
        # Combined function with updated weights, normalization, and chaotic amplification
        return 0.32 * f1 + 0.24 * f2 + 0.20 * f3 + 0.16 * f4 + 0.15 * f5 + 0.10 * f6 + 0.08 * f7 + 0.05 * f8