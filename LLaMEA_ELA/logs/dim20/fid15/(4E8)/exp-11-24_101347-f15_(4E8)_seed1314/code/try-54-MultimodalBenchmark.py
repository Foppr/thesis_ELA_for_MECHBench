import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with chaotic exponential decay and higher-order harmonics
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.exp(-r**2) * (1.0 + 0.4 * np.sin(5.0 * r) + 0.2 * np.cos(3.0 * r))
        
        # Enhanced chaotic angular coupling with multiple interaction terms
        angular_coupling = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim])
            angular_coupling += (np.sin(4.0 * angle + r) * np.cos(3.0 * angle - r) + 
                               0.5 * np.cos(6.0 * angle + 2.0 * r) * np.sin(2.0 * angle - 3.0 * r))
        
        # Dynamic conditioning with polynomial and trigonometric variations
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.6 * np.sin(2.0 * x_scaled[i]) + 0.3 * np.cos(4.0 * x_scaled[i]))
        
        # Multi-modal sinusoidal component with dynamic frequency and higher-order interactions
        modal_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.7 * np.sin(x_scaled[i]) + 0.3 * np.cos(2.0 * x_scaled[i])
            modal_term += (np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[(i+1) % self.dim]) +
                          0.5 * np.sin(3.0 * freq * x_scaled[i]) * np.cos(2.0 * freq * x_scaled[(i+1) % self.dim]))
        
        # Cross-dimensional coupling with higher-order terms
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += (np.sin(x_scaled[i] + x_scaled[j]) * np.cos(x_scaled[i] - x_scaled[j]) +
                                 0.3 * np.cos(2.0 * x_scaled[i] + x_scaled[j]) * np.sin(2.0 * x_scaled[i] - x_scaled[j]))
        
        # Combine all terms with varying weights
        result = radial_term + 0.5 * angular_coupling + 0.7 * modal_term * condition_factor + 0.3 * cross_coupling
        
        return result