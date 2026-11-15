import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial component with extremely high degrees and cross-terms
        f1 = np.sum(x**31 - 23*x**17 + 37*x**13 - 29*x**11 + 23*x**9 - 17*x**7 + 13*x**5 - 7.0)
        
        # Modified trigonometric component with extremely high frequencies and phase shifts
        f2 = np.sum(np.sin(31.0 * x) * np.cos(37.0 * x) * np.sin(41.0 * x) * np.cos(47.0 * x) * np.sin(53.0 * x) * np.cos(59.0 * x))
        
        # Advanced radial basis function with dynamic centers and variable widths
        centers = np.linspace(-4.9, 4.9, self.dim)
        widths = np.linspace(0.2, 6.0, self.dim)
        f3 = np.sum(np.exp(-0.5 * (x - centers)**2 / widths) * np.cos(12.0 * x) * np.sin(13.0 * x))
        
        # Coupled oscillatory terms with variable coupling strength and time delays
        f4 = np.sum(np.sin(25.0 * x[:-1] * x[1:]) * np.cos(25.0 * (x[:-1] + x[1:])) * np.exp(-0.6 * np.abs(x[:-1] - x[1:])) * np.sin(7.0 * x[:-1]) * np.cos(7.0 * x[1:]))
        
        # High-frequency chaotic-like component with feedback and modulation
        f5 = np.sum(np.sin(80.0 * x) * np.cos(85.0 * x) * np.exp(-0.3 * x**2) * np.sin(5.0 * np.sum(x**2)) * np.cos(3.0 * np.sum(x)) * np.sin(4.0 * np.sum(x**3)))
        
        # Cross-term interaction with dynamic decay and multi-frequency modulation
        f6 = np.sum(np.exp(-1.2 * np.abs(x[:-1] - x[1:])) * np.sin(25.0 * (x[:-1] + x[1:])) * np.cos(20.0 * x[:-1]) * np.sin(17.0 * x[1:]) * np.cos(15.0 * x[:-1]) * np.sin(13.0 * x[1:]))
        
        # Additional non-separable component with complex interactions and fractional powers
        f7 = np.sum((x[:-1] + x[1:])**25 * np.sin(25.0 * x[:-1]) * np.cos(25.0 * x[1:]) * np.exp(-1.0 * np.abs(x[:-1] - x[1:])) * np.sin(10.0 * x[:-1]) * np.cos(10.0 * x[1:]))
        
        # Additional chaotic and fractal-like component with recursive structure and increased complexity
        f8 = np.sum(np.sin(70.0 * x) * np.cos(75.0 * x) * np.sin(80.0 * x) * np.cos(85.0 * x) * np.exp(-0.15 * x**3) * np.sin(3.0 * np.sum(x**3)) * np.cos(2.5 * np.sum(x**2)))
        
        # Combined function with updated weights, normalization, and chaotic amplification
        return 0.42 * f1 + 0.38 * f2 + 0.35 * f3 + 0.32 * f4 + 0.30 * f5 + 0.25 * f6 + 0.22 * f7 + 0.18 * f8