import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hyperchaotic component with enhanced fractal dimensionality
        chaotic = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced chaotic behavior with higher frequencies and nonlinearity
            chaotic += (np.sin(xi * 30.0) * np.cos(xi * 25.0) * np.sin(xi * 19.0) + 
                       np.cos(xi * 35.0) * np.sin(xi * 15.0) * np.cos(xi * 12.0) +
                       np.sin(xi * 28.0) * np.cos(xi * 22.0) * np.sin(xi * 16.0) +
                       np.cos(xi * 40.0) * np.sin(xi * 18.0) * np.cos(xi * 10.0)) / 4.0
        
        # Enhanced entanglement with stronger cross-scale coupling
        entanglement = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stronger cross-scale correlation with fractal scaling and higher order terms
                dist = np.abs(x_norm[i] - x_norm[j])
                scale_factor = 1.0 / (1.0 + np.exp(-dist * 8.0))
                corr_strength = np.exp(-dist**2 * 5.0) * np.sin(dist * np.pi * 3.0)
                entanglement += corr_strength * scale_factor * (x_norm[i]**4 + x_norm[j]**4)
        
        # Adaptive curvature modulation with enhanced dynamic scaling
        curvature = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced curvature with higher order polynomial and stronger modulation
            curvature += (xi**5 - 2.5 * xi**3 + xi) * np.exp(-0.7 * xi**2) * (1.0 + 0.4 * np.sin(xi * 9.0))
        
        # Cross-scale energy coupling with multi-resolution enhanced components
        energy = 0.0
        for i in range(self.dim):
            # Enhanced multi-resolution energy terms with higher-order polynomials
            energy += (x_norm[i]**10 - 5.0 * x_norm[i]**8 + 10.0 * x_norm[i]**6 - 10.0 * x_norm[i]**4 + 5.0 * x_norm[i]**2 - 1.0) * np.exp(-0.4 * x_norm[i]**2)
        
        # Enhanced basin boundaries with stronger hyperchaotic tunneling
        basins = 0.0
        for i in range(self.dim):
            # Stronger hyperchaotic tunneling regions
            tunnel = np.exp(-np.abs(x_norm[i]) * 6.0) * np.sin(x_norm[i] * 25.0)
            basins += tunnel
        
        # Enhanced amplitude modulation with fractal scaling
        amp_modulation = 1.0 + 0.7 * np.sin(self.dim * 0.7) * np.cos(self.dim * 0.4) * np.exp(-self.dim * 0.03)
        
        # Dynamic weighting with enhanced hyperchaotic frequency modulation
        weight_chaotic = 0.3 + 0.15 * np.sin(self.dim * 0.6)
        weight_entanglement = 0.4 + 0.2 * np.cos(self.dim * 0.5)
        weight_curvature = 0.25 + 0.15 * np.sin(self.dim * 0.4)
        weight_energy = 0.25 + 0.1 * np.cos(self.dim * 0.3)
        weight_basins = 0.18 + 0.07 * np.sin(self.dim * 0.7)
        
        return amp_modulation * (weight_chaotic * chaotic + 
                                weight_entanglement * entanglement + 
                                weight_curvature * curvature + 
                                weight_energy * energy + 
                                weight_basins * basins)