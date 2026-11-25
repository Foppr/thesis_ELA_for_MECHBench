import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Chaotic sinusoidal perturbations with varying frequencies and amplitudes
        f2 = 0.3 * np.sum(np.sin(10.0 * x) * np.cos(7.0 * x) * np.exp(-0.2 * x**2))
        
        # Add fractal-like structure with multiple overlapping peaks and valleys
        f3 = 0.25 * np.sum(np.sin(15.0 * x) * np.sin(8.0 * x) * np.cos(5.0 * x) * np.exp(-0.1 * x**2))
        
        # Introduce saddle points and ridges through mixed trigonometric terms
        f4 = 0.1 * np.sum(np.sin(4.0 * x) * np.cos(9.0 * x) * x**2)
        
        # Add a complex cubic and quartic structure for enhanced landscape complexity
        f5 = 0.03 * np.sum(x**3 * np.sin(6.0 * x) + x**4 * np.cos(3.0 * x))
        
        # Include a small fractional power term to create non-smooth regions
        f6 = 0.01 * np.sum(np.abs(x)**1.7)
        
        return f1 + f2 + f3 + f4 + f5 + f6