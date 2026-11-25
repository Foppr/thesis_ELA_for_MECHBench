import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.exp(-r) * (1.0 + 0.5 * np.sin(3.0 * r))
        
        # Angular components with multiple frequencies
        angular_terms = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim])
            angular_terms += np.sin((i+1) * angle) * np.cos((i+1) * angle)
        
        # Multi-modal sinusoidal component
        modal_term = 0.0
        for i in range(self.dim):
            modal_term += np.sin(2.0 * np.pi * x_scaled[i]) * np.cos(3.0 * np.pi * x_scaled[i])
        
        # Combine all terms with different weights
        result = radial_term + 0.3 * angular_terms + 0.7 * modal_term
        
        return result