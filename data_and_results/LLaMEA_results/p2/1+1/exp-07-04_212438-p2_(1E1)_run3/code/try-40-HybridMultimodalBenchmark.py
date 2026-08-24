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
        f1 = np.sum(x**17 - 10*x**9 + 13*x**7 - 8*x**5 + 6*x**3 - 3.0)
        
        # Modified trigonometric component with higher frequencies and phase shifts
        f2 = np.sum(np.sin(13.0 * x) * np.cos(15.0 * x) * np.sin(17.0 * x) * np.cos(23.0 * x) * np.sin(25.0 * x))
        
        # Advanced radial basis function with dynamic centers and variable widths
        centers = np.linspace(-4.9, 4.9, self.dim)
        widths = np.linspace(0.4, 4.0, self.dim)
        f3 = np.sum(np.exp(-0.5 * (x - centers)**2 / widths) * np.cos(6.0 * x))
        
        # Coupled oscillatory terms with variable coupling strength and time delays
        f4 = np.sum(np.sin(11.0 * x[:-1] * x[1:]) * np.cos(11.0 * (x[:-1] + x[1:])) * np.exp(-0.25 * np.abs(x[:-1] - x[1:])))
        
        # High-frequency chaotic-like component with feedback and modulation
        f5 = np.sum(np.sin(40.0 * x) * np.cos(45.0 * x) * np.exp(-0.1 * x**2) * np.sin(2.5 * np.sum(x**2)) * np.cos(1.0 * np.sum(x)))
        
        # Slightly modified cross-term interaction with dynamic decay and multi-frequency modulation
        f6 = np.sum(np.exp(-0.7 * np.abs(x[:-1] - x[1:])) * np.sin(14.0 * (x[:-1] + x[1:])) * np.cos(10.0 * x[:-1]) * np.sin(8.0 * x[1:]) * 0.9)
        
        # Additional non-separable component with complex interactions and fractional powers
        f7 = np.sum((x[:-1] + x[1:])**11 * np.sin(12.0 * x[:-1]) * np.cos(12.0 * x[1:]) * np.exp(-0.5 * np.abs(x[:-1] - x[1:])) * 1.1)
        
        # Additional chaotic and fractal-like component with recursive structure
        f8 = np.sum(np.sin(30.0 * x) * np.cos(35.0 * x) * np.sin(40.0 * x) * np.cos(45.0 * x) * np.exp(-0.07 * x**3) * 0.8)
        
        # Combined function with updated weights, normalization, and chaotic amplification
        return 0.35 * f1 + 0.25 * f2 + 0.22 * f3 + 0.18 * f4 + 0.17 * f5 + 0.12 * f6 + 0.09 * f7 + 0.06 * f8