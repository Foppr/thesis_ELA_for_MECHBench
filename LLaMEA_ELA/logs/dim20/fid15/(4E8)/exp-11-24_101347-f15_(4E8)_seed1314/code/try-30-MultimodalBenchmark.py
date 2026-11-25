import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with exponential decay and chaotic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.exp(-r * (1.0 + 0.3 * np.sin(10.0 * r))) * (1.0 + 0.4 * np.cos(5.0 * r))
        
        # Angular components with chaotic coupling
        angular_terms = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim])
            angular_terms += np.sin((i+1) * angle + 0.5 * np.sin(7.0 * angle)) * np.cos((i+1) * angle + 0.3 * np.cos(4.0 * angle))
        
        # Multi-modal sinusoidal component with chaotic frequency modulation
        modal_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.2 * np.sin(3.0 * x_scaled[i])
            modal_term += np.sin(freq_mod * (2.0 * np.pi * x_scaled[i])) * np.cos(freq_mod * (3.0 * np.pi * x_scaled[i]))
        
        # Cross-dimensional coupling with chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.sin(4.0 * (x_scaled[i] + x_scaled[j])) * np.cos(2.0 * (x_scaled[i] - x_scaled[j]))
        
        # Combine all terms with different weights and add chaotic noise
        result = radial_term + 0.4 * angular_terms + 0.6 * modal_term + 0.2 * coupling_term + 0.1 * np.random.uniform(-0.1, 0.1)
        
        return result