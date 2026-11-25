import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain
        x_scaled = x / 5.0
        
        # Polynomial terms with varying degrees
        poly_term = np.sum(x_scaled**6) + 0.5 * np.sum(x_scaled**4) + 0.1 * np.sum(x_scaled**2)
        
        # Trigonometric components with different frequencies and amplitudes
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled)) + 0.5 * np.sum(np.cos(4 * np.pi * x_scaled))
        
        # Interaction terms between dimensions
        interaction_term = 0.3 * np.sum(x_scaled[:-1] * x_scaled[1:])
        
        # Add a global shifting component to increase complexity
        shift = 1.0
        shifted_x = x_scaled + shift
        
        # Additional sinusoidal modulation based on dimension interactions
        modulate = np.prod(np.cos(0.5 * np.pi * shifted_x))
        
        # Combine all terms with different weights
        result = poly_term + trig_term + interaction_term + 0.2 * modulate
        
        return float(result)