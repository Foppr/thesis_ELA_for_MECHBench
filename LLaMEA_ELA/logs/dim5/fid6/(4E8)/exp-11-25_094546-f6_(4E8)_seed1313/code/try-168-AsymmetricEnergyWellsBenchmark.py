import numpy as np

class AsymmetricEnergyWellsBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Multi-scale energy wells with asymmetric depth and width
        energy_well = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple well scales with varying depths and widths
            scale1 = 2.0 * np.exp(-0.5 * (xi - 0.3)**2) * np.sin(8.0 * xi)
            scale2 = 1.5 * np.exp(-0.3 * (xi + 0.4)**2) * np.cos(12.0 * xi)
            scale3 = 1.0 * np.exp(-0.7 * (xi - 0.8)**2) * np.sin(15.0 * xi)
            energy_well += scale1 + scale2 + scale3
            
        # Dynamic curvature modulation with dimension-dependent scaling
        curvature = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Varying curvature strength based on dimension index
            curv_strength = 0.5 + 0.5 * np.sin(0.3 * i)
            curvature += curv_strength * (xi**4 - 2.0 * xi**2 + 0.5 * xi)
            
        # Cross-dimensional interference with asymmetric coupling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                # Asymmetric coupling strength based on dimension indices
                asym_strength = 0.3 + 0.2 * np.sin(0.5 * (i - j))
                cross_coupling += asym_strength * np.exp(-dist**2 * 5.0) * np.sin(10.0 * dist)
                
        # Multi-modal harmonic interference with frequency modulation
        harmonic = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple frequencies with varying amplitudes and phases
            freqs = [2.0, 5.0, 8.0, 12.0]
            amps = [1.0, 0.7, 0.5, 0.3]
            phases = [0.0, np.pi/4, np.pi/2, 3*np.pi/4]
            
            for freq, amp, phase in zip(freqs, amps, phases):
                harmonic += amp * np.sin(freq * xi + phase) * np.exp(-0.5 * (xi - 0.5)**2)
                
        # Asymmetric basin boundaries with varying steepness
        basin = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Different steepness on left vs right sides of the domain
            if xi < 0:
                steepness = 1.5 + 0.5 * np.sin(2.0 * i)
                basin += steepness * xi**3
            else:
                steepness = 1.2 + 0.3 * np.cos(1.5 * i)
                basin += steepness * xi**4
                
        # Dynamic scaling factor based on problem dimensionality
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * 0.5) + 0.2 * np.cos(self.dim * 0.3)
        
        # Combine all components with optimized weights
        total = (0.4 * energy_well + 
                0.3 * curvature + 
                0.2 * cross_coupling + 
                0.1 * harmonic + 
                0.05 * basin) * scale_factor
        
        return total