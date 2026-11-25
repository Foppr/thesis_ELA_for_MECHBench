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
            # Fractal-like chaotic behavior with modified frequencies
            chaotic += (np.sin(xi * 22.0) * np.cos(xi * 19.0) * np.sin(xi * 15.0) + 
                       np.cos(xi * 27.0) * np.sin(xi * 13.0) * np.cos(xi * 10.0) +
                       np.sin(xi * 21.0) * np.cos(xi * 16.0) * np.sin(xi * 11.0)) / 3.0
        
        # Enhanced entanglement with cross-scale coupling
        entanglement = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-scale correlation with modified scaling
                dist = np.abs(x_norm[i] - x_norm[j])
                scale_factor = 1.0 / (1.0 + np.exp(-dist * 6.0))
                corr_strength = np.exp(-dist**2 * 4.0) * np.sin(dist * np.pi * 2.5)
                entanglement += corr_strength * scale_factor * (x_norm[i]**3 + x_norm[j]**3)
        
        # Adaptive curvature modulation with dynamic scaling
        curvature = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Dynamic curvature based on position and dimension
            curvature += (xi**4 - 2.0 * xi**2) * np.exp(-0.5 * xi**2) * (1.0 + 0.35 * np.sin(xi * 8.0))
        
        # Cross-scale energy coupling with multi-resolution components
        energy = 0.0
        for i in range(self.dim):
            # Multi-resolution energy terms with modified exponents
            energy += (x_norm[i]**9 - 4.5 * x_norm[i]**7 + 6.5 * x_norm[i]**5 - 4.5 * x_norm[i]**3 + 1.5 * x_norm[i]) * np.exp(-0.35 * x_norm[i]**2)
        
        # Enhanced basin boundaries with hyperchaotic tunneling
        basins = 0.0
        for i in range(self.dim):
            # Hyperchaotic tunneling regions with modified parameters
            tunnel = np.exp(-np.abs(x_norm[i]) * 4.5) * np.sin(x_norm[i] * 22.0)
            basins += tunnel
        
        # Adaptive amplitude modulation with fractal scaling
        amp_modulation = 1.0 + 0.55 * np.sin(self.dim * 0.65) * np.cos(self.dim * 0.35) * np.exp(-self.dim * 0.025)
        
        # Dynamic weighting with hyperchaotic frequency modulation
        weight_chaotic = 0.27 + 0.12 * np.sin(self.dim * 0.55)
        weight_entanglement = 0.37 + 0.16 * np.cos(self.dim * 0.45)
        weight_curvature = 0.22 + 0.11 * np.sin(self.dim * 0.35)
        weight_energy = 0.22 + 0.06 * np.cos(self.dim * 0.25)
        weight_basins = 0.17 + 0.06 * np.sin(self.dim * 0.65)
        
        return amp_modulation * (weight_chaotic * chaotic + 
                                weight_entanglement * entanglement + 
                                weight_curvature * curvature + 
                                weight_energy * energy + 
                                weight_basins * basins)