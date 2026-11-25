import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced quantum tunneling with adaptive well depths and positions
        tunneling = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive well parameters based on dimension
            well_depths = [1.2, 0.8, 1.5, 0.6]
            well_positions = [0.0, 1.0, -0.9, 1.8]
            for depth, pos in zip(well_depths, well_positions):
                tunneling += depth * np.exp(-0.3 * (xi - pos)**2) * np.sin(4.0 * xi + pos)
        
        # Improved entanglement with dynamic correlation strengths
        entanglement = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic entanglement strength based on dimension and position
                ent_strength = 0.4 * (1.0 + np.cos(0.3 * (i + j)))
                distance = np.abs(x_norm[i] - x_norm[j])
                # Enhanced correlation with phase interference
                entanglement += ent_strength * np.exp(-2.0 * distance**2) * np.sin(5.0 * distance + i*j)
        
        # Dynamic energy barriers with enhanced complexity
        barriers = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Complex barrier structure with multiple peaks
            barrier_params = [(1.8, 0.25), (0.9, 0.5), (1.4, 0.3)]
            for height, width in barrier_params:
                barriers += height * np.exp(-0.4 * ((xi - 0.6) / width)**2) * np.sin(3.0 * xi)
        
        # Discrete optimization with enhanced integer-like structure
        discrete = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced discrete penalties with multiple frequency components
            discrete += np.sin(6.0 * xi) * np.cos(4.0 * xi) + 0.15 * np.sin(12.0 * xi) + 0.05 * np.cos(8.0 * xi)
        
        # Fractal-like roughness with improved multi-scale characteristics
        roughness = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale fractal roughness with varying amplitudes and frequencies
            frequencies = [1.5, 3.0, 4.5, 6.0]
            amplitudes = [0.6, 0.4, 0.25, 0.15]
            for freq, amp in zip(frequencies, amplitudes):
                roughness += amp * np.sin(freq * xi) * np.cos(freq * xi)
        
        # Dynamic scaling with enhanced dimensionality dependence
        dynamic_scale = 1.0 + 0.4 * np.sin(self.dim * 0.3)
        
        # Adaptive weighting scheme to balance components
        weight_tunneling = 0.20 + 0.08 * np.cos(self.dim * 0.15)
        weight_entanglement = 0.35 + 0.12 * np.sin(self.dim * 0.2)
        weight_barriers = 0.25 + 0.10 * np.tanh(self.dim * 0.08)
        weight_discrete = 0.12 + 0.06 * np.cos(self.dim * 0.25)
        weight_roughness = 0.08 + 0.04 * np.sin(self.dim * 0.15)
        
        return dynamic_scale * (weight_tunneling * tunneling + 
                               weight_entanglement * entanglement + 
                               weight_barriers * barriers + 
                               weight_discrete * discrete + 
                               weight_roughness * roughness)