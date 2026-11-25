import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hyperchaotic component with fractal dimensionality
        chaotic = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Fractal-like chaotic behavior with multiple frequencies
            chaotic += (np.sin(xi * 20.0) * np.cos(xi * 17.0) * np.sin(xi * 13.0) + 
                       np.cos(xi * 25.0) * np.sin(xi * 11.0) * np.cos(xi * 8.0) +
                       np.sin(xi * 19.0) * np.cos(xi * 14.0) * np.sin(xi * 9.0)) / 3.0
        
        # Enhanced entanglement with cross-scale coupling
        entanglement = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-scale correlation with fractal scaling
                dist = np.abs(x_norm[i] - x_norm[j])
                scale_factor = 1.0 / (1.0 + np.exp(-dist * 5.0))
                corr_strength = np.exp(-dist**2 * 3.0) * np.sin(dist * np.pi * 2.0)
                entanglement += corr_strength * scale_factor * (x_norm[i]**3 + x_norm[j]**3)
        
        # Adaptive curvature modulation with dynamic scaling
        curvature = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Dynamic curvature based on position and dimension
            curvature += (xi**4 - 2.0 * xi**2) * np.exp(-0.5 * xi**2) * (1.0 + 0.3 * np.sin(xi * 7.0))
        
        # Cross-scale energy coupling with multi-resolution components
        energy = 0.0
        for i in range(self.dim):
            # Multi-resolution energy terms
            energy += (x_norm[i]**8 - 4.0 * x_norm[i]**6 + 6.0 * x_norm[i]**4 - 4.0 * x_norm[i]**2 + 1.0) * np.exp(-0.3 * x_norm[i]**2)
        
        # Enhanced basin boundaries with hyperchaotic tunneling
        basins = 0.0
        for i in range(self.dim):
            # Hyperchaotic tunneling regions
            tunnel = np.exp(-np.abs(x_norm[i]) * 4.0) * np.sin(x_norm[i] * 20.0)
            basins += tunnel
        
        # Adaptive amplitude modulation with fractal scaling
        amp_modulation = 1.0 + 0.5 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.3) * np.exp(-self.dim * 0.02)
        
        # Dynamic weighting with hyperchaotic frequency modulation
        weight_chaotic = 0.25 + 0.1 * np.sin(self.dim * 0.5)
        weight_entanglement = 0.35 + 0.15 * np.cos(self.dim * 0.4)
        weight_curvature = 0.2 + 0.1 * np.sin(self.dim * 0.3)
        weight_energy = 0.2 + 0.05 * np.cos(self.dim * 0.2)
        weight_basins = 0.15 + 0.05 * np.sin(self.dim * 0.6)
        
        return amp_modulation * (weight_chaotic * chaotic + 
                                weight_entanglement * entanglement + 
                                weight_curvature * curvature + 
                                weight_energy * energy + 
                                weight_basins * basins)