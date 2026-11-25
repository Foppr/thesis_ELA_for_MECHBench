import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Chaotic sinusoidal perturbations with modified frequencies and amplitudes
        f2 = 0.4 * np.sum(np.sin(13.0 * x) * np.cos(8.0 * x) * np.exp(-0.15 * x**2))
        
        # Fractal-like structure with altered overlapping peaks and valleys
        f3 = 0.3 * np.sum(np.sin(19.0 * x) * np.sin(9.0 * x) * np.cos(5.0 * x) * np.exp(-0.05 * x**2))
        
        # Saddle points and ridges through modified trigonometric terms
        f4 = 0.15 * np.sum(np.sin(4.0 * x) * np.cos(12.0 * x) * x**2)
        
        # Complex cubic and quartic structure with adjusted coefficients
        f5 = 0.04 * np.sum(x**3 * np.sin(6.0 * x) + x**4 * np.cos(3.0 * x))
        
        # Enhanced non-smooth regions with logarithmic barrier
        f6 = 0.02 * np.sum(np.abs(x)**1.8)
        
        # New chaotic component with modified exponential decay and oscillations
        f7 = 0.25 * np.sum(np.sin(21.0 * x) * np.cos(14.0 * x) * np.exp(-0.35 * x**2) * np.sin(26.0 * x))
        
        # Additional fractal-like component with new frequency interactions
        f8 = 0.18 * np.sum(np.sin(23.0 * x) * np.cos(16.0 * x) * np.sin(12.0 * x) * np.exp(-0.25 * x**2))
        
        # Logarithmic barrier component to increase non-smoothness
        f9 = 0.1 * np.sum(np.log(1.0 + np.abs(x)) * np.sin(10.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9