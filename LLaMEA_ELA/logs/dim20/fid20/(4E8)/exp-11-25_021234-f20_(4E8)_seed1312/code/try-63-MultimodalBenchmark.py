import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal perturbations with higher frequencies and variable amplitudes
        f2 = 0.5 * np.sum(np.sin(25.0 * x) * np.cos(18.0 * x) * np.exp(-0.2 * x**2))
        
        # Fractal-like structure with multiple overlapping peaks and valleys at higher frequencies
        f3 = 0.4 * np.sum(np.sin(30.0 * x) * np.sin(15.0 * x) * np.cos(8.0 * x) * np.exp(-0.1 * x**2))
        
        # Saddle points and ridges through mixed high-frequency trigonometric terms
        f4 = 0.2 * np.sum(np.sin(7.0 * x) * np.cos(20.0 * x) * x**2)
        
        # Complex cubic and quartic structure with enhanced non-smooth behavior
        f5 = 0.06 * np.sum(x**3 * np.sin(10.0 * x) + x**4 * np.cos(6.0 * x))
        
        # Stronger fractional power term to create more pronounced non-smooth regions
        f6 = 0.03 * np.sum(np.abs(x)**2.1)
        
        # New chaotic component with exponential decay and ultra-high-frequency oscillations
        f7 = 0.3 * np.sum(np.sin(35.0 * x) * np.cos(28.0 * x) * np.exp(-0.4 * x**2) * np.sin(30.0 * x))
        
        # Additional fractal-like component with multiple overlapping sine waves at even higher frequencies
        f8 = 0.25 * np.sum(np.sin(40.0 * x) * np.cos(32.0 * x) * np.sin(24.0 * x) * np.exp(-0.3 * x**2))
        
        # Introduce adaptive scaling to make the function more sensitive in different regions
        adaptive_scale = 1.0 + 0.5 * np.sin(0.5 * x)
        f9 = 0.1 * np.sum(adaptive_scale * (x**2) * np.cos(12.0 * x))
        
        # Add a new non-smooth component using absolute value with fractional exponents
        f10 = 0.05 * np.sum(np.abs(x)**1.9 * np.sin(22.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10