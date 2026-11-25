import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Asymmetric chaotic saddle component with modified bifurcation zones
        saddle = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Modified bifurcation zones with sharper transitions
            if xi < -0.25:
                saddle += 2.5 * np.sin(18.0 * xi) * np.exp(-0.4 * xi**2)
            elif xi > 0.25:
                saddle += 1.8 * np.cos(14.0 * xi) * np.exp(-0.2 * xi**2)
            else:
                # Enhanced central chaotic region with fractal-like behavior
                saddle += 1.0 * np.sin(25.0 * xi + 0.7 * np.sin(35.0 * xi)) * np.exp(-0.6 * xi**2)
        
        # Dynamic basin boundary component with modified curvature
        basins = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Modified sigmoidal transitions with steeper gradients
            boundary = 1.0 / (1.0 + np.exp(-12.0 * (xi - 0.15)))
            curvature = 2.5 + 2.0 * np.sin(10.0 * xi)
            basins += curvature * boundary * (xi**4 - 1.8 * xi**2 + 0.6)
        
        # Multi-scale harmonic interference with altered frequency modulation
        harmonics = 0.0
        freq_mod = 1.2 + 0.4 * np.sin(0.6 * self.dim)
        for i in range(self.dim):
            xi = x_norm[i]
            # Modified harmonic components with different scale factors
            scale_factor = 2.5**(i % 5)
            harmonics += (0.6 + 0.4 * np.sin(scale_factor * xi)) * \
                        np.cos(freq_mod * scale_factor * xi) * \
                        np.exp(-0.15 * xi**2)
        
        # Cross-dimensional coupling with modified asymmetric interaction coefficients
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                xi, xj = x_norm[i], x_norm[j]
                # Modified coupling strength based on dimension index
                asym_strength = 0.9 + 0.1 * np.sin(0.4 * (i - j))
                dist = np.sqrt((xi - xj)**2 + 0.15)
                cross += asym_strength * np.sin(18.0 * dist) * np.exp(-dist**2)
        
        # Time-varying landscape modulation with enhanced perturbations
        time_mod = 1.0 + 0.5 * np.sin(0.25 * self.dim + np.sum(x_norm))
        landscape_mod = 0.6 * np.cos(3.5 * np.sum(x_norm)) + 0.4 * np.sin(5.5 * np.sum(x_norm))
        
        # Combine all components with updated dynamic weights
        weight_saddle = 0.35 + 0.25 * np.sin(self.dim * 0.35)
        weight_basins = 0.35 + 0.15 * np.cos(self.dim * 0.25)
        weight_harmonics = 0.18 + 0.17 * np.tanh(self.dim * 0.12)
        weight_cross = 0.28
        
        return time_mod * (weight_saddle * saddle + 
                          weight_basins * basins + 
                          weight_harmonics * harmonics + 
                          weight_cross * cross) + landscape_mod