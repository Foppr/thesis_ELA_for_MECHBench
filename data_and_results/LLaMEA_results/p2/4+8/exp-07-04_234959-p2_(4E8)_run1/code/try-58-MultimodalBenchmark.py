import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slightly perturbed global minimum position
        self.global_min = np.array([(-1)**i * 1.7 for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with higher frequency
        r = np.sqrt(np.sum((x - self.global_min)**2))
        f1 = np.sin(7.0 * r) * np.exp(-0.15 * r)
        
        # Trigonometric interactions with higher harmonics
        f2 = np.sum(np.cos(3.0 * x) * np.sin(4.0 * x))
        
        # Step-like penalty for proximity to boundaries
        boundary_penalty = np.sum(np.where(np.abs(x) > 4.2, (np.abs(x) - 4.2)**2, 0.0))
        
        # Enhanced polynomial coupling with mixed degrees
        f3 = np.sum(x**4 - 6 * x**3 + 3 * x**2 - x)
        
        # Exponential decay component with tighter spread
        f4 = np.sum(np.exp(-0.3 * (x - self.global_min)**2))
        
        # Chaotic sine composition with added phase shift
        f5 = np.sum(np.sin(np.pi * x + 0.5) * np.cos(np.pi * x + 0.5))
        
        # Combine all components with adjusted weights
        return 0.25 * f1 + 0.25 * f2 + 0.15 * f3 + 0.15 * boundary_penalty + 0.1 * f4 + 0.1 * f5