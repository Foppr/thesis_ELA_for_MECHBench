import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_normalized**2)
        
        # Sinusoidal terms with exponentially decaying amplitudes and modified frequencies
        sinusoidal = np.sum(np.exp(-0.5 * np.abs(x_normalized)) * np.sin(3 * np.pi * x_normalized))
        
        # Additional high-frequency oscillation component with modified amplitude
        high_freq = np.sum(0.8 * np.sin(15 * np.pi * x_normalized))
        
        # Product term with exponential decay and modified base
        product = np.prod(np.exp(-0.3 * np.abs(x_normalized)))
        
        # Shifted global minimum component
        shift = np.sum((x_normalized + 0.1)**2)
        
        # Combine all components with different weights
        return quadratic + 0.6 * sinusoidal + 0.15 * high_freq + 0.08 * product + 0.2 * shift