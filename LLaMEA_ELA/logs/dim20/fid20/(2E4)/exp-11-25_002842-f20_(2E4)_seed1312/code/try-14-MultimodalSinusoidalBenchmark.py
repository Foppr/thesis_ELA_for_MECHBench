import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range for sinusoidal components
        scaled_x = x * np.pi / 5.0
        
        # Enhanced sinusoidal component with multiple global minima
        sinusoidal = np.sum(np.sin(scaled_x) * np.cos(3 * scaled_x) * np.sin(5 * scaled_x))
        
        # Quadratic basin component to create wide optima regions
        quadratic = 0.1 * np.sum(x**2)
        
        # Additional harmonic components to increase landscape complexity
        harmonic = 0.05 * np.sum(np.sin(7 * scaled_x) + np.cos(4 * scaled_x))
        
        # Add a small noise term to make it non-trivial
        noise = 0.01 * np.sum(np.sin(2 * scaled_x) * np.cos(3 * scaled_x))
        
        # Add a cubic term to increase the difficulty of optimization
        cubic = 0.02 * np.sum(x**3)
        
        return sinusoidal + quadratic + harmonic + noise + cubic