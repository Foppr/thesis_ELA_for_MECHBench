import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential radial component with modified frequencies and harmonics
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (np.sin(18 * np.pi * r) + 0.5 * np.cos(35 * np.pi * r) + 
                                      0.25 * np.sin(65 * np.pi * r) + 0.15 * np.cos(80 * np.pi * r))
        
        # Enhanced angular component with modified chaotic behavior
        if self.dim == 1:
            angular_term = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = (np.sin(25 * angles) * np.cos(10 * angles) + 
                           0.7 * np.sin(35 * angles) * np.cos(18 * angles) + 
                           0.35 * np.sin(45 * angles) * np.cos(22 * angles))
            
        # Modified chaotic cross-dimensional interactions with different coupling strengths
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += np.exp(-abs(x_norm[i] - x_norm[i+1])) * np.sin(30 * (x_norm[i]**2 + x_norm[i+1]**2)) + \
                          0.6 * np.exp(-abs(x_norm[i] + x_norm[i+1])) * np.cos(20 * (x_norm[i]**3 + x_norm[i+1]**3))
            
        # Modified adaptive conditioning with altered exponential scaling
        cond_factor = 1.0 + 3.5 * np.exp(-self.dim / 4.5)
        
        # Enhanced high-frequency chaotic noise component with modified exponents
        noise = np.sum(np.sin(45 * np.pi * x_norm) ** 5 + 0.7 * np.cos(55 * np.pi * x_norm) ** 3 + 
                      0.35 * np.sin(65 * np.pi * x_norm) ** 7)
        
        # Modified global structure with different periodic modulation
        periodic_structure = np.sin(3.5 * np.pi * r) * np.cos(4.5 * np.pi * r) + 0.6 * np.sin(5.5 * np.pi * r)
        
        # Additional complex interaction terms with altered coupling
        interaction_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_terms += np.exp(-((x_norm[i] - x_norm[j])**2 + (x_norm[i] + x_norm[j])**2)) * \
                                   np.sin(35 * np.pi * (x_norm[i]**2 + x_norm[j]**2))
        
        # Combine all components with adjusted scaling
        return cond_factor * (radial_term + angular_term + cross_terms + noise + periodic_structure + 0.35 * interaction_terms)