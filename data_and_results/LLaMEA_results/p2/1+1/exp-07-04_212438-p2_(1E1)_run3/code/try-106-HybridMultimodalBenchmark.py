import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # High-degree polynomial with chaotic coefficients and cross-terms
        f1 = np.sum(19*x**23 - 25*x**19 + 21*x**17 - 19*x**15 + 17*x**13 - 15*x**11 + 13*x**9 - 11*x**7 + 9*x**5 - 7*x**3 + 5*x)
        
        # Multi-frequency trigonometric with dynamic phase modulation and coupling
        f2 = np.sum(np.sin(23.0 * x) * np.cos(27.0 * x) * np.sin(31.0 * x) * np.cos(37.0 * x) * np.sin(41.0 * x) * np.cos(43.0 * x))
        
        # Enhanced radial basis with fractal-like centers and variable widths
        centers = np.linspace(-4.8, 4.8, self.dim)
        widths = np.linspace(0.3, 4.5, self.dim)
        f3 = np.sum(np.exp(-0.3 * (x - centers)**2 / widths) * np.cos(12.0 * x) * np.sin(15.0 * x))
        
        # Stronger coupled oscillatory terms with time delays and variable coupling
        f4 = np.sum(np.sin(20.0 * x[:-1] * x[1:]) * np.cos(20.0 * (x[:-1] + x[1:])) * np.exp(-0.6 * np.abs(x[:-1] - x[1:])) * np.sin(10.0 * x[:-1]) * np.cos(10.0 * x[1:]))
        
        # Ultra-high frequency chaotic-like component with recursive feedback
        f5 = np.sum(np.sin(70.0 * x) * np.cos(75.0 * x) * np.exp(-0.3 * x**2) * np.sin(5.0 * np.sum(x**2)) * np.cos(3.0 * np.sum(x)) * np.sin(4.0 * np.sum(x**3)))
        
        # Complex cross-term interaction with fractional powers and multi-scale modulation
        f6 = np.sum(np.exp(-1.2 * np.abs(x[:-1] - x[1:])) * np.sin(25.0 * (x[:-1] + x[1:])) * np.cos(20.0 * x[:-1]) * np.sin(15.0 * x[1:]) * np.exp(-0.8 * np.abs(x[:-1] + x[1:])))
        
        # Advanced non-separable component with recursive structure and higher-order interactions
        f7 = np.sum((x[:-1] + x[1:])**20 * np.sin(20.0 * x[:-1]) * np.cos(20.0 * x[1:]) * np.exp(-0.9 * np.abs(x[:-1] - x[1:])) * np.sin(15.0 * np.sum(x**2)))
        
        # Fractal-like chaotic component with recursive structure and increased complexity
        f8 = np.sum(np.sin(60.0 * x) * np.cos(65.0 * x) * np.sin(70.0 * x) * np.cos(75.0 * x) * np.exp(-0.15 * x**3) * np.sin(3.0 * np.sum(x**3)) * np.cos(2.5 * np.sum(x**2)))
        
        # Combined function with updated weights, normalization, and chaotic amplification
        return 0.42 * f1 + 0.38 * f2 + 0.34 * f3 + 0.31 * f4 + 0.30 * f5 + 0.25 * f6 + 0.22 * f7 + 0.18 * f8