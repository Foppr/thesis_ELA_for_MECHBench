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
        sinusoidal = np.sum(np.exp(-0.3 * np.abs(x_normalized)) * np.sin(3 * np.pi * x_normalized))
        
        # Additional high-frequency oscillation component with varying decay
        high_freq = np.sum(np.sin(20 * np.pi * x_normalized) * np.exp(-0.2 * np.abs(x_normalized)))
        
        # Product term with exponential decay and additional interaction
        product = np.prod(np.exp(-0.5 * np.abs(x_normalized)) * (1 + 0.15 * x_normalized**2))
        
        # Cross-term interaction to increase complexity
        cross_term = np.sum(x_normalized[:-1] * x_normalized[1:] * np.exp(-0.5 * np.abs(x_normalized[:-1] + x_normalized[1:])))
        
        # Additional radial component to create more complex landscape
        radial = np.exp(-0.1 * np.sum(x_normalized**2)) * np.sin(5 * np.pi * np.sum(x_normalized**2))
        
        # Combine all components with different weights
        return 0.7 * quadratic + 0.5 * sinusoidal + 0.3 * high_freq + 0.15 * product + 0.08 * cross_term + 0.02 * radial