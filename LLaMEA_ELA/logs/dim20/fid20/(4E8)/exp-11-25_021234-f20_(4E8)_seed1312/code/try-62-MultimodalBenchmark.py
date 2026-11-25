import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with adaptive scaling
        f2 = 0.5 * np.sum(np.sin(15.0 * x) * np.cos(11.0 * x) * np.exp(-0.2 * x**2))
        
        # Modified fractal-like structure with overlapping peaks and valleys
        f3 = 0.4 * np.sum(np.sin(20.0 * x) * np.sin(12.0 * x) * np.cos(8.0 * x) * np.exp(-0.1 * x**2))
        
        # Saddle points and ridges with modified trigonometric interactions
        f4 = 0.2 * np.sum(np.sin(6.0 * x) * np.cos(13.0 * x) * x**1.5)
        
        # Complex polynomial and trigonometric structure for increased landscape complexity
        f5 = 0.05 * np.sum(x**3 * np.sin(8.0 * x) + x**4 * np.cos(5.0 * x))
        
        # Enhanced non-smooth regions with fractional power terms
        f6 = 0.03 * np.sum(np.abs(x)**1.9)
        
        # New chaotic component with multi-scale oscillations and exponential decay
        f7 = 0.3 * np.sum(np.sin(25.0 * x) * np.cos(20.0 * x) * np.exp(-0.4 * x**2) * np.sin(30.0 * x))
        
        # Additional fractal-like component with asymmetric wave interference
        f8 = 0.2 * np.sum(np.sin(24.0 * x) * np.cos(19.0 * x) * np.sin(15.0 * x) * np.exp(-0.3 * x**2))
        
        # Adaptive scaling factor to balance contribution of different components
        scale_factor = 1.0 + 0.1 * np.sin(0.5 * np.sum(x**2))
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)