import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Asymmetric chaotic saddle component with bifurcation zones
        saddle = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Create asymmetric bifurcation zones
            if xi < -0.3:
                saddle += 2.0 * np.sin(15.0 * xi) * np.exp(-0.5 * xi**2)
            elif xi > 0.3:
                saddle += 1.5 * np.cos(12.0 * xi) * np.exp(-0.3 * xi**2)
            else:
                # Central chaotic region
                saddle += 0.8 * np.sin(20.0 * xi + 0.5 * np.sin(30.0 * xi)) * np.exp(-0.7 * xi**2)
        
        # Dynamic basin boundary component with varying curvature
        basins = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Create dynamic boundaries using sigmoidal transitions
            boundary = 1.0 / (1.0 + np.exp(-10.0 * (xi - 0.2)))
            curvature = 2.0 + 1.5 * np.sin(8.0 * xi)
            basins += curvature * boundary * (xi**4 - 2.0 * xi**2 + 0.5)
        
        # Multi-scale harmonic interference with frequency modulation
        harmonics = 0.0
        freq_mod = 1.0 + 0.3 * np.sin(0.5 * self.dim)
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple harmonic components at different scales
            scale_factor = 2.0**(i % 4)
            harmonics += (0.5 + 0.5 * np.sin(scale_factor * xi)) * \
                        np.cos(freq_mod * scale_factor * xi) * \
                        np.exp(-0.2 * xi**2)
        
        # Cross-dimensional coupling with asymmetric interaction coefficients
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                xi, xj = x_norm[i], x_norm[j]
                # Asymmetric coupling strength based on dimension index
                asym_strength = 0.8 + 0.2 * np.sin(0.3 * (i - j))
                dist = np.sqrt((xi - xj)**2 + 0.1)
                cross += asym_strength * np.sin(15.0 * dist) * np.exp(-dist**2)
        
        # Time-varying landscape modulation with periodic perturbations
        time_mod = 1.0 + 0.4 * np.sin(0.2 * self.dim + np.sum(x_norm))
        landscape_mod = 0.5 * np.cos(3.0 * np.sum(x_norm)) + 0.3 * np.sin(5.0 * np.sum(x_norm))
        
        # Combine all components with dynamic weights
        weight_saddle = 0.4 + 0.2 * np.sin(self.dim * 0.3)
        weight_basins = 0.3 + 0.1 * np.cos(self.dim * 0.2)
        weight_harmonics = 0.2 + 0.15 * np.tanh(self.dim * 0.1)
        weight_cross = 0.25
        
        return time_mod * (weight_saddle * saddle + 
                          weight_basins * basins + 
                          weight_harmonics * harmonics + 
                          weight_cross * cross) + landscape_mod