import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum-like probabilistic tunneling component
        tunneling = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple quantum wells with varying depths and positions
            well_depths = [1.0, 0.7, 1.3, 0.5]
            well_positions = [0.0, 1.2, -0.8, 2.1]
            for depth, pos in zip(well_depths, well_positions):
                tunneling += depth * np.exp(-0.5 * (xi - pos)**2) * np.sin(3.0 * xi + pos)
        
        # Entangled dimension coupling with quantum-like correlations
        entanglement = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced entanglement strength based on dimension indices
                ent_strength = 0.3 * (1.0 + np.sin(0.5 * (i + j)))
                distance = np.abs(x_norm[i] - x_norm[j])
                # Quantum correlation function with phase interference
                entanglement += ent_strength * np.exp(-distance**2) * np.cos(4.0 * distance + i*j)
        
        # Dynamic energy barriers with time-varying characteristics
        barriers = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple barrier heights and widths
            barrier_params = [(1.5, 0.3), (0.8, 0.6), (1.2, 0.4)]
            for height, width in barrier_params:
                barriers += height * np.exp(-0.5 * ((xi - 0.5) / width)**2) * np.cos(2.0 * xi)
        
        # Discrete optimization challenges with integer-like structure
        discrete = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Integer-like penalties with continuous approximation
            discrete += np.sin(5.0 * xi) * np.cos(3.0 * xi) + 0.1 * np.sin(10.0 * xi)
        
        # Continuous optimization with fractal-like roughness
        roughness = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Fractal-like roughness with multiple frequency components
            frequencies = [2.0, 4.0, 6.0, 8.0]
            amplitudes = [0.5, 0.3, 0.2, 0.1]
            for freq, amp in zip(frequencies, amplitudes):
                roughness += amp * np.sin(freq * xi) * np.cos(freq * xi)
        
        # Dynamic scaling based on problem dimensionality
        dynamic_scale = 1.0 + 0.3 * np.sin(self.dim * 0.25)
        
        # Weighted combination of all components
        weight_tunneling = 0.25 + 0.05 * np.cos(self.dim * 0.1)
        weight_entanglement = 0.30 + 0.10 * np.sin(self.dim * 0.15)
        weight_barriers = 0.20 + 0.08 * np.tanh(self.dim * 0.05)
        weight_discrete = 0.15 + 0.07 * np.cos(self.dim * 0.2)
        weight_roughness = 0.10 + 0.05 * np.sin(self.dim * 0.1)
        
        return dynamic_scale * (weight_tunneling * tunneling + 
                               weight_entanglement * entanglement + 
                               weight_barriers * barriers + 
                               weight_discrete * discrete + 
                               weight_roughness * roughness)