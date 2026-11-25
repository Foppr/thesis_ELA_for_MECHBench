import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Multiple overlapping sinusoidal wells with adaptive frequency modulation
        f2 = 0.3 * np.sum(np.sin(8.0 * x + 0.7) * np.exp(-0.15 * x**2))
        
        # Chaotic sinusoidal modulations with saddle points
        f3 = 0.25 * np.sum(np.cos(12.0 * x - 0.4) * np.exp(-0.1 * x**2))
        
        # Fractal-like terrain with exponential decay
        f4 = 0.18 * np.sum(np.sin(15.0 * x + 0.2) * np.exp(-0.3 * np.abs(x)) * np.cos(5.0 * x))
        
        # Additional cosine modulation for increased complexity
        f5 = 0.12 * np.sum(np.cos(20.0 * x - 0.6) * np.exp(-0.08 * x**2))
        
        # Shifted sine perturbations to create deceptive minima
        f6 = 0.08 * np.sum(np.sin(25.0 * (x + 0.3)) * np.exp(-0.2 * x**2))
        
        # Cubic and quartic terms for additional landscape complexity
        f7 = 0.01 * np.sum(x**3)
        f8 = 0.005 * np.sum(x**4)
        
        # Add a novel adaptive scaling factor
        adaptive_scale = 1.0 + 0.5 * np.sin(0.5 * np.sum(x**2))
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)