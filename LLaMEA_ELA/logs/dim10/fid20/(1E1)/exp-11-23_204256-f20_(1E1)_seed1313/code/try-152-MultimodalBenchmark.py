import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential radial component with higher frequencies and additional harmonics
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (np.sin(15 * np.pi * r) + 0.4 * np.cos(30 * np.pi * r) + 
                                      0.2 * np.sin(60 * np.pi * r) + 0.1 * np.cos(75 * np.pi * r))
        
        # Enhanced angular component with more chaotic behavior
        if self.dim == 1:
            angular_term = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = (np.sin(20 * angles) * np.cos(9 * angles) + 
                           0.6 * np.sin(30 * angles) * np.cos(15 * angles) + 
                           0.3 * np.sin(40 * angles) * np.cos(20 * angles))
            
        # Enhanced chaotic cross-dimensional interactions with stronger coupling
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += np.exp(-abs(x_norm[i] - x_norm[i+1])) * np.sin(25 * (x_norm[i]**2 + x_norm[i+1]**2)) + \
                          0.5 * np.exp(-abs(x_norm[i] + x_norm[i+1])) * np.cos(15 * (x_norm[i]**3 + x_norm[i+1]**3))
            
        # Modified adaptive conditioning with exponential scaling
        cond_factor = 1.0 + 3.0 * np.exp(-self.dim / 4.0)
        
        # Enhanced high-frequency chaotic noise component
        noise = np.sum(np.sin(40 * np.pi * x_norm) ** 5 + 0.6 * np.cos(50 * np.pi * x_norm) ** 3 + 
                      0.3 * np.sin(60 * np.pi * x_norm) ** 7)
        
        # Enhanced global structure with additional periodic modulation
        periodic_structure = np.sin(3 * np.pi * r) * np.cos(4 * np.pi * r) + 0.5 * np.sin(5 * np.pi * r)
        
        # Additional complex interaction terms for increased multimodality
        interaction_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_terms += np.exp(-((x_norm[i] - x_norm[j])**2 + (x_norm[i] + x_norm[j])**2)) * \
                                   np.sin(30 * np.pi * (x_norm[i]**2 + x_norm[j]**2))
        
        # Add a new component to improve fitness score by increasing complexity and altering gradient behavior
        new_complexity = 0.1 * np.sum(np.sin(100 * x_norm) * np.cos(80 * x_norm) * np.exp(-x_norm**2))
        
        # Combine all components with appropriate scaling
        return cond_factor * (radial_term + angular_term + cross_terms + noise + periodic_structure + 0.3 * interaction_terms + new_complexity)