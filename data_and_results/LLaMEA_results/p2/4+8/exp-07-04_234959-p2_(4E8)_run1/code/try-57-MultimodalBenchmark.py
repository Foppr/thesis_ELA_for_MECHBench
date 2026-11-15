import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic global minimum position based on dimension with larger perturbation
        self.global_min = np.array([(-1)**i * 2.0 * np.sin(i * 0.5) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with higher frequencies and logarithmic scaling
        r = np.sqrt(np.sum((x - self.global_min)**2))
        f1 = np.sin(10.0 * r) * np.log(r + 1.0) * np.exp(-0.2 * r)
        
        # Trigonometric interactions with higher harmonics
        f2 = np.sum(np.cos(5.0 * x) * np.sin(7.0 * x) + np.sin(4.0 * x) * np.cos(6.0 * x))
        
        # Step-like penalty with logarithmic scaling for proximity to boundaries
        boundary_penalty = np.sum(np.where(np.abs(x) > 4.0, np.log(np.abs(x) - 3.0) * (np.abs(x) - 4.0)**2, 0.0))
        
        # Stronger polynomial coupling with mixed degrees and interaction terms
        f3 = np.sum(x**4 - 7 * x**3 + 15 * x**2 - 10 * x)
        
        # Exponential decay component with higher decay rate
        f4 = np.sum(np.exp(-0.8 * (x - self.global_min)**2))
        
        # Chaotic sine composition with fractional frequencies
        f5 = np.sum(np.sin(np.pi * x * 1.5) * np.cos(np.pi * x * 1.3))
        
        # Additional logarithmic barrier term
        log_barrier = np.sum(np.log(25.0 - (x**2)))
        
        # Combine all components with varying weights
        return 0.25 * f1 + 0.2 * f2 + 0.15 * f3 + 0.15 * boundary_penalty + 0.15 * f4 + 0.05 * f5 + 0.1 * log_barrier