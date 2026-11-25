import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced radial component with modified exponential decay and chaotic modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = np.exp(-r * (1.5 + 0.5 * np.sin(15.0 * r))) * (1.0 + 0.6 * np.cos(7.0 * r) + 0.3 * np.sin(12.0 * r))
        
        # Enhanced angular components with stronger chaotic coupling
        angular_terms = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim])
            angular_terms += np.sin((i+1) * angle + 0.7 * np.sin(9.0 * angle)) * np.cos((i+1) * angle + 0.5 * np.cos(6.0 * angle))
        
        # Enhanced multi-modal sinusoidal component with adaptive frequency modulation
        modal_term = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.3 * np.sin(4.0 * x_scaled[i]) + 0.2 * np.cos(5.0 * x_scaled[i])
            modal_term += np.sin(freq_mod * (3.0 * np.pi * x_scaled[i])) * np.cos(freq_mod * (4.0 * np.pi * x_scaled[i]))
        
        # Improved cross-dimensional coupling with higher-order interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.sin(6.0 * (x_scaled[i] + x_scaled[j])) * np.cos(3.0 * (x_scaled[i] - x_scaled[j])) + \
                               0.5 * np.sin(8.0 * (x_scaled[i] * x_scaled[j])) * np.cos(4.0 * (x_scaled[i] / (x_scaled[j] + 1e-8)))
        
        # Additional harmonic component for increased complexity
        harmonic_term = 0.0
        for i in range(self.dim):
            harmonic_term += np.sin(2.0 * np.pi * x_scaled[i]) * np.cos(3.0 * np.pi * x_scaled[i]) * \
                           (1.0 + 0.2 * np.sin(5.0 * x_scaled[i]))
        
        # Combine all terms with optimized weights and add controlled noise
        result = radial_term + 0.5 * angular_terms + 0.7 * modal_term + 0.3 * coupling_term + 0.2 * harmonic_term + \
                 0.1 * np.random.uniform(-0.05, 0.05)
        
        return result