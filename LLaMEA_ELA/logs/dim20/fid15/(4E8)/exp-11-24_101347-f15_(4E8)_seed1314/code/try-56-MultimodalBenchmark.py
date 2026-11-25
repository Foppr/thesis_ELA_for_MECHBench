import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with modified exponential decay
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.exp(-r**3.0) * (1.0 + 0.6 * np.sin(7.0 * r))
        
        # Chaotic angular coupling term with altered interaction
        angular_coupling = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim])
            angular_coupling += np.sin(5.0 * angle + r) * np.cos(4.0 * angle - r)
        
        # Dynamic conditioning based on position with modified scaling
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.8 * np.sin(3.0 * x_scaled[i]))
        
        # Multi-modal sinusoidal component with adjusted frequencies
        modal_term = 0.0
        for i in range(self.dim):
            freq = 3.0 + 0.6 * np.sin(x_scaled[i])
            modal_term += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[(i+1) % self.dim])
        
        # Additional cross-dimensional coupling with chaotic modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            j = (i + 2) % self.dim
            cross_coupling += np.sin(3.0 * x_scaled[i] + 4.0 * x_scaled[j]) * np.cos(2.0 * x_scaled[i] - 3.0 * x_scaled[j])
        
        # Add a new high-frequency chaotic component to increase complexity
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(10.0 * x_scaled[i]) * np.cos(8.0 * x_scaled[(i+1) % self.dim]) * np.exp(-r**2)
        
        # Combine all terms with new weights
        result = radial_term + 0.7 * angular_coupling + 0.9 * modal_term * condition_factor + 0.4 * cross_coupling + 0.5 * chaotic_component
        
        return result