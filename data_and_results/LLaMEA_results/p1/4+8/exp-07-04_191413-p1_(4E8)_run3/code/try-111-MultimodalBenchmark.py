import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Shift input to center the global minimum at (1,1,...,1)
        x_shifted = x - 1.0
        
        # Scale input to [-1, 1] range
        x_scaled = x_shifted / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Exponential decay terms with sinusoidal modulation (modified frequency)
        exp_decay = np.sum(np.exp(-x_scaled**2) * np.sin(5 * np.pi * x_scaled)**2)
        
        # Additional cosine peaks with different frequency and weight
        cos_peaks = np.sum(np.cos(9 * np.pi * x_scaled) * np.exp(-0.3 * x_scaled**2))
        
        # Add a cross-dimensional interaction term with chaotic multiplier
        cross_term = 0.1 * np.sum(np.sin(3 * np.pi * x_scaled[:-1]) * x_scaled[1:] * np.exp(-0.5 * x_scaled[:-1]**2))
        
        # Introduce nested chaotic sine wave component with enhanced nonlinearity
        chaotic_term = 0.3 * np.sum(np.sin(7 * np.pi * x_scaled) * np.sin(11 * np.pi * x_scaled) * np.sin(13 * np.pi * x_scaled))
        
        # Add a new secondary chaotic modulation to increase multimodality - slightly modified frequencies and weights
        secondary_chaos = 0.18 * np.sum(np.sin(17 * np.pi * x_scaled**2) * np.cos(19 * np.pi * x_scaled) * np.exp(-0.2 * x_scaled**2))
        
        # Add a new higher-order polynomial interaction for increased complexity
        poly_interaction = 0.05 * np.sum(x_scaled**4 * np.sin(2 * np.pi * x_scaled)**2)
        
        # Introduce a new chaotic component with frequency modulation and adaptive weights
        adaptive_chaos = 0.25 * np.sum(np.sin(23 * np.pi * x_scaled**3) * np.cos(25 * np.pi * x_scaled) * np.exp(-0.1 * x_scaled**2))
        
        # Add a new interaction term with a different chaotic pattern and higher dimensionality coupling
        high_dim_interaction = 0.15 * np.sum(np.sin(4 * np.pi * x_scaled[:-2]) * x_scaled[1:-1] * x_scaled[2:] * np.exp(-0.3 * x_scaled[:-2]**2))
        
        # Combine with different weights
        return quadratic + 0.6 * exp_decay + 0.2 * cos_peaks + cross_term + chaotic_term + secondary_chaos + poly_interaction + adaptive_chaos + high_dim_interaction