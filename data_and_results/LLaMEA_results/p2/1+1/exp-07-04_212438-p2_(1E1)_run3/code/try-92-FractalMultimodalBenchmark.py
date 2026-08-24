import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with high-degree terms and dynamic coefficients
        coeffs = np.linspace(1.0, 10.0, self.dim)
        f1 = np.sum(coeffs * (x**13 + 0.5 * x**9 + 0.3 * x**7 + 0.1 * x**5))
        
        # Trigonometric component with varying frequencies and phase shifts
        f2 = np.sum(np.sin(20.0 * x) * np.cos(15.0 * x) * np.sin(25.0 * x) * np.cos(10.0 * x))
        
        # Fractal-like component with recursive structure and self-similarity
        f3 = np.sum(np.sin(30.0 * np.sin(15.0 * x)) * np.cos(25.0 * np.cos(10.0 * x)))
        
        # Cross-dimensional interaction terms with dynamic coupling
        f4 = np.sum(np.exp(-0.5 * np.sum((x[:-1] - x[1:])**2)) * np.sin(12.0 * (x[:-1] + x[1:])))
        
        # Multi-scale oscillatory component with varying amplitudes and frequencies
        f5 = np.sum(np.sin(50.0 * x) * np.cos(40.0 * x) * np.exp(-0.1 * np.abs(x)) * np.sin(3.0 * np.sum(x**2)))
        
        # Non-separable component with fractional powers and complex interactions
        f6 = np.sum((x[:-1]**1.5 + x[1:]**1.5)**2 * np.sin(20.0 * x[:-1]) * np.cos(20.0 * x[1:]))
        
        # Dynamic scaling component with exponential modulation
        f7 = np.sum(np.exp(0.5 * x**2) * np.sin(10.0 * x) * np.cos(15.0 * x))
        
        # Multi-modal chaotic component with feedback and time-delayed interactions
        f8 = np.sum(np.sin(40.0 * x) * np.cos(35.0 * x) * np.sin(30.0 * x) * np.cos(25.0 * x) * np.exp(-0.3 * np.abs(x)))
        
        # Combined function with adaptive weights and normalization
        return 0.25 * f1 + 0.20 * f2 + 0.18 * f3 + 0.15 * f4 + 0.12 * f5 + 0.10 * f6 + 0.08 * f7 + 0.07 * f8