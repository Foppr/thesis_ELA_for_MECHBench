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
            chaotic += (np.sin(xi * 20.0) * np.cos(xi * 17.0) * np.sin(xi * 13.0) + 
                       np.cos(xi * 25.0) * np.sin(xi * 11.0) * np.cos(xi * 8.0) +
                       np.sin(xi * 19.0) * np.cos(xi * 14.0) * np.sin(xi * 9.0)) / 3.0
        
        # Enhanced entanglement with cross-scale coupling and quantum tunneling
        entanglement = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-scale correlation with fractal scaling and quantum tunneling
                dist = np.abs(x_norm[i] - x_norm[j])
                scale_factor = 1.0 / (1.0 + np.exp(-dist * 5.0))
                corr_strength = np.exp(-dist**2 * 3.0) * np.sin(dist * np.pi * 2.0)
                # Add quantum tunneling effect
                tunneling = np.exp(-np.abs(x_norm[i] - x_norm[j]) * 2.0) * np.cos((x_norm[i] + x_norm[j]) * 10.0)
                entanglement += corr_strength * scale_factor * (x_norm[i]**3 + x_norm[j]**3) + tunneling
        
        # Adaptive curvature modulation with dynamic scaling and quantum phase
        curvature = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Dynamic curvature based on position and dimension with quantum phase
            curvature += (xi**4 - 2.0 * xi**2) * np.exp(-0.5 * xi**2) * (1.0 + 0.3 * np.sin(xi * 7.0)) * np.cos(xi * 3.0)
        
        # Cross-scale energy coupling with multi-resolution components and quantum interference
        energy = 0.0
        for i in range(self.dim):
            # Multi-resolution energy terms with quantum interference
            energy += (x_norm[i]**8 - 4.0 * x_norm[i]**6 + 6.0 * x_norm[i]**4 - 4.0 * x_norm[i]**2 + 1.0) * np.exp(-0.3 * x_norm[i]**2) * np.sin(x_norm[i] * 5.0)
        
        # Enhanced basin boundaries with hyperchaotic tunneling and quantum probability
        basins = 0.0
        for i in range(self.dim):
            # Hyperchaotic tunneling regions with quantum probability
            tunnel = np.exp(-np.abs(x_norm[i]) * 4.0) * np.sin(x_norm[i] * 20.0) * np.cos(x_norm[i] * 8.0)
            basins += tunnel
        
        # Adaptive amplitude modulation with fractal scaling and quantum phase
        amp_modulation = 1.0 + 0.5 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.3) * np.exp(-self.dim * 0.02) * np.sin(self.dim * 0.4)
        
        # Dynamic weighting with hyperchaotic frequency modulation and quantum interference
        weight_chaotic = 0.25 + 0.1 * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.2)
        weight_entanglement = 0.35 + 0.15 * np.cos(self.dim * 0.4) * np.sin(self.dim * 0.3)
        weight_curvature = 0.2 + 0.1 * np.sin(self.dim * 0.3) * np.cos(self.dim * 0.1)
        weight_energy = 0.2 + 0.05 * np.cos(self.dim * 0.2) * np.sin(self.dim * 0.6)
        weight_basins = 0.15 + 0.05 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.4)
        
        return amp_modulation * (weight_chaotic * chaotic + 
                                weight_entanglement * entanglement + 
                                weight_curvature * curvature + 
                                weight_energy * energy + 
                                weight_basins * basins)