import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component with adaptive conditioning
        f1 = np.sum(0.1 * x**2 + 0.01 * x**4 + 0.001 * x**6)
        
        # Chaotic sinusoidal modulation with exponential decay
        f2 = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(10.0 * np.exp(0.5 * x)) * np.cos(15.0 * np.exp(0.3 * x)))
        
        # Nested oscillatory terms with varying frequencies and amplitudes
        f3 = np.sum(np.sin(20.0 * x) * np.cos(25.0 * x) * np.exp(-0.05 * x**2) * np.sin(5.0 * np.sum(x**2)))
        
        # Multi-scale fractal-like structure with recursive interactions
        f4 = np.sum(np.sin(30.0 * x) * np.cos(35.0 * x) * np.sin(40.0 * x) * np.cos(45.0 * x) * 
                   np.exp(-0.2 * np.abs(x)) * np.sin(2.0 * np.sum(x**3)))
        
        # Gradient-based component with directional sensitivity and sharp transitions
        grad_term = np.zeros_like(x)
        for i in range(self.dim - 1):
            grad_term[i] += (x[i+1] - x[i])**2 * np.exp(-0.1 * np.abs(x[i] + x[i+1]))
        f5 = np.sum(grad_term)
        
        # Adaptive conditioning with exponential scaling
        f6 = np.sum(np.exp(0.5 * x**2) * np.sin(8.0 * x) * np.cos(12.0 * x) * 
                   np.exp(-0.3 * np.abs(x)) * np.sin(3.0 * np.sum(x**2)))
        
        # Cross-dimensional coupling with dynamic weights
        f7 = np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * 
                   np.sin(18.0 * (x[:-1] + x[1:])) * 
                   np.cos(14.0 * (x[:-1] - x[1:])) * 
                   np.exp(-0.1 * np.abs(x[:-1] + x[1:])))
        
        # High-frequency chaotic component with feedback loops
        f8 = np.sum(np.sin(60.0 * x) * np.cos(65.0 * x) * 
                   np.exp(-0.08 * x**2) * 
                   np.sin(4.0 * np.sum(np.sin(x))) * 
                   np.cos(3.0 * np.sum(np.cos(x))))
        
        # Combine all components with dynamic weighting
        return 0.3 * f1 + 0.25 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5 + 0.08 * f6 + 0.05 * f7 + 0.02 * f8