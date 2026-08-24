import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic basin term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sinusoidal component with varying frequencies and phase shifts
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(11 * np.pi * x_scaled) * np.sin(9 * np.pi * x_scaled))
        
        # Logarithmic barrier terms to create extremely rugged terrain
        barriers = np.sum(np.log(1 + 5 * np.abs(x_scaled)) * np.sin(5 * np.pi * x_scaled)**2)
        
        # Saddle point structure using mixed polynomial terms with adaptive exponents
        saddle = np.sum(x_scaled**6 - 3 * x_scaled**4 + 2 * x_scaled**2)
        
        # Trigonometric coupling between dimensions to increase interdependence
        coupling = np.sum(np.sin(np.pi * x_scaled[:-1] + x_scaled[1:]) * np.cos(np.pi * x_scaled[:-1] - x_scaled[1:]))
        
        # Combine all components with different weights
        return 0.3 * quadratic + 3.0 * chaotic + 2.0 * barriers + 0.5 * saddle + 1.0 * coupling