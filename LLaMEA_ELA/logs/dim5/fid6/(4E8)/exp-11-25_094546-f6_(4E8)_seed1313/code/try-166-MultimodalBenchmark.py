import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced hyperchaotic entanglement with fractal phase interference
        entanglement = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            for j in range(i+1, self.dim):
                # Fractal-based entanglement with dynamic coupling strength and enhanced chaos
                coupling_strength = 0.9 * (1.0 + np.sin(0.5 * (i + j) + np.pi/4))
                phase_diff = np.abs(xi - x_norm[j])
                entanglement += coupling_strength * np.exp(-3.0 * phase_diff**2) * np.sin(10.0 * phase_diff + i*j + np.sin(3.0 * phase_diff))
        
        # Enhanced adaptive tunneling with multi-scale potential wells and hyperchaotic dynamics
        tunneling = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Hyperchaotic well structures with varying depths, positions, and chaotic modulation
            wells = [(1.8, -0.9), (1.3, 0.6), (1.5, 1.2), (1.0, -1.0), (1.2, 0.4)]
            for depth, pos in wells:
                tunneling += depth * np.exp(-0.3 * (xi - pos)**2) * np.cos(5.0 * xi + pos + np.sin(4.0 * xi))
        
        # Enhanced dynamic barrier landscape with hyperchaotic tunneling probabilities
        barriers = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-peak barrier structure with fractal heights, widths, and enhanced chaos
            peaks = [(2.2, 0.15), (1.1, 0.45), (1.7, 0.25), (0.8, 0.6)]
            for height, width in peaks:
                barriers += height * np.exp(-0.4 * ((xi - 0.7) / width)**2) * np.cos(4.0 * xi + np.sin(3.0 * xi))
        
        # Enhanced discrete quantum-like energy levels with hyperchaotic structure
        discrete = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Hyperchaotic discrete penalties with multiple harmonic components, fractal modulation, and enhanced complexity
            discrete += 1.3 * np.sin(7.0 * xi + np.sin(3.0 * xi)) + 0.6 * np.cos(9.0 * xi) + 0.25 * np.sin(14.0 * xi + np.sin(4.0 * xi))
        
        # Enhanced fractal-like roughness with hyperchaotic self-similarity and multi-scale coupling
        roughness = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale fractal structure with varying frequencies, amplitudes, chaotic modulation, and enhanced complexity
            frequencies = [3.0, 5.0, 7.0, 9.0, 11.0, 13.0]
            amplitudes = [0.7, 0.45, 0.3, 0.2, 0.12, 0.08]
            for freq, amp in zip(frequencies, amplitudes):
                roughness += amp * np.sin(freq * xi + np.sin(2.5 * freq * xi)) * np.cos(freq * xi + np.cos(2.5 * freq * xi))
        
        # Enhanced hyperchaotic scaling factor with dimensionality dependence and fractal modulation
        dynamic_scale = 1.0 + 0.7 * np.cos(self.dim * 0.4 + np.sin(self.dim * 0.2))
        
        # Component weighting based on enhanced hyperchaotic complexity and fractal dimensionality
        weights = [0.23, 0.22, 0.23, 0.22, 0.10]
        
        return dynamic_scale * (weights[0] * entanglement + 
                               weights[1] * tunneling + 
                               weights[2] * barriers + 
                               weights[3] * discrete + 
                               weights[4] * roughness)