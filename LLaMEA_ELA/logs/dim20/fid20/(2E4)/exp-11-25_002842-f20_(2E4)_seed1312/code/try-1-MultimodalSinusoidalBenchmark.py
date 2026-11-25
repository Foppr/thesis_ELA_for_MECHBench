import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range for sinusoidal components
        scaled_x = x * np.pi / 5.0
        
        # Sinusoidal component with multiple global minima
        sinusoidal = np.sum(np.sin(scaled_x) * np.cos(2 * scaled_x))
        
        # Quadratic basin component to create wide optima regions
        quadratic = 0.1 * np.sum(x**2)
        
        # Add a small noise term to make it non-trivial
        noise = 0.01 * np.sum(np.sin(5 * scaled_x))
        
        return sinusoidal + quadratic + noise