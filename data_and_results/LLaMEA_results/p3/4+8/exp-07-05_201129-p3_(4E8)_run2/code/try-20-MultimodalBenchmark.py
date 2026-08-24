import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_normalized**2)
        
        # Sinusoidal terms with exponentially decaying amplitudes
        sinusoidal = np.sum(np.exp(-np.abs(x_normalized)) * np.sin(2 * np.pi * x_normalized))
        
        # Additional high-frequency oscillation component
        high_freq = np.sum(np.sin(10 * np.pi * x_normalized))
        
        # Product term with exponential decay
        product = np.prod(np.exp(-np.abs(x_normalized)))
        
        # Add polynomial correlation terms
        poly_corr = np.sum(x_normalized**4) + 0.5 * np.sum(x_normalized**3)
        
        # Add a complex interaction term
        interaction = np.sum(np.sin(np.pi * x_normalized) * np.cos(2 * np.pi * x_normalized))
        
        # Add a logarithmic barrier near the boundaries
        barrier = np.sum(np.log(1 + np.abs(x_normalized)))
        
        # Combine all components with different weights
        return quadratic + 0.5 * sinusoidal + 0.1 * high_freq + 0.05 * product + 0.02 * poly_corr + 0.03 * interaction + 0.01 * barrier