import numpy as np

class ChaoticSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.alpha = 0.5 + 1.0 * np.random.rand()
        self.beta = 0.3 + 0.7 * np.random.rand()
        self.gamma = 0.1 + 0.4 * np.random.rand()
        self.time_phase = np.random.rand() * 2 * np.pi
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Time-varying chaotic scaling
        t = np.cos(self.time_phase) + 1.0
        scaled_x = x * (1.0 + 0.3 * np.sin(0.3 * self.time_phase))
        
        # Multi-scale harmonic saddle components
        saddle_term = 0.0
        for i in range(self.dim):
            # Saddle point with varying depth and width
            depth = 1.0 + 0.5 * np.cos(i * 0.8)
            width = 0.6 + 0.4 * np.sin(i * 0.6)
            saddle_term += depth * (scaled_x[i]**2 - width)**2
            
        # Adaptive gradient modulation
        grad_mod = 1.0 + 0.4 * np.sin(0.5 * self.time_phase + np.sum(x))
        
        # Multi-scale harmonic coupling
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range coupling
                coupling_strength = self.gamma * np.cos(0.2 * (i - j) + self.time_phase)
                coupling_term += coupling_strength * scaled_x[i] * scaled_x[j]
                
        # Basin topology with varying smoothness
        basin_term = 0.0
        for i in range(self.dim):
            smoothness = 0.3 + 0.7 * np.sin(i * 0.4 + self.time_phase)
            basin_term += (scaled_x[i]**3 - 3.0 * scaled_x[i]) * smoothness
            
        # Chaotic time-varying global structure
        global_structure = np.sin(0.15 * np.sum(x**2) + self.time_phase) * np.cos(0.2 * np.sum(x))
        
        # Combine all components with dynamic weights
        result = (saddle_term * grad_mod + 
                 coupling_term * 0.4 + 
                 basin_term * 0.3 + 
                 global_structure * 0.2)
        
        return result