import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like structure with recursive trigonometric transformations
        f1 = 0.3 * np.sum(np.sin(2.0 * np.pi * x) * np.cos(3.0 * np.pi * x) * np.sin(5.0 * np.pi * x))
        
        # Asymmetric polynomial coupling with exponential weights
        f2 = 0.25 * np.sum((x**3 + 0.3 * x**4 + 0.05 * x**5) * np.exp(-0.1 * np.abs(x)))
        
        # Multi-scale noise modulation with dynamic frequency adjustment
        noise = np.sin(0.2 * np.sum(x**2)) * np.cos(0.1 * np.sum(x))
        f3 = 0.2 * np.sum(np.exp(-0.05 * np.abs(x)) * np.sin(12.0 * x) * noise)
        
        # Saddle point distribution with hyperbolic and polynomial components
        f4 = 0.2 * np.sum(np.tanh(x) * (x**2 - 1.0) * np.cos(4.0 * x))
        
        # Cross-term coupling with logarithmic distance scaling
        f5 = 0.15 * np.sum(np.log(np.abs(x) + 1.0) * np.sin(6.0 * x) * np.cos(4.0 * x))
        
        # Enhanced radial component with multiple frequency harmonics
        r = np.sqrt(np.sum(x**2))
        f6 = 0.1 * (1.0 + np.sin(4.0 * r) * np.cos(3.0 * r) * np.sin(6.0 * r) * np.cos(2.0 * r))
        
        # Modified Gaussian interaction term with adaptive variance
        f7 = 0.1 * np.sum(np.exp(-0.5 * (x**2) / (0.5 + 0.5 * np.abs(x))) * np.sin(8.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7