import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic global minimum position based on dimension
        self.global_min = np.array([(-1)**i * 1.2 for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with varying frequencies
        r = np.sqrt(np.sum((x - self.global_min)**2))
        f1 = np.sin(6.0 * r) * np.exp(-0.15 * r)
        
        # Trigonometric interactions
        f2 = np.sum(np.cos(2.5 * x) * np.sin(3.5 * x))
        
        # Step-like penalty for proximity to boundaries
        boundary_penalty = np.sum(np.where(np.abs(x) > 4.2, (np.abs(x) - 4.2)**2.5, 0.0))
        
        # Polynomial coupling with mixed degrees
        f3 = np.sum(x**4 - 4 * x**3 + 3 * x**2 - x)
        
        # Exponential decay component
        f4 = np.sum(np.exp(-0.3 * (x - self.global_min)**2))
        
        # Chaotic sine composition
        f5 = np.sum(np.sin(np.pi * x) * np.cos(1.5 * np.pi * x))
        
        # Combine all components with varying weights
        return 0.35 * f1 + 0.15 * f2 + 0.1 * f3 + 0.2 * boundary_penalty + 0.15 * f4 + 0.1 * f5