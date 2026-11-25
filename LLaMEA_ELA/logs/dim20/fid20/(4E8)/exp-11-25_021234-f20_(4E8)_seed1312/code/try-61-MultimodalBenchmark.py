import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Chaotic sinusoidal perturbations with altered frequencies and amplitudes
        f2 = 0.4 * np.sum(np.sin(13.0 * x) * np.cos(8.0 * x) * np.exp(-0.2 * x**2))
        
        # Fractal-like structure with modified overlapping peaks and valleys
        f3 = 0.3 * np.sum(np.sin(19.0 * x) * np.sin(9.0 * x) * np.cos(5.0 * x) * np.exp(-0.07 * x**2))
        
        # Saddle points and ridges through different trigonometric terms
        f4 = 0.15 * np.sum(np.sin(4.0 * x) * np.cos(12.0 * x) * x**2)
        
        # Complex cubic and quartic structure with altered coefficients
        f5 = 0.04 * np.sum(x**3 * np.sin(6.0 * x) + x**4 * np.cos(3.0 * x))
        
        # Stronger fractional power term with modified exponent
        f6 = 0.02 * np.sum(np.abs(x)**1.7)
        
        # New chaotic component with different exponential decay and oscillation frequency
        f7 = 0.25 * np.sum(np.sin(21.0 * x) * np.cos(14.0 * x) * np.exp(-0.35 * x**2) * np.sin(26.0 * x))
        
        # New fractal-like component with altered wave interactions
        f8 = 0.18 * np.sum(np.sin(23.0 * x) * np.cos(16.0 * x) * np.sin(12.0 * x) * np.exp(-0.2 * x**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8