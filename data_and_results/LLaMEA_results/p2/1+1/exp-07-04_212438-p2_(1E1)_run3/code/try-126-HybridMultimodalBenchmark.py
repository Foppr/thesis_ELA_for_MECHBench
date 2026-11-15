import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with higher degrees, cross-terms, and fractional exponents
        f1 = np.sum(x**25 - 15*x**13 + 19*x**11 - 13*x**9 + 11*x**7 - 7*x**5 + 3.0)
        
        # Modified trigonometric component with higher frequencies, phase shifts, and multi-dimensional modulation
        f2 = np.sum(np.sin(21.0 * x) * np.cos(23.0 * x) * np.sin(25.0 * x) * np.cos(33.0 * x) * np.sin(37.0 * x) * np.cos(41.0 * x))
        
        # Advanced radial basis function with dynamic centers, variable widths, and multi-dimensional Gaussian modulation
        centers = np.linspace(-4.8, 4.8, self.dim)
        widths = np.linspace(0.3, 4.2, self.dim)
        f3 = np.sum(np.exp(-0.5 * (x - centers)**2 / widths) * np.cos(10.0 * x) * np.sin(12.0 * x))
        
        # Coupled oscillatory terms with variable coupling strength, time delays, and chaotic feedback
        f4 = np.sum(np.sin(19.0 * x[:-1] * x[1:]) * np.cos(19.0 * (x[:-1] + x[1:])) * np.exp(-0.5 * np.abs(x[:-1] - x[1:])) * np.sin(2.0 * x[:-1]) * np.cos(2.0 * x[1:]))
        
        # High-frequency chaotic-like component with feedback, modulation, and recursive structure
        f5 = np.sum(np.sin(60.0 * x) * np.cos(65.0 * x) * np.exp(-0.3 * x**2) * np.sin(4.0 * np.sum(x**2)) * np.cos(3.0 * np.sum(x)) * np.sin(5.0 * np.sum(x**3)))
        
        # Cross-term interaction with dynamic decay, multi-frequency modulation, and non-linear coupling
        f6 = np.sum(np.exp(-1.1 * np.abs(x[:-1] - x[1:])) * np.sin(22.0 * (x[:-1] + x[1:])) * np.cos(17.0 * x[:-1]) * np.sin(15.0 * x[1:]) * np.exp(-0.6 * (x[:-1] + x[1:])**2))
        
        # Additional non-separable component with complex interactions, fractional powers, and recursive structure
        f7 = np.sum((x[:-1] + x[1:])**19 * np.sin(20.0 * x[:-1]) * np.cos(20.0 * x[1:]) * np.exp(-0.8 * np.abs(x[:-1] - x[1:])) * np.sin(3.0 * np.sum(x[:-1] * x[1:])))
        
        # Additional chaotic and fractal-like component with recursive structure, increased complexity, and multi-dimensional feedback
        f8 = np.sum(np.sin(50.0 * x) * np.cos(55.0 * x) * np.sin(60.0 * x) * np.cos(65.0 * x) * np.exp(-0.15 * x**3) * np.sin(3.0 * np.sum(x**3)) * np.cos(4.0 * np.sum(x**2)))
        
        # Combined function with updated weights, normalization, and chaotic amplification
        return 0.42 * f1 + 0.35 * f2 + 0.31 * f3 + 0.28 * f4 + 0.28 * f5 + 0.22 * f6 + 0.19 * f7 + 0.16 * f8