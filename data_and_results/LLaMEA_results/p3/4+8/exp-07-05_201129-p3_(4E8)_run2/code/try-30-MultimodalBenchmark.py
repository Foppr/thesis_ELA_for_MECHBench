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
        sinusoidal = np.sum(np.exp(-0.5 * np.abs(x_normalized)) * np.sin(2 * np.pi * x_normalized))
        
        # Additional high-frequency oscillation component with varying decay
        high_freq = np.sum(np.sin(15 * np.pi * x_normalized) * np.exp(-0.3 * np.abs(x_normalized)))
        
        # Product term with exponential decay and additional interaction
        product = np.prod(np.exp(-0.7 * np.abs(x_normalized)) * (1 + 0.1 * x_normalized**2))
        
        # Cross-term interaction to increase complexity
        cross_term = np.sum(x_normalized[:-1] * x_normalized[1:] * np.exp(-np.abs(x_normalized[:-1] + x_normalized[1:])))
        
        # Combine all components with different weights
        return 0.8 * quadratic + 0.6 * sinusoidal + 0.2 * high_freq + 0.1 * product + 0.05 * cross_term