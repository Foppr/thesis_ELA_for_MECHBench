import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine map component with adaptive basin complexity
        chaos = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Adaptive basin depth based on dimension and position
            basin_depth = 1.0 + 0.5 * np.sin(0.7 * i) + 0.3 * np.cos(0.5 * xi)
            # Chaotic sine map with varying frequency and damping
            freq = 2.0 * (1.0 + 0.2 * np.sin(0.4 * i))
            damping = 0.8 + 0.1 * np.cos(0.6 * xi)
            chaos += basin_depth * np.sin(freq * xi) * np.exp(-damping * xi**2)
        
        # Energy-based attraction fields with multi-scale basins
        energy = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple attraction points with varying strengths
            attractor_strength = 1.5 + 0.8 * np.sin(0.3 * i)
            distance_sum = 0.0
            for j in range(1, 6):  # Up to 5 attraction points
                attractor_pos = 0.2 * np.sin(0.5 * (i + j))
                dist = np.abs(xi - attractor_pos)
                # Quadratic energy with dimensionally varying exponent
                exponent = 2.0 + 0.3 * np.cos(0.4 * i)
                distance_sum += attractor_strength * dist**exponent
            energy += distance_sum
        
        # Cross-dimensional coupling with phase-locked oscillators
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling range
                xi, xj = x_norm[i], x_norm[j]
                # Phase-locking with dynamic frequency modulation
                freq_mod = 1.0 + 0.4 * np.sin(0.3 * (i + j))
                phase_diff = freq_mod * (xi - xj)
                coupling += np.sin(phase_diff) * np.cos(phase_diff)
        
        # Adaptive scaling based on dimensionality and input magnitude
        scale_factor = 1.0 + 0.2 * np.sin(0.5 * self.dim) + 0.1 * np.tanh(np.sum(x_norm**2))
        
        # Weighted combination of components with dynamic balancing
        w1, w2, w3 = 0.4 + 0.1 * np.sin(self.dim * 0.3), 0.35 + 0.1 * np.cos(self.dim * 0.2), 0.25 + 0.1 * np.sin(self.dim * 0.4)
        
        return scale_factor * (w1 * chaos + w2 * energy + w3 * coupling)