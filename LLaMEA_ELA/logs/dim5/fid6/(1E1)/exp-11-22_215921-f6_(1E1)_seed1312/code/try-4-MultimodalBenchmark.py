import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic = np.sum(x_norm ** 2)
        
        # Multiple sinusoidal oscillations with different frequencies creating more local minima
        sinusoidal = 3 * np.sum(np.sin(3 * np.pi * x_norm) ** 2 + 
                               2 * np.sin(7 * np.pi * x_norm) ** 2)
        
        # Multiple Gaussian peaks with varying amplitudes and positions
        gaussian = 0.8 * np.sum(np.exp(-15 * (x_norm - 0.2) ** 2) + 
                               0.6 * np.exp(-12 * (x_norm + 0.3) ** 2) +
                               0.4 * np.exp(-8 * (x_norm - 0.5) ** 2))
        
        # Cross-term interaction to increase landscape complexity
        cross_term = 0.5 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine all terms with different weights
        return quadratic + sinusoidal + gaussian + cross_term