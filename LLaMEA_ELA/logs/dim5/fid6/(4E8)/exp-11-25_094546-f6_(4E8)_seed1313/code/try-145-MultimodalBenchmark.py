import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced quantum entanglement with hyperchaotic phase coupling
        entanglement = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            for j in range(i+1, self.dim):
                # Hyperchaotic coupling with exponential decay and sinusoidal modulation
                coupling_strength = 0.7 * (1.0 + np.sin(0.3 * (i + j) + np.pi/4))
                phase_diff = np.abs(xi - x_norm[j])
                entanglement += coupling_strength * np.exp(-3.0 * phase_diff**2) * np.sin(8.0 * phase_diff + i*j + np.sin(2.0 * phase_diff))
        
        # Adaptive curvature modulation with dynamic tunneling wells
        tunneling = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale well structure with varying depths and positions
            wells = [(1.5, -0.9), (1.0, 0.7), (1.3, 1.1), (0.8, -1.2), (1.2, 0.3)]
            for depth, pos in wells:
                tunneling += depth * np.exp(-0.3 * (xi - pos)**2) * np.cos(4.0 * xi + pos + 0.5 * np.sin(3.0 * xi))
        
        # Multi-peak barrier landscape with dynamic scaling and quantum tunneling probabilities
        barriers = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Complex multi-peak structure with varying heights, widths, and positions
            peaks = [(1.8, 0.25), (1.1, 0.55), (1.4, 0.35), (0.9, 0.65)]
            for height, width in peaks:
                barriers += height * np.exp(-0.7 * ((xi - 0.6) / width)**2) * np.cos(3.0 * xi + 0.5 * np.sin(2.0 * xi))
        
        # Enhanced discrete energy levels with multi-harmonic quantum interference
        discrete = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Complex harmonic structure with multiple frequencies and amplitudes
            discrete += 1.0 * np.sin(6.0 * xi) + 0.5 * np.cos(8.0 * xi) + 0.2 * np.sin(12.0 * xi) + 0.1 * np.cos(15.0 * xi)
        
        # Fractal-like roughness with enhanced self-similarity and multi-scale coupling
        roughness = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale fractal structure with varying frequencies, amplitudes, and coupling strengths
            frequencies = [2.5, 4.5, 6.5, 8.5, 10.5]
            amplitudes = [0.6, 0.4, 0.25, 0.15, 0.1]
            for freq, amp in zip(frequencies, amplitudes):
                roughness += amp * np.sin(freq * xi) * np.cos(freq * xi + 0.3 * np.sin(freq * xi))
        
        # Enhanced dynamic scaling factor with dimensionality and frequency dependence
        dynamic_scale = 1.0 + 0.4 * np.cos(self.dim * 0.25) * np.sin(0.5 * self.dim)
        
        # Component weighting with adaptive complexity modulation
        weights = [0.28, 0.32, 0.18, 0.16, 0.06]
        
        return dynamic_scale * (weights[0] * entanglement + 
                               weights[1] * tunneling + 
                               weights[2] * barriers + 
                               weights[3] * discrete + 
                               weights[4] * roughness)