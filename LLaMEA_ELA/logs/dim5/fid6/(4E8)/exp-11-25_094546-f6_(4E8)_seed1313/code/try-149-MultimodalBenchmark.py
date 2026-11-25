import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hyperchaotic entanglement with fractal phase interference
        entanglement = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            for j in range(i+1, self.dim):
                # Fractal-based entanglement with dynamic coupling strength
                coupling_strength = 0.7 * (1.0 + np.sin(0.3 * (i + j) + np.pi/4))
                phase_diff = np.abs(xi - x_norm[j])
                entanglement += coupling_strength * np.exp(-3.0 * phase_diff**2) * np.sin(8.0 * phase_diff + i*j + np.sin(2.0 * phase_diff))
        
        # Adaptive tunneling with multi-scale potential wells and hyperchaotic dynamics
        tunneling = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Hyperchaotic well structures with varying depths and positions
            wells = [(1.5, -0.9), (1.1, 0.6), (1.3, 1.4), (0.8, -1.2), (1.0, 0.2)]
            for depth, pos in wells:
                tunneling += depth * np.exp(-0.3 * (xi - pos)**2) * np.cos(4.0 * xi + pos + np.sin(3.0 * xi))
        
        # Dynamic barrier landscape with hyperchaotic tunneling probabilities
        barriers = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-peak barrier structure with fractal heights and widths
            peaks = [(1.8, 0.25), (0.9, 0.55), (1.4, 0.35), (0.6, 0.7)]
            for height, width in peaks:
                barriers += height * np.exp(-0.4 * ((xi - 0.8) / width)**2) * np.cos(3.0 * xi + np.sin(2.0 * xi))
        
        # Discrete quantum-like energy levels with hyperchaotic structure
        discrete = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Hyperchaotic discrete penalties with multiple harmonic components and fractal modulation
            discrete += 1.0 * np.sin(6.0 * xi + np.sin(2.0 * xi)) + 0.4 * np.cos(8.0 * xi) + 0.15 * np.sin(12.0 * xi + np.sin(3.0 * xi))
        
        # Fractal-like roughness with hyperchaotic self-similarity and multi-scale coupling
        roughness = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale fractal structure with varying frequencies, amplitudes, and chaotic modulation
            frequencies = [2.5, 4.5, 6.5, 8.5, 10.5]
            amplitudes = [0.6, 0.35, 0.2, 0.12, 0.08]
            for freq, amp in zip(frequencies, amplitudes):
                roughness += amp * np.sin(freq * xi + np.sin(2.0 * freq * xi)) * np.cos(freq * xi + np.cos(2.0 * freq * xi))
        
        # Hyperchaotic scaling factor with dimensionality dependence and fractal modulation
        dynamic_scale = 1.0 + 0.5 * np.cos(self.dim * 0.3 + np.sin(self.dim * 0.1))
        
        # Component weighting based on hyperchaotic complexity and fractal dimensionality
        weights = [0.20, 0.25, 0.25, 0.20, 0.10]
        
        return dynamic_scale * (weights[0] * entanglement + 
                               weights[1] * tunneling + 
                               weights[2] * barriers + 
                               weights[3] * discrete + 
                               weights[4] * roughness)