import numpy as np

class RadialAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with adaptive curvature
        r = np.sqrt(np.sum(x_norm**2))
        radial = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive curvature based on distance from origin
            curvature = 1.0 + 0.5 * np.sin(2.0 * r + i * 0.3)
            radial += curvature * (xi**2 - 0.3 * xi**4 + 0.05 * xi**6)
        
        # Multi-scale harmonic component with dynamic frequencies
        harmonics = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Frequency modulation based on dimension and position
            freq = 2.0 + 1.5 * np.sin(0.5 * i + r)
            harm_freq = 3.0 + 2.0 * np.cos(0.3 * i + r)
            harmonics += np.sin(freq * xi) * np.cos(harm_freq * xi) * np.exp(-0.5 * xi**2)
        
        # Nested basin component with varying depth
        basins = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Nested structure with different scaling factors
            scale = 1.0 + 0.3 * np.sin(0.7 * i)
            basin_depth = 2.0 + 1.5 * np.cos(0.4 * i + r)
            basins += basin_depth * np.exp(-scale * (xi**2 - 0.5)**2)
        
        # Cross-dimensional coupling with radial dependence
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi, xj = x_norm[i], x_norm[j]
                # Radial coupling strength that decreases with distance
                dist = np.sqrt(xi**2 + xj**2)
                coupling_strength = 0.8 * np.exp(-0.3 * dist)
                cross += coupling_strength * np.sin(5.0 * (xi + xj)) * np.cos(3.0 * (xi - xj))
        
        # Dynamic time-varying modulation
        time_mod = 1.0 + 0.2 * np.sin(0.1 * self.dim + r)
        
        # Combine components with adaptive weights
        weight_radial = 0.4 + 0.1 * np.sin(0.5 * self.dim)
        weight_harmonics = 0.3 + 0.15 * np.cos(0.3 * self.dim)
        weight_basins = 0.2 + 0.1 * np.tanh(0.4 * self.dim)
        weight_cross = 0.1
        
        return time_mod * (weight_radial * radial + 
                          weight_harmonics * harmonics + 
                          weight_basins * basins + 
                          weight_cross * cross) + 0.1 * np.sin(10.0 * r)