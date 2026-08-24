import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic global minimum position based on dimension
        self.global_min = np.array([(-1)**i * 2.0 for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with varying frequencies and amplitude modulation
        r = np.sqrt(np.sum((x - self.global_min)**2))
        f1 = np.sin(7.0 * r) * np.exp(-0.15 * r) * np.cos(0.5 * r)
        
        # Trigonometric interactions with higher frequency and phase shifts
        f2 = np.sum(np.sin(4.0 * x) * np.cos(3.0 * x) + np.sin(2.0 * x) * np.cos(5.0 * x))
        
        # Step-like penalty for proximity to boundaries with non-linear scaling
        boundary_penalty = np.sum(np.where(np.abs(x) > 4.2, (np.abs(x) - 4.2)**3, 0.0))
        
        # Polynomial coupling with mixed degrees and interaction terms
        f3 = np.sum(x**4 - 6 * x**3 + 11 * x**2 - 6 * x)
        
        # Exponential decay component with multi-modal peaks
        f4 = np.sum(np.exp(-0.3 * (x - self.global_min)**2) * np.sin(2.0 * x))
        
        # Chaotic sine composition with varying frequencies and coupling
        f5 = np.sum(np.sin(np.pi * x + np.sin(2.0 * x)) * np.cos(np.pi * x + np.cos(2.0 * x)))
        
        # Additional interference term to increase landscape complexity
        interference = np.sum(np.sin(10.0 * x) * np.cos(8.0 * x) * np.exp(-0.05 * r))
        
        # Combine all components with varying weights
        return 0.25 * f1 + 0.2 * f2 + 0.15 * f3 + 0.15 * boundary_penalty + 0.15 * f4 + 0.1 * f5 + 0.05 * interference