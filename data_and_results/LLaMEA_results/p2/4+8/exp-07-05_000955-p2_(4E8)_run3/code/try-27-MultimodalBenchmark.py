import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term for global convergence
        f1 = np.sum(x**2)
        
        # Chaotic sine-wave interactions with varying amplitudes and frequencies
        f2 = 0.3 * np.sum(np.sin(5.0 * x + np.sin(3.0 * x)) * np.cos(7.0 * x + np.sin(2.0 * x)))
        
        # Radial gradient with exponential decay to create basin-like structures
        f3 = 0.2 * np.sum(np.exp(-0.5 * np.sum(x**2)) * np.sin(4.0 * np.sum(x**2)))
        
        # Cross-term interactions with polynomial modulation
        f4 = 0.1 * np.sum((x**3) * np.sin(6.0 * x) * np.cos(3.0 * x))
        
        # Multi-scale sinusoidal modulation to increase landscape complexity
        f5 = 0.15 * np.sum(np.sin(10.0 * x) * np.sin(15.0 * x) * np.cos(5.0 * x))
        
        # Adaptive scaling based on the distance from the origin
        f6 = 0.05 * np.sum(np.exp(-0.2 * np.sum(x**2)) * x**4)
        
        return f1 + f2 + f3 + f4 + f5 + f6