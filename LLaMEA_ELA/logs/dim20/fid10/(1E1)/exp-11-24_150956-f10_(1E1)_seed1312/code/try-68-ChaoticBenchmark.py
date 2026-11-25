import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Multimodal sinusoidal component with varying frequencies
        sin_component = np.sum(np.sin(8 * np.pi * x_scaled) + np.cos(6 * np.pi * x_scaled) + 
                              np.sin(4 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled))
        
        # Radial basis function component with multiple centers
        rbfs = []
        centers = np.linspace(-1, 1, 5)
        for center in centers:
            rbf = np.exp(-5 * np.sum((x_scaled - center)**2))
            rbfs.append(rbf)
        rbf_component = np.sum(rbfs)
        
        # Polynomial interaction terms with mixed degrees
        poly_interaction = np.sum(0.5 * x_scaled**6 + 0.3 * x_scaled**4 + 0.7 * x_scaled**3 + 
                                0.2 * x_scaled**2 + 0.1 * x_scaled)
        
        # Cross-dimensional gradient enhancement
        gradient_enhancement = np.sum(np.sin(3 * x_scaled) * np.cos(5 * x_scaled) * 
                                     np.exp(-0.5 * np.sum(x_scaled**2)))
        
        # Chaotic coupling between dimensions
        chaotic_coupling = np.sum(np.sin(x_scaled[:-1] * x_scaled[1:]) * 
                                 np.cos(x_scaled[:-1] + x_scaled[1:]))
        
        # Combine all components with different weights
        return 0.4 * sin_component + 0.3 * rbf_component + 0.2 * poly_interaction + \
               0.05 * gradient_enhancement + 0.05 * chaotic_coupling + 2.0