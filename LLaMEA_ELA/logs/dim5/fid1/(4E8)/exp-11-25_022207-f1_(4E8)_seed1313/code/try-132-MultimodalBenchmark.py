import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced sinusoidal modulation with higher frequencies and chaotic phase shifts
        sin_modulation = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                               np.sin(9 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) * 
                               np.sin(13 * np.pi * x_norm))
        
        # Enhanced radial basis function component with multiple peaks and varying scales
        rbf = 0.0
        centers = [-0.7, -0.3, 0.0, 0.3, 0.7]
        widths = [0.05, 0.1, 0.15, 0.2, 0.25]
        for i in range(self.dim):
            for c, w in zip(centers, widths):
                rbf += np.exp(-0.5 * (x_norm[i] - c)**2 / w**2)
        
        # Enhanced asymmetric saddle point structure with cubic scaling and directional bias
        saddle = 0.0
        for i in range(self.dim - 1):
            diff = x_norm[i]**2 - x_norm[i+1]**2
            saddle += diff**3 * np.exp(-0.5 * (x_norm[i] + x_norm[i+1])**2)
        
        # Increased polynomial coupling with higher-order terms and cross-dimensional interactions
        poly_interaction = 0.0
        for i in range(self.dim - 2):
            poly_interaction += (x_norm[i]**4 + x_norm[i+1]**4 + x_norm[i+2]**4) * \
                              (x_norm[i]**3 + x_norm[i+1]**3 + x_norm[i+2]**3) * \
                              np.exp(-0.1 * (x_norm[i] - x_norm[i+1])**2)
        
        # Perturbed repulsive force field with fractal-like behavior and time-variant components
        chaotic_repulsion = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                # Add time-variant chaotic component
                chaotic_factor = np.sin(20 * dist) * np.cos(15 * dist)
                chaotic_repulsion += 0.3 * chaotic_factor * np.exp(-dist**3)
        
        # Additional high-frequency oscillatory component with chaotic modulation
        high_freq = 0.4 * np.sum(np.sin(20 * np.pi * x_norm) * 
                               np.cos(22 * np.pi * x_norm) * 
                               np.sin(24 * np.pi * x_norm) * 
                               np.cos(26 * np.pi * x_norm))
        
        # Add a global scaling factor that depends on the dimensionality
        dim_factor = 1.0 + 0.1 * self.dim
        
        # Combine all components with different weights and add controlled noise
        result = (sin_modulation * 0.8 + 
                 rbf * 1.2 + 
                 saddle * 0.6 + 
                 poly_interaction * 0.9 + 
                 chaotic_repulsion * 1.5 + 
                 high_freq * 0.7) * dim_factor
        
        # Add controlled noise term
        noise = 0.15 * np.random.normal(0, 1)
        
        return result + noise