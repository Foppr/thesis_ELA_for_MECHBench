import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Multiple overlapping quadratic wells with varying depths and positions
        wells = 0.0
        centers = np.linspace(-4.0, 4.0, 9)
        depths = np.sin(np.linspace(0, np.pi, 9)) * 0.8 + 0.5
        for i, (center, depth) in enumerate(zip(centers, depths)):
            wells += depth * np.sum((x - center)**2)
        
        # Enhanced periodic modulation with multiple frequencies
        f2 = 0.4 * np.sum(np.sin(2.5 * x) * np.cos(1.5 * x) * np.sin(0.8 * x))
        
        # Novel deceptive term with exponential decay and high-frequency oscillation
        f3 = 0.2 * np.sum(np.exp(-0.3 * x**2) * np.sin(10.0 * x) * np.cos(5.0 * x))
        
        # Additional harmonic interference to increase landscape complexity
        f4 = 0.15 * np.sum(np.sin(7.0 * x) + np.cos(4.0 * x) - np.sin(3.0 * x))
        
        # Combine all terms with optimized weights
        return f1 + 0.3 * wells + f2 + f3 + f4