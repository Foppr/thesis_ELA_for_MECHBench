import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced sinusoidal wells with varying frequencies and amplitudes
        f2 = 0.4 * np.sum(np.sin(10.0 * x + 0.5) * np.exp(-0.2 * x**2))
        
        # Chaotic modulation with saddle points and fractal characteristics
        f3 = 0.3 * np.sum(np.cos(15.0 * x - 0.3) * np.exp(-0.15 * np.abs(x)) * np.sin(3.0 * x))
        
        # Exponentially decaying sinusoidal perturbations with cubic terms
        f4 = 0.25 * np.sum(np.sin(20.0 * x + 0.1) * np.exp(-0.25 * np.abs(x)) * np.cos(7.0 * x))
        
        # Additional cosine modulation for increased complexity
        f5 = 0.2 * np.sum(np.cos(25.0 * x - 0.5) * np.exp(-0.1 * x**2))
        
        # Shifted sine perturbations to create deceptive minima with adaptive scaling
        f6 = 0.15 * np.sum(np.sin(30.0 * (x + 0.2)) * np.exp(-0.3 * x**2))
        
        # Higher-order polynomial terms for additional landscape complexity
        f7 = 0.02 * np.sum(x**3)
        f8 = 0.01 * np.sum(x**4)
        
        # Novel adaptive scaling factor with enhanced nonlinearity
        adaptive_scale = 1.0 + 0.6 * np.sin(0.3 * np.sum(x**2)) * np.cos(0.4 * np.sum(x))
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8)