import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with chaotic exponential decay
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.exp(-r**2) * (1.0 + 0.3 * np.sin(5.0 * r))
        
        # Chaotic angular coupling term
        angular_coupling = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim])
            angular_coupling += np.sin(4.0 * angle + r) * np.cos(3.0 * angle - r)
        
        # Dynamic conditioning based on position
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.5 * np.sin(2.0 * x_scaled[i]))
        
        # Multi-modal sinusoidal component with dynamic frequency
        modal_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(x_scaled[i])
            modal_term += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[(i+1) % self.dim])
        
        # Combine all terms with varying weights
        result = radial_term + 0.4 * angular_coupling + 0.6 * modal_term * condition_factor
        
        return result