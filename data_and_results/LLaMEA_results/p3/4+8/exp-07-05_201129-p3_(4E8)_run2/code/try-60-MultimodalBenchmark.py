import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Wave interference component with varying frequencies and amplitudes
        wave_term = 0.0
        for i in range(min(6, self.dim)):
            freq = (i + 1) * 3.0
            amp = 1.0 / (1.0 + 0.3 * i)
            wave_term += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Radial conditioning with exponential decay and periodic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial_conditioning = r**2 * np.exp(-0.5 * r**2) * (1.0 + 0.2 * np.sin(5.0 * r))
        
        # Asymmetric basin structure with polynomial potential
        basin_term = 0.0
        for i in range(self.dim):
            # Create asymmetric regions based on sign of variable
            asym_factor = 1.0 + 0.5 * np.sign(x_norm[i])
            basin_term += asym_factor * (x_norm[i]**4 + 0.5 * x_norm[i]**2)
        
        # Cross-term with harmonic coupling and gradient-dependent modulation
        cross_term = 0.0
        if self.dim > 1:
            for i in range(self.dim):
                for j in range(i+1, self.dim):
                    cross_term += np.sin(x_norm[i] * x_norm[j]) * (1.0 + 0.1 * (i + j))
        
        # Periodic potential with multiple local minima and varying depths
        periodic_term = 0.0
        for i in range(min(4, self.dim)):
            periodic_term += np.cos(2.0 * np.pi * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Combine all terms with dynamic weighting based on dimensionality
        dim_factor = 1.0 + 0.05 * (self.dim - 1)
        result = (0.3 * wave_term + 
                 0.25 * radial_conditioning + 
                 0.2 * basin_term + 
                 0.15 * cross_term + 
                 0.1 * periodic_term) * dim_factor
        
        return result