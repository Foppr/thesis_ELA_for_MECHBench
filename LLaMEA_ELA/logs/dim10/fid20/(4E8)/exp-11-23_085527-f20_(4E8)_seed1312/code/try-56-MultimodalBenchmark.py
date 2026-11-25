import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with quadratic and quartic terms
        r = np.sqrt(np.sum(x_normalized**2))
        radial_term = 0.5 * r**2 + 0.1 * r**4
        
        # Trigonometric oscillations in radial direction
        oscillation_term = 10 * np.sin(5 * np.pi * r)**2 + 5 * np.cos(3 * np.pi * r)**2
        
        # Angular components with cross-terms
        angular_terms = 0.0
        for i in range(self.dim - 1):
            angular_terms += np.sin(x_normalized[i]) * np.cos(x_normalized[i+1])
        
        # Coupled quadratic terms with different weights
        quadratic_coupling = 0.3 * np.sum((x_normalized[:-1] - x_normalized[1:])**2)
        
        # Logarithmic barrier near origin to avoid singularities
        log_barrier = 0.05 * np.log(1 + r**2)
        
        # Combine all terms
        return radial_term + oscillation_term + angular_terms + quadratic_coupling + log_barrier