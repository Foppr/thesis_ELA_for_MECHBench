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
        
        # Cubic barrier component to create narrow optima regions
        cubic_barrier = 0.05 * np.sum(np.abs(x)**3)
        
        # Add a complex noise term to make it non-trivial
        noise = 0.02 * np.sum(np.sin(3 * scaled_x) * np.cos(4 * scaled_x))
        
        return sinusoidal + quadratic + cubic_barrier + noise