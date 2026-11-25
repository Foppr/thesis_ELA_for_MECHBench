import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum-inspired entanglement with complex phase interference
        entanglement = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            for j in range(i+1, self.dim):
                # Phase-based entanglement with dimensionally adaptive coupling
                coupling_strength = 0.5 * (1.0 + np.sin(0.5 * (i + j)))
                phase_diff = np.abs(xi - x_norm[j])
                entanglement += coupling_strength * np.exp(-2.0 * phase_diff**2) * np.sin(6.0 * phase_diff + i*j)
        
        # Adaptive tunneling with multi-scale potential wells
        tunneling = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple well depths and positions with dynamic scaling
            wells = [(1.3, -0.8), (0.9, 0.5), (1.1, 1.2), (0.7, -1.0)]
            for depth, pos in wells:
                tunneling += depth * np.exp(-0.2 * (xi - pos)**2) * np.cos(3.0 * xi + pos)
        
        # Dynamic barrier landscape with quantum-like tunneling probabilities
        barriers = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-peak barrier structure with varying heights and widths
            peaks = [(1.5, 0.3), (0.8, 0.6), (1.2, 0.4)]
            for height, width in peaks:
                barriers += height * np.exp(-0.5 * ((xi - 0.7) / width)**2) * np.cos(2.0 * xi)
        
        # Discrete quantum-like energy levels with enhanced structure
        discrete = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced discrete penalties with multiple harmonic components
            discrete += 0.8 * np.sin(5.0 * xi) + 0.3 * np.cos(7.0 * xi) + 0.1 * np.sin(10.0 * xi)
        
        # Fractal-like roughness with quantum-inspired self-similarity
        roughness = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale fractal structure with varying frequencies and amplitudes
            frequencies = [2.0, 4.0, 6.0, 8.0]
            amplitudes = [0.5, 0.3, 0.15, 0.1]
            for freq, amp in zip(frequencies, amplitudes):
                roughness += amp * np.sin(freq * xi) * np.cos(freq * xi)
        
        # Dynamic scaling factor with dimensionality dependence
        dynamic_scale = 1.0 + 0.3 * np.cos(self.dim * 0.2)
        
        # Component weighting based on dimension and complexity
        weights = [0.25, 0.30, 0.20, 0.15, 0.10]
        
        return dynamic_scale * (weights[0] * entanglement + 
                               weights[1] * tunneling + 
                               weights[2] * barriers + 
                               weights[3] * discrete + 
                               weights[4] * roughness)