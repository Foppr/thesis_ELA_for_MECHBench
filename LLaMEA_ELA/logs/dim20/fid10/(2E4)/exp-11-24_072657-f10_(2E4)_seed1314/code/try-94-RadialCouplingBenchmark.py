import numpy as np

class RadialCouplingBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with logarithmic conditioning
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = r * np.log(r + 1e-8) * np.sin(3 * r)
        
        # Multi-modal sinusoidal patterns in radial direction
        modal_terms = []
        for i in range(1, min(6, self.dim + 1)):
            freq = i * 2.0
            amp = 1.0 / (i * 0.5 + 1.0)
            modal_terms.append(amp * np.sin(freq * r) * np.cos(freq * r))
        
        # Cross-dimensional coupling with adaptive weights
        coupling_term = 0.0
        for i in range(self.dim - 1):
            weight = 1.0 / (1.0 + 0.1 * i)
            coupling_term += weight * (x_norm[i]**2 + x_norm[i+1]**2) * \
                           np.sin(2 * (x_norm[i] - x_norm[i+1])**2)
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * 0.5)
        
        # Angular component with periodic variations
        if self.dim > 1:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = np.sum(np.sin(angles * (self.dim + 1)) * 
                                np.cos(angles * (self.dim - 1)))
        else:
            angular_term = 0.0
        
        # Combine all components
        result = condition_factor * (radial_term + 0.5 * np.sum(modal_terms) + 
                                   0.3 * coupling_term + 0.2 * angular_term)
        
        # Add small random noise for increased complexity
        noise = 0.001 * np.random.random()
        
        return result + noise