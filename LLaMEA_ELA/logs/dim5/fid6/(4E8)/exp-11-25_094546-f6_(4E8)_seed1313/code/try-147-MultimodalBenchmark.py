import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum-like interference patterns with dynamic phase modulation
        interference = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-frequency quantum interference terms with modified coefficients
            frequencies = [2.0, 3.5, 5.0, 7.0]
            phases = [0.0, np.pi/4, np.pi/2, 3*np.pi/4]
            for freq, phase in zip(frequencies, phases):
                interference += 1.2 * np.sin(freq * xi + phase) * np.cos(freq * xi + phase)
        
        # Adaptive entanglement with dimensionally varying coupling strengths
        entanglement = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                # Dynamic coupling with altered strength and position dependence
                coupling_strength = 0.7 * (1.0 + np.sin(0.3 * (i + j) + self.dim))
                distance = np.abs(x_norm[i] - x_norm[j])
                entanglement += coupling_strength * np.exp(-distance**2.5) * np.sin(4.0 * (xi + x_norm[j]))
        
        # Dynamic tunneling landscape with quantum-like probability amplitudes
        tunneling = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple tunneling wells with varying depths and positions
            wells = [(1.0, -1.2), (0.8, 0.0), (1.5, 1.0), (0.6, 2.0)]
            for depth, pos in wells:
                tunneling += 1.3 * depth * np.exp(-0.5 * (xi - pos)**2) * np.sin(2.5 * xi + pos)
        
        # Fractal energy landscape with recursive self-similarity
        fractal = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Recursive fractal components with decreasing scale and modified frequencies
            scales = [1.0, 0.5, 0.25]
            for scale in scales:
                fractal += 0.8 * scale * np.sin(9.0 * xi * scale) * np.cos(4.5 * xi * scale)
        
        # Adaptive barrier structure with quantum tunneling probabilities
        barriers = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple overlapping barriers with varying heights and widths
            barrier_params = [(1.2, 0.3), (0.9, 0.6), (1.4, 0.4)]
            for height, width in barrier_params:
                barriers += 1.1 * height * np.exp(-0.5 * ((xi - 0.5) / width)**2) * np.cos(2.5 * xi)
        
        # Dimensional scaling with quantum-inspired complexity
        dim_scale = 1.0 + 0.35 * np.sin(self.dim * 0.55)
        
        # Component weighting based on dimensionality and complexity
        weights = {
            'interference': 0.27 + 0.06 * np.cos(self.dim * 0.22),
            'entanglement': 0.32 + 0.11 * np.sin(self.dim * 0.17),
            'tunneling': 0.19 + 0.09 * np.tanh(self.dim * 0.12),
            'fractal': 0.14 + 0.07 * np.cos(self.dim * 0.27),
            'barriers': 0.08 + 0.05 * np.sin(self.dim * 0.32)
        }
        
        return dim_scale * (weights['interference'] * interference + 
                           weights['entanglement'] * entanglement + 
                           weights['tunneling'] * tunneling + 
                           weights['fractal'] * fractal + 
                           weights['barriers'] * barriers)