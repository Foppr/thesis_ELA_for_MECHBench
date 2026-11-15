import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay with sinusoidal modulation
        f1 = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Trigonometric wave interactions with varying frequencies
        f2 = np.sum(np.sin(1.5 * x) * np.cos(2.5 * x) * np.sin(4.0 * x))
        
        # Quaternion-inspired cross-term coupling
        f3 = np.sum(np.sin(x) * np.cos(x**2) * np.sin(x**3))
        
        # Multi-scale oscillation with logarithmic scaling
        f4 = np.sum(np.sin(np.log(np.abs(x) + 1.0)) * np.cos(np.log(np.abs(x) + 1.0)))
        
        # Gaussian mixture with varying centers and variances
        gaussian_mixture = 0
        centers = np.linspace(-3.0, 3.0, 5)
        for center in centers:
            gaussian_mixture += np.exp(-0.5 * ((x - center) / 1.5)**2)
        f5 = gaussian_mixture
        
        # Polynomial coupling with negative exponents
        f6 = np.sum((x**(-1.5) + 0.5 * x**(-2.5)) * np.abs(x)**0.8)
        
        # Saddle point with hyperbolic tangent and polynomial components
        f7 = np.sum(np.tanh(x) * (x**2 - 2.0) * np.cos(1.5 * x))
        
        # Fractal-like recursive structure
        f8 = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.sin(5.0 * x))
        
        # Combined result
        return 0.2 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)