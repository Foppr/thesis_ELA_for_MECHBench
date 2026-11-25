import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with higher degree to increase complexity
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sinusoidal = np.sum(np.sin(5.0 * x)) + 0.5 * np.sum(np.sin(10.0 * x)) + 0.2 * np.sum(np.sin(15.0 * x))
        
        # Add radial symmetry component to increase multimodality
        radius = np.sqrt(np.sum(x**2))
        radial_component = 0.3 * np.sin(3.0 * radius) * np.cos(2.0 * radius)
        
        # Add interaction terms between dimensions to increase complexity
        interaction = 0.1 * np.sum(x[:-1] * x[1:]) + 0.05 * np.sum(x**3)
        
        # Combined function with global minimum at origin
        return polynomial + sinusoidal + radial_component + interaction + 0.05 * radius**4