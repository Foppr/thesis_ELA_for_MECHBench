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
        f2 = 0.4 * np.sum(np.sin(12.0 * x) * np.cos(9.0 * x) * np.exp(-0.15 * x**2))
        
        # Add fractal-like structure with multiple overlapping peaks and valleys
        f3 = 0.3 * np.sum(np.sin(18.0 * x) * np.sin(10.0 * x) * np.cos(6.0 * x) * np.exp(-0.05 * x**2))
        
        # Introduce saddle points and ridges through mixed trigonometric terms
        f4 = 0.15 * np.sum(np.sin(5.0 * x) * np.cos(11.0 * x) * x**2)
        
        # Add a complex cubic and quartic structure for enhanced landscape complexity
        f5 = 0.04 * np.sum(x**3 * np.sin(7.0 * x) + x**4 * np.cos(4.0 * x))
        
        # Include a stronger fractional power term to create more pronounced non-smooth regions
        f6 = 0.02 * np.sum(np.abs(x)**1.8)
        
        # Add a new chaotic component with exponential decay and high-frequency oscillations
        f7 = 0.25 * np.sum(np.sin(20.0 * x) * np.cos(15.0 * x) * np.exp(-0.3 * x**2) * np.sin(25.0 * x))
        
        # Add a new fractal-like component with multiple overlapping sine waves
        f8 = 0.18 * np.sum(np.sin(22.0 * x) * np.cos(17.0 * x) * np.sin(13.0 * x) * np.exp(-0.25 * x**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8