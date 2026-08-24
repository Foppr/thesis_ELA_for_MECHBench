import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base with dynamic conditioning
        base = np.sum(x_norm**2)
        
        # Multi-scale sinusoidal interference with varying amplitudes and frequencies
        interference = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 1)
            amp = 3.0 + 2.0 * np.sin(i * 0.7)
            interference += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * 0.5 * np.pi * x_norm[i])
        
        # Asymmetric saddle points with position-dependent steepness
        saddles = 0.0
        for i in range(self.dim):
            steepness = 1.0 + 0.5 * np.sin(i * 0.3)
            saddles += steepness * (x_norm[i]**4 - 2 * x_norm[i]**2) * np.exp(-0.2 * x_norm[i]**2)
        
        # Dynamic conditioning based on coordinate values
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (1.0 + 0.3 * np.sin(10 * x_norm[i])) * x_norm[i]**6
        
        # Cross-dimensional interaction terms with exponential decay
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                cross_interaction += 0.5 * np.exp(-dist**2) * np.sin(50 * dist)
        
        # Global multimodal structure with chaotic modulation
        chaotic_structure = 0.0
        for i in range(self.dim):
            freq_mod = 20 + 10 * np.sin(i * 0.4)
            chaotic_structure += 0.4 * np.sin(freq_mod * x_norm[i]) * np.cos(freq_mod * x_norm[i] * 0.5) * np.exp(-0.1 * x_norm[i]**2)
        
        # Non-separable multimodal component
        nonsep = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                nonsep += 0.3 * np.sin(20 * (x_norm[i]**2 + x_norm[j]**2)) * np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2))
        
        return base + interference + saddles + conditioning + cross_interaction + chaotic_structure + nonsep