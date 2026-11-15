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
        f1 = np.sum(x**11 - 6*x**6 + 8*x**4 - 4*x**3 + 2*x**2 - 1)
        
        # Modified trigonometric component with higher frequencies and phase shifts
        f2 = np.sum(np.sin(7.0 * x) * np.cos(9.0 * x) * np.sin(11.0 * x) * np.cos(13.0 * x) * np.sin(15.0 * x))
        
        # Advanced radial basis function with dynamic centers and variable widths
        centers = np.linspace(-4.0, 4.0, self.dim)
        widths = np.linspace(0.3, 2.5, self.dim)
        f3 = np.sum(np.exp(-0.3 * (x - centers)**2 / widths) * np.cos(3.0 * x))
        
        # Coupled oscillatory terms with variable coupling strength and time delays
        f4 = np.sum(np.sin(5.0 * x[:-1] * x[1:]) * np.cos(5.0 * (x[:-1] + x[1:])) * np.exp(-0.1 * np.abs(x[:-1] - x[1:])))
        
        # High-frequency chaotic-like component with feedback and modulation
        f5 = np.sum(np.sin(25.0 * x) * np.cos(30.0 * x) * np.exp(-0.05 * x**2) * np.sin(1.2 * np.sum(x**2)) * np.cos(0.5 * np.sum(x)))
        
        # Cross-term interaction with dynamic decay and multi-frequency modulation
        f6 = np.sum(np.exp(-0.4 * np.abs(x[:-1] - x[1:])) * np.sin(8.0 * (x[:-1] + x[1:])) * np.cos(5.0 * x[:-1]) * np.sin(3.0 * x[1:]))
        
        # Additional non-separable component with complex interactions and fractional powers
        f7 = np.sum((x[:-1] + x[1:])**5 * np.sin(6.0 * x[:-1]) * np.cos(6.0 * x[1:]) * np.exp(-0.2 * np.abs(x[:-1] - x[1:])))
        
        # Additional chaotic and fractal-like component with recursive structure
        f8 = np.sum(np.sin(18.0 * x) * np.cos(22.0 * x) * np.sin(26.0 * x) * np.cos(30.0 * x) * np.exp(-0.03 * x**3))
        
        # Combined function with updated weights, normalization, and chaotic amplification
        return 0.28 * f1 + 0.20 * f2 + 0.17 * f3 + 0.12 * f4 + 0.11 * f5 + 0.08 * f6 + 0.06 * f7 + 0.03 * f8