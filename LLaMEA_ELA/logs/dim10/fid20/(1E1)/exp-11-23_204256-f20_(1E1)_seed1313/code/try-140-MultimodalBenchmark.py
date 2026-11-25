import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential radial component with higher frequencies and additional harmonics
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (np.sin(20 * np.pi * r) + 0.5 * np.cos(40 * np.pi * r) + 
                                      0.3 * np.sin(80 * np.pi * r) + 0.15 * np.cos(100 * np.pi * r))
        
        # Enhanced angular component with more chaotic behavior
        if self.dim == 1:
            angular_term = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = (np.sin(25 * angles) * np.cos(10 * angles) + 
                           0.7 * np.sin(35 * angles) * np.cos(18 * angles) + 
                           0.4 * np.sin(50 * angles) * np.cos(25 * angles))
            
        # Enhanced chaotic cross-dimensional interactions with stronger coupling
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += np.exp(-abs(x_norm[i] - x_norm[i+1])) * np.sin(30 * (x_norm[i]**2 + x_norm[i+1]**2)) + \
                          0.6 * np.exp(-abs(x_norm[i] + x_norm[i+1])) * np.cos(20 * (x_norm[i]**3 + x_norm[i+1]**3))
            
        # Modified adaptive conditioning with exponential scaling
        cond_factor = 1.0 + 4.0 * np.exp(-self.dim / 5.0)
        
        # Enhanced high-frequency chaotic noise component
        noise = np.sum(np.sin(50 * np.pi * x_norm) ** 6 + 0.7 * np.cos(60 * np.pi * x_norm) ** 4 + 
                      0.4 * np.sin(70 * np.pi * x_norm) ** 8)
        
        # Enhanced global structure with additional periodic modulation
        periodic_structure = np.sin(4 * np.pi * r) * np.cos(5 * np.pi * r) + 0.6 * np.sin(6 * np.pi * r)
        
        # Additional complex interaction terms for increased multimodality
        interaction_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_terms += np.exp(-((x_norm[i] - x_norm[j])**2 + (x_norm[i] + x_norm[j])**2)) * \
                                   np.sin(35 * np.pi * (x_norm[i]**2 + x_norm[j]**2))
        
        # Novel coupling mechanism with sine-cosine hybrid interactions
        coupling_terms = 0
        for i in range(self.dim):
            coupling_terms += np.sin(15 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i]) * \
                             np.exp(-x_norm[i]**2) + 0.3 * np.cos(25 * np.pi * x_norm[i]) * np.sin(8 * np.pi * x_norm[i])
        
        # Combine all components with appropriate scaling
        return cond_factor * (radial_term + angular_term + cross_terms + noise + periodic_structure + 
                             0.4 * interaction_terms + 0.2 * coupling_terms)