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
        
        # Add a novel exponential decay term to increase landscape complexity
        exponential = 0.5 * np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(3 * scaled_x))
        
        # Add a fourth harmonic component for additional multimodality
        harmonic = 0.05 * np.sum(np.sin(4 * scaled_x) * np.cos(scaled_x))
        
        # Add a small noise term to make it non-trivial
        noise = 0.01 * np.sum(np.sin(5 * scaled_x))
        
        return sinusoidal + quadratic + exponential + harmonic + noise