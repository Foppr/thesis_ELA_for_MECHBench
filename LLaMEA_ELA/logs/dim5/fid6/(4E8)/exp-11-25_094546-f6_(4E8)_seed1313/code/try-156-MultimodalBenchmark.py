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
                interference += 1.3 * np.sin(freq * xi + phase) * np.cos(freq * xi + phase)
        
        # Adaptive entanglement with dimensionally varying coupling strengths
        entanglement = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                # Dynamic coupling with altered strength and position dependence
                coupling_strength = 0.8 * (1.0 + np.sin(0.35 * (i + j) + self.dim))
                distance = np.abs(x_norm[i] - x_norm[j])
                entanglement += coupling_strength * np.exp(-distance**2.7) * np.sin(4.5 * (xi + x_norm[j]))
        
        # Dynamic tunneling landscape with quantum-like probability amplitudes
        tunneling = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple tunneling wells with varying depths and positions
            wells = [(1.1, -1.3), (0.9, 0.0), (1.6, 1.1), (0.7, 2.1)]
            for depth, pos in wells:
                tunneling += 1.4 * depth * np.exp(-0.5 * (xi - pos)**2) * np.sin(2.7 * xi + pos)
        
        # Fractal energy landscape with recursive self-similarity
        fractal = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Recursive fractal components with decreasing scale and modified frequencies
            scales = [1.0, 0.5, 0.25]
            for scale in scales:
                fractal += 0.9 * scale * np.sin(9.5 * xi * scale) * np.cos(4.7 * xi * scale)
        
        # Adaptive barrier structure with quantum tunneling probabilities
        barriers = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple overlapping barriers with varying heights and widths
            barrier_params = [(1.3, 0.35), (1.0, 0.65), (1.5, 0.45)]
            for height, width in barrier_params:
                barriers += 1.2 * height * np.exp(-0.5 * ((xi - 0.5) / width)**2) * np.cos(2.7 * xi)
        
        # Dimensional scaling with quantum-inspired complexity
        dim_scale = 1.0 + 0.4 * np.sin(self.dim * 0.6)
        
        # Component weighting based on dimensionality and complexity
        weights = {
            'interference': 0.28 + 0.07 * np.cos(self.dim * 0.25),
            'entanglement': 0.31 + 0.12 * np.sin(self.dim * 0.2),
            'tunneling': 0.18 + 0.1 * np.tanh(self.dim * 0.15),
            'fractal': 0.15 + 0.08 * np.cos(self.dim * 0.3),
            'barriers': 0.08 + 0.06 * np.sin(self.dim * 0.35)
        }
        
        return dim_scale * (weights['interference'] * interference + 
                           weights['entanglement'] * entanglement + 
                           weights['tunneling'] * tunneling + 
                           weights['fractal'] * fractal + 
                           weights['barriers'] * barriers)