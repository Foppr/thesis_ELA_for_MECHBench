import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hyperchaotic component with fractal dimensionality and quantum-like probability
        chaotic = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Fractal-like chaotic behavior with multiple frequencies and quantum probability
            chaotic += (np.sin(xi * 21.0) * np.cos(xi * 18.0) * np.sin(xi * 14.0) + 
                       np.cos(xi * 26.0) * np.sin(xi * 12.0) * np.cos(xi * 9.0) +
                       np.sin(xi * 20.0) * np.cos(xi * 15.0) * np.sin(xi * 10.0)) / 3.0
        
        # Enhanced entanglement with cross-scale coupling and quantum tunneling
        entanglement = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-scale correlation with fractal scaling and quantum tunneling
                dist = np.abs(x_norm[i] - x_norm[j])
                scale_factor = 1.0 / (1.0 + np.exp(-dist * 5.5))
                corr_strength = np.exp(-dist**2 * 3.5) * np.sin(dist * np.pi * 2.2)
                # Add quantum tunneling effect
                tunneling = np.exp(-np.abs(x_norm[i] - x_norm[j]) * 2.2) * np.cos((x_norm[i] + x_norm[j]) * 10.5)
                entanglement += corr_strength * scale_factor * (x_norm[i]**3 + x_norm[j]**3) + tunneling
        
        # Adaptive curvature modulation with dynamic scaling and quantum phase
        curvature = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Dynamic curvature based on position and dimension with quantum phase
            curvature += (xi**4 - 2.0 * xi**2) * np.exp(-0.5 * xi**2) * (1.0 + 0.3 * np.sin(xi * 7.5)) * np.cos(xi * 3.5)
        
        # Cross-scale energy coupling with multi-resolution components and quantum interference
        energy = 0.0
        for i in range(self.dim):
            # Multi-resolution energy terms with quantum interference
            energy += (x_norm[i]**8 - 4.0 * x_norm[i]**6 + 6.0 * x_norm[i]**4 - 4.0 * x_norm[i]**2 + 1.0) * np.exp(-0.3 * x_norm[i]**2) * np.sin(x_norm[i] * 5.5)
        
        # Enhanced basin boundaries with hyperchaotic tunneling and quantum probability
        basins = 0.0
        for i in range(self.dim):
            # Hyperchaotic tunneling regions with quantum probability
            tunnel = np.exp(-np.abs(x_norm[i]) * 4.2) * np.sin(x_norm[i] * 21.0) * np.cos(x_norm[i] * 8.5)
            basins += tunnel
        
        # Adaptive amplitude modulation with fractal scaling and quantum phase
        amp_modulation = 1.0 + 0.5 * np.sin(self.dim * 0.65) * np.cos(self.dim * 0.35) * np.exp(-self.dim * 0.025) * np.sin(self.dim * 0.45)
        
        # Dynamic weighting with hyperchaotic frequency modulation and quantum interference
        weight_chaotic = 0.26 + 0.1 * np.sin(self.dim * 0.55) * np.cos(self.dim * 0.25)
        weight_entanglement = 0.36 + 0.15 * np.cos(self.dim * 0.45) * np.sin(self.dim * 0.35)
        weight_curvature = 0.21 + 0.1 * np.sin(self.dim * 0.35) * np.cos(self.dim * 0.15)
        weight_energy = 0.21 + 0.05 * np.cos(self.dim * 0.25) * np.sin(self.dim * 0.65)
        weight_basins = 0.16 + 0.05 * np.sin(self.dim * 0.65) * np.cos(self.dim * 0.45)
        
        return amp_modulation * (weight_chaotic * chaotic + 
                                weight_entanglement * entanglement + 
                                weight_curvature * curvature + 
                                weight_energy * energy + 
                                weight_basins * basins)