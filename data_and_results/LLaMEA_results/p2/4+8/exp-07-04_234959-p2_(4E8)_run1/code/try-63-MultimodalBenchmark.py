import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic global minimum position based on dimension
        self.global_min = np.array([(-1)**i * 2.0 for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees
        f1 = np.sum(x**4 - 6 * x**2 + 4 * x)
        
        # Exponential decay component with dynamic center
        f2 = np.sum(np.exp(-0.5 * (x - self.global_min)**2))
        
        # Trigonometric interference with varying frequencies
        f3 = np.sum(np.sin(3.0 * x) * np.cos(2.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Radial sine component with dynamic scaling
        r = np.sqrt(np.sum((x - self.global_min)**2))
        f4 = np.sin(4.0 * r) * np.exp(-0.2 * r)
        
        # Step-like penalty for proximity to boundaries
        boundary_penalty = np.sum(np.where(np.abs(x) > 4.0, (np.abs(x) - 4.0)**3, 0.0))
        
        # Adaptive noise component
        noise = np.random.normal(0, 0.01, self.dim)
        f5 = np.sum(noise * x**2)
        
        # Combine all components with varying weights
        return 0.25 * f1 + 0.2 * f2 + 0.15 * f3 + 0.2 * f4 + 0.15 * boundary_penalty + 0.05 * f5