import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with altered frequency ratios
        f2 = 0.5 * np.sum(np.sin(19.0 * x) * np.cos(13.0 * x) * np.exp(-0.25 * x**2))
        
        # Fractal-like structure with overlapping peaks and valleys
        f3 = 0.4 * np.sum(np.sin(25.0 * x) * np.sin(15.0 * x) * np.cos(9.0 * x) * np.exp(-0.15 * x**2))
        
        # Saddle points and ridges through modified trigonometric terms
        f4 = 0.2 * np.sum(np.sin(7.0 * x) * np.cos(20.0 * x) * x**2)
        
        # Complex cubic and quartic structure with adjusted coefficients
        f5 = 0.05 * np.sum(x**3 * np.sin(9.0 * x) + x**4 * np.cos(6.0 * x))
        
        # Enhanced non-smooth regions with logarithmic barrier
        f6 = 0.03 * np.sum(np.abs(x)**1.8)
        
        # New chaotic component with modified exponential decay and oscillations
        f7 = 0.3 * np.sum(np.sin(27.0 * x) * np.cos(19.0 * x) * np.exp(-0.45 * x**2) * np.sin(32.0 * x))
        
        # Additional fractal-like component with new frequency interactions
        f8 = 0.2 * np.sum(np.sin(29.0 * x) * np.cos(21.0 * x) * np.sin(17.0 * x) * np.exp(-0.35 * x**2))
        
        # Enhanced logarithmic barrier component to increase non-smoothness
        f9 = 0.15 * np.sum(np.log(1.0 + np.abs(x)) * np.sin(14.0 * x))
        
        # Additional ridge structure with modified amplitude
        f10 = 0.1 * np.sum(np.cos(11.0 * x) * np.exp(-0.2 * x**2) * x**3)
        
        # Cross-term interactions to increase complexity
        f11 = 0.08 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x) * np.sin(8.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11