import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with altered degrees and enhanced non-separability
        f1 = np.sum(x**9 - 5*x**5 + 7*x**3 - 3*x**2 + 1)
        
        # Trigonometric component with modified frequencies and phase shifts
        f2 = np.sum(np.sin(5.0 * x) * np.cos(7.0 * x) * np.sin(9.0 * x) * np.cos(11.0 * x))
        
        # Radial basis function with shifted centers and scaled widths
        centers = np.linspace(-3.5, 3.5, self.dim)
        widths = np.linspace(0.4, 2.2, self.dim)
        f3 = np.sum(np.exp(-0.5 * (x - centers)**2 / widths))
        
        # Coupled oscillatory terms with modified coupling strength
        f4 = np.sum(np.sin(4.0 * x[:-1] * x[1:]) * np.cos(4.0 * (x[:-1] + x[1:])))
        
        # High-frequency chaotic-like component with modified feedback
        f5 = np.sum(np.sin(22.0 * x) * np.cos(27.0 * x) * np.exp(-0.04 * x**2) * np.sin(0.8 * np.sum(x**2)))
        
        # Cross-term interaction with modified decay and modulation
        f6 = np.sum(np.exp(-0.5 * np.abs(x[:-1] - x[1:])) * np.sin(7.0 * (x[:-1] + x[1:])) * np.cos(4.0 * x[:-1]))
        
        # Additional non-separable component with altered interactions
        f7 = np.sum((x[:-1] + x[1:])**4 * np.sin(5.0 * x[:-1]) * np.cos(5.0 * x[1:]))
        
        # Combined function with updated weights and normalization
        return 0.33 * f1 + 0.22 * f2 + 0.19 * f3 + 0.13 * f4 + 0.10 * f5 + 0.07 * f6 + 0.06 * f7