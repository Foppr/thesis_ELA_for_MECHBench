import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic dynamics
        self.r = 3.9  # Logistic map parameter
        self.theta = np.linspace(0, 2*np.pi, dim+1)[:-1]  # Angular coordinates
        self.phi = np.linspace(0, np.pi, dim+1)[:-1]      # Polar coordinates
        
    def f(self, x):
        # Scale input to [-1, 1]
        x_scaled = x / 5.0
        
        # Chaotic component using logistic map
        chaotic = 0.0
        for i in range(min(10, self.dim)):
            if i == 0:
                chaotic += (self.r * x_scaled[i] * (1 - x_scaled[i])) ** 2
            else:
                chaotic += (self.r * x_scaled[i-1] * (1 - x_scaled[i-1])) ** 2
        
        # Spherical harmonics component
        sph_harm = 0.0
        for i in range(self.dim):
            sph_harm += (np.sin(self.theta[i]) * np.cos(self.phi[i]) * x_scaled[i])**2
        
        # Quaternion-based rotation component
        quat_rot = 0.0
        for i in range(0, self.dim-1, 2):
            if i+1 < self.dim:
                quat_rot += (x_scaled[i]**2 + x_scaled[i+1]**2) * np.sin(x_scaled[i] * x_scaled[i+1])
        
        # Multi-scale sinusoidal interference
        multi_scale = 0.0
        for k in range(1, 6):
            multi_scale += np.sin(k * np.sum(x_scaled**2)) * np.cos(k * np.sum(x_scaled))
        
        # Asymmetric cubic polynomial with cross-terms
        cubic_poly = np.sum(x_scaled**3 + 0.5 * x_scaled**2 - 0.3 * x_scaled)
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = 0.0
        for i in range(self.dim-1):
            cross_coupling += np.exp(-0.5 * (x_scaled[i] - x_scaled[i+1])**2) * \
                             np.sin(3.0 * (x_scaled[i] + x_scaled[i+1]))
        
        # Combine all components with different weights
        return 0.4 * chaotic + 0.3 * sph_harm + 0.15 * quat_rot + \
               0.1 * multi_scale + 0.05 * cubic_poly + 0.05 * cross_coupling + 2.1