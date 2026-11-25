import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2 / 2.0)
        
        # Sinusoidal terms with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = (i + 1) * np.pi
            sinusoidal += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Add a polynomial term to create additional curvature
        poly_term = np.sum(x_norm**4)
        
        # Combine components with different weights
        return 2.0 * radial + 0.5 * sinusoidal - 0.1 * poly_term + 1.5