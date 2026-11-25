import numpy as np

class ChaoticQuadraticLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.chaotic_factor = 0.8 + 0.4 * np.random.rand()
        self.oscillation_freq = 1.0 + 2.0 * np.random.rand()
        self.basin_splitting = 0.3 + 0.4 * np.random.rand()
        self.gradient_scaling = 1.0 + 0.5 * np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic oscillatory component
        chaotic_term = 0.0
        for i in range(self.dim):
            # Multi-scale chaotic oscillations with adaptive frequency
            freq = self.oscillation_freq * (1.0 + 0.3 * np.sin(i * 0.5))
            chaotic_term += np.sin(freq * x[i] + self.chaotic_factor * np.sin(2.0 * freq * x[i]))
            
        # Quadratic basin component with adaptive splitting
        quadratic_term = 0.0
        for i in range(self.dim):
            # Split basins with varying curvature
            curvature = 1.0 + 0.5 * np.sin(i * 0.3)
            basin_shift = self.basin_splitting * np.cos(i * 0.7)
            quadratic_term += curvature * (x[i] - basin_shift)**2
            
        # Multi-scale gradient modulation
        gradient_mod = 1.0 + 0.2 * np.sin(0.5 * np.sum(x))
        
        # Adaptive coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling_strength = 0.1 + 0.2 * np.sin((i+j) * 0.3)
                coupling_term += coupling_strength * x[i] * x[j]
                
        # Time-varying global structure
        time_phase = np.sin(0.1 * np.sum(x**2)) + np.cos(0.05 * np.sum(x))
        global_term = np.sin(time_phase * 3.0) * np.cos(time_phase * 2.0)
        
        # Combine all components
        result = (self.gradient_scaling * (quadratic_term + chaotic_term) + 
                 coupling_term * 0.3 + 
                 global_term * 0.1)
        
        return result