import numpy as np

class FractalGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors
        self.fractal_scale = np.array([1.0 / (2**i) for i in range(dim)])
    
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dimension scaling
        f1 = 0.3 * np.sum(x**2) / self.dim
        
        # Fractal-like pattern with recursive sine-cosine combinations
        f2 = 0.4 * np.sum(np.sin(20.0 * np.sin(5.0 * x)) * np.cos(15.0 * np.cos(3.0 * x)))
        
        # Adaptive gradient field with dimension-dependent weights
        grad_field = np.zeros_like(x)
        for i in range(self.dim):
            if i < self.dim - 1:
                grad_field[i] = np.sin(x[i]) * np.cos(x[i+1])
            else:
                grad_field[i] = np.sin(x[i]) * np.cos(x[0])
        f3 = 0.25 * np.sum(grad_field**2)
        
        # Dynamic penalty based on distance from center with fractal scaling
        center_distance = np.sqrt(np.sum(x**2))
        penalty = 0.3 * np.exp(-center_distance / 3.0) * (1.0 + 0.5 * np.sin(10.0 * center_distance))
        f4 = penalty
        
        # Multi-scale oscillation with varying amplitudes and frequencies
        f5 = 0.2 * np.sum(np.sin(50.0 * x * self.fractal_scale) * np.cos(30.0 * x * self.fractal_scale))
        
        # Dimensional coupling with exponential weighting
        coupling = 0.15 * np.sum(np.exp(-0.5 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2))
        f6 = coupling
        
        # Nested local minima with chaotic perturbations
        nested = 0.2 * np.sum(np.sin(100.0 * x) * np.cos(75.0 * x) * np.exp(-0.1 * x**2))
        f7 = nested
        
        # Asymmetric conditioning with step-function behavior
        condition = np.where(x > 0, x**1.5, -x**1.3)
        f8 = 0.18 * np.sum(condition)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8