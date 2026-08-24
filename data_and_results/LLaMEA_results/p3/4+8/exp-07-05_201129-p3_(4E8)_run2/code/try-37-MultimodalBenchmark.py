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
        sinusoidal = np.sum(np.exp(-0.5 * np.abs(x_normalized)) * np.sin(4 * np.pi * x_normalized))
        
        # Additional high-frequency oscillation component with modified amplitude
        high_freq = np.sum(0.9 * np.sin(20 * np.pi * x_normalized))
        
        # Polynomial interaction term
        poly_interaction = np.sum(x_normalized**4)
        
        # Product term with exponential decay and modified base
        product = np.prod(np.exp(-0.2 * np.abs(x_normalized)))
        
        # Shifted global minimum component with perturbation
        shift = np.sum((x_normalized + 0.15)**2)
        
        # Cross-term interaction
        cross_term = np.sum(x_normalized[:-1] * x_normalized[1:])
        
        # Combine all components with different weights
        return quadratic + 0.7 * sinusoidal + 0.2 * high_freq + 0.1 * poly_interaction + 0.05 * product + 0.15 * shift + 0.05 * cross_term