import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic global minimum position based on dimension
        self.global_min = np.array([(-1)**i * 1.5 for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with varying frequencies and chaotic modulation
        r = np.sqrt(np.sum((x - self.global_min)**2))
        f1 = np.sin(5.0 * r) * np.exp(-0.1 * r) * np.sin(0.5 * r**2)
        
        # Trigonometric interactions with dynamic phase shifts
        f2 = np.sum(np.cos(2.0 * x + np.sin(x)) * np.sin(3.0 * x + np.cos(x)))
        
        # Step-like penalty for proximity to boundaries with non-linear scaling
        boundary_penalty = np.sum(np.where(np.abs(x) > 4.0, (np.abs(x) - 4.0)**3, 0.0))
        
        # Polynomial coupling with mixed degrees and chaotic coefficients
        coeffs = np.sin(np.arange(self.dim) * 0.5) + 1.0
        f3 = np.sum(coeffs * (x**3 - 5 * x**2 + 2 * x))
        
        # Exponential decay component with dynamic centering
        f4 = np.sum(np.exp(-0.5 * (x - self.global_min)**2) * np.cos(0.3 * x))
        
        # Chaotic sine composition with multiple frequencies
        f5 = np.sum(np.sin(np.pi * x) * np.cos(np.pi * x) * np.sin(2 * np.pi * x))
        
        # Additional chaotic interference term
        chaotic_term = np.sum(np.sin(10.0 * x) * np.cos(7.0 * x))
        
        # Combine all components with varying weights
        return 0.25 * f1 + 0.2 * f2 + 0.1 * f3 + 0.15 * boundary_penalty + 0.15 * f4 + 0.1 * f5 + 0.05 * chaotic_term