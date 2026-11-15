import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic global minimum position based on dimension
        self.global_min = np.array([(-1)**i * 2.0 for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with varying frequencies
        r = np.sqrt(np.sum((x - self.global_min)**2))
        f1 = np.sin(7.0 * r) * np.exp(-0.15 * r)
        
        # Trigonometric interactions
        f2 = np.sum(np.cos(3.0 * x) * np.sin(4.0 * x))
        
        # Step-like penalty for proximity to boundaries
        boundary_penalty = np.sum(np.where(np.abs(x) > 4.2, (np.abs(x) - 4.2)**2, 0.0))
        
        # Polynomial coupling with mixed degrees
        f3 = np.sum(x**4 - 6 * x**3 + 3 * x**2)
        
        # Exponential decay component
        f4 = np.sum(np.exp(-0.3 * (x - self.global_min)**2))
        
        # Chaotic sine composition
        f5 = np.sum(np.sin(2.0 * np.pi * x) * np.cos(2.0 * np.pi * x))
        
        # Combine all components with varying weights
        return 0.25 * f1 + 0.25 * f2 + 0.15 * f3 + 0.15 * boundary_penalty + 0.1 * f4 + 0.1 * f5