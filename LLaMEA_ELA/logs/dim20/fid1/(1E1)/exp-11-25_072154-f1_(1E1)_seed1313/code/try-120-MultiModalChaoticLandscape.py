import numpy as np

class MultiModalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with periodic basis functions
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled)) + \
                 0.5 * np.sum(np.sin(7 * np.pi * x_scaled**2) * np.cos(5 * np.pi * x_scaled**2)) + \
                 0.3 * np.sum(np.sin(11 * np.pi * x_scaled**0.5) * np.cos(9 * np.pi * x_scaled**0.5))
        
        # Cross-dimensional interference patterns
        interference = 0.0
        for i in range(self.dim - 1):
            for j in range(i + 1, self.dim):
                interference += np.sin(np.pi * (x_scaled[i] + x_scaled[j])) * \
                               np.cos(2 * np.pi * (x_scaled[i] - x_scaled[j]))
        
        # Asymmetric gradient fields with directional bias
        asym_gradient = 0.0
        for i in range(self.dim):
            asym_gradient += (x_scaled[i]**3) * np.sin(4 * np.pi * x_scaled[i]) + \
                           0.5 * (x_scaled[i]**2) * np.cos(3 * np.pi * x_scaled[i])
        
        # Multi-scale periodic modulations
        periodic_mod = 0.0
        for i in range(self.dim):
            periodic_mod += np.sin(15 * np.pi * x_scaled[i]) * np.cos(12 * np.pi * x_scaled[i]) + \
                           0.4 * np.sin(20 * np.pi * x_scaled[i]**1.5) * np.cos(18 * np.pi * x_scaled[i]**1.5)
        
        # Deceptive local optima with varying curvature
        deceptive = 0.0
        for i in range(self.dim):
            deceptive += (x_scaled[i]**4) * np.sin(6 * np.pi * x_scaled[i]) + \
                        0.3 * (x_scaled[i]**6) * np.cos(5 * np.pi * x_scaled[i])
        
        # Fractional dimensionality component
        frac_dim = 0.0
        for i in range(self.dim):
            frac_dim += np.sin(8 * np.pi * x_scaled[i]**1.3) * np.cos(7 * np.pi * x_scaled[i]**1.2)
        
        # Cross-dimensional coupling with varying strength
        cross_coupling = 0.0
        for i in range(self.dim - 2):
            cross_coupling += (x_scaled[i] + x_scaled[i+1]) * np.sin(3 * np.pi * (x_scaled[i] - x_scaled[i+1])) + \
                             0.5 * (x_scaled[i+1] + x_scaled[i+2]) * np.cos(4 * np.pi * (x_scaled[i+1] - x_scaled[i+2]))
        
        # Combined function with optimized weights
        return 0.3 * radial + 0.25 * interference + 0.2 * asym_gradient + 0.15 * periodic_mod + \
               0.1 * deceptive + 0.08 * frac_dim + 0.07 * cross_coupling