import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial terms with varying degrees to create multiple local minima
        poly = np.sum(x_scaled**6 + 0.5 * x_scaled**4 + 0.1 * x_scaled**2)
        
        # Trigonometric component with varying frequencies and amplitudes
        trig = np.sum(np.sin(5 * x_scaled) * np.cos(3 * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Exponential barrier terms with asymmetric scaling
        exp_barrier = np.sum(np.exp(-2 * np.abs(x_scaled)) * (1 + 0.5 * np.sin(4 * x_scaled)))
        
        # Cross-dimensional coupling with non-uniform weights
        coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * np.sin(3 * np.pi * x_scaled[:-1] * x_scaled[1:]))
        
        # Asymmetric dimension scaling to increase difficulty in certain directions
        asymmetry = np.sum((1 + 0.3 * np.abs(x_scaled)) * x_scaled**3)
        
        # Combine all components with different weights
        return 0.3 * poly + 1.5 * trig + 0.8 * exp_barrier + 0.2 * coupling + 0.1 * asymmetry