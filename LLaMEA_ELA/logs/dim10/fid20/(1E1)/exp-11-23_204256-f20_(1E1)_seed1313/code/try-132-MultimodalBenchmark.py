import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential radial component with multiple frequencies and amplitude modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (np.sin(15 * np.pi * r) + 0.4 * np.cos(30 * np.pi * r) + 0.2 * np.sin(60 * np.pi * r) + 0.1 * np.cos(75 * np.pi * r))
        
        # Enhanced angular component with chaotic behavior and multiple interaction terms
        if self.dim == 1:
            angular_term = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular_term = (np.sin(20 * angles) * np.cos(8 * angles) + 
                           0.6 * np.sin(25 * angles) * np.cos(12 * angles) + 
                           0.3 * np.sin(35 * angles) * np.cos(18 * angles))
            
        # Enhanced chaotic cross-dimensional interactions with non-linear coupling and multiple interaction types
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += (np.exp(-abs(x_norm[i] - x_norm[i+1])) * 
                           np.sin(25 * (x_norm[i]**2 + x_norm[i+1]**2)) + 
                           0.5 * np.exp(-abs(x_norm[i] + x_norm[i+1])) * 
                           np.cos(15 * (x_norm[i]**3 + x_norm[i+1]**3)))
            
        # Enhanced adaptive conditioning with exponential scaling and dimension-dependent factor
        cond_factor = 1.0 + 3.0 * np.exp(-self.dim / 7.0) + 0.5 * np.sin(self.dim * np.pi / 4)
        
        # High-frequency chaotic noise component with multiple harmonics
        noise = np.sum(np.sin(40 * np.pi * x_norm)**6 + 0.6 * np.cos(50 * np.pi * x_norm)**4 + 
                      0.3 * np.sin(60 * np.pi * x_norm)**8)
        
        # Additional global structure with periodic modulation and harmonic components
        periodic_structure = (np.sin(3 * np.pi * r) * np.cos(4 * np.pi * r) + 
                             0.5 * np.sin(5 * np.pi * r) * np.cos(6 * np.pi * r))
        
        # Add a complex interaction term between all dimensions
        if self.dim > 2:
            complex_interaction = 0
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    complex_interaction += np.sin(10 * (x_norm[i] - x_norm[j])) * np.cos(5 * (x_norm[i] + x_norm[j]))
            complex_interaction /= (self.dim * (self.dim - 1) / 2)
        else:
            complex_interaction = 0
            
        # Combine all components with appropriate scaling
        return cond_factor * (radial_term + angular_term + cross_terms + noise + periodic_structure + complex_interaction)