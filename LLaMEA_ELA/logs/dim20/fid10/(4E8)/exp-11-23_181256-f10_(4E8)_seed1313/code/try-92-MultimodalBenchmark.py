import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Separable quartic terms creating shallow and deep minima
        f1 = np.sum(x_scaled**4)
        
        # Non-separable cosine interactions with varying frequencies
        f2 = np.sum(np.cos(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Cross-dimensional coupling with sine modulation
        f3 = np.sum(np.sin(4 * np.pi * x_scaled[:-1]) * np.cos(5 * np.pi * x_scaled[1:]))
        
        # Gradient-based attraction-repulsion field
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = (x_scaled[i] - x_scaled[j])**2
                f4 += np.exp(-dist) * np.sin(2 * np.pi * dist)
        
        # Novel radial component with polynomial decay and logarithmic barrier
        r = np.sqrt(np.sum(x_scaled**2))
        f5 = r**3 * np.exp(-r**2) + 1.0 / (1.0 + r**2)
        
        # Additional harmonic oscillation with dynamic frequency
        f6 = np.sum(np.sin(7 * np.pi * x_scaled) * np.cos(8 * np.pi * x_scaled))
        
        # Combined function with diverse curvature and conditioning
        return 0.8 * f1 + 0.6 * f2 + 0.5 * f3 + 0.4 * f4 + 0.3 * f5 + 0.2 * f6 + np.sum(x_scaled**6)