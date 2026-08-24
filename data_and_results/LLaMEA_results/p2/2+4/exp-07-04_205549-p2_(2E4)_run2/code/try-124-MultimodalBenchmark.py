import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        quadratic = np.sum(x_norm**2)
        
        # Radial component with multiple peaks
        radial = 0.0
        for i in range(self.dim):
            radial += 2.0 * np.exp(-0.5 * (x_norm[i]**2)) * np.cos(10 * np.pi * x_norm[i])
        
        # Dynamic phase-shifted sinusoidal terms
        phase_shifted = 0.0
        for i in range(self.dim):
            phase = 0.3 * np.sin(0.5 * i * np.pi) * np.cos(0.7 * i * np.pi)
            freq = 3.0 + 2.0 * np.sin(i * 0.4)
            amp = 1.5 + 0.8 * np.cos(i * 0.3)
            phase_shifted += amp * np.sin(freq * np.pi * x_norm[i] + phase) * np.exp(-0.3 * x_norm[i]**2)
        
        # Cross-dimensional interaction with adaptive weights
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.sin(0.2 * (i + j))
                cross_interaction += weight * np.sin(20 * np.pi * (x_norm[i]**2 + x_norm[j]**2)) * np.cos(15 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Chaotic component with exponential decay
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 1.2 * np.sin(40 * np.pi * x_norm[i]) * np.cos(35 * np.pi * x_norm[i]) * np.exp(-0.25 * x_norm[i]**2)
        
        # Multi-scale oscillatory term
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += 0.8 * np.sin(25 * np.pi * x_norm[i]) * np.cos(20 * np.pi * x_norm[i]) * np.sin(15 * np.pi * x_norm[i])
        
        # Radial basis function with variable centers
        radial_basis = 0.0
        for i in range(self.dim):
            center = 0.5 * np.sin(0.3 * i * np.pi)
            radial_basis += 0.6 * np.exp(-2.0 * (x_norm[i] - center)**2) * np.sin(30 * np.pi * (x_norm[i] - center))
        
        # Adaptive frequency modulation
        adaptive_freq = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(0.4 * i * np.pi)
            adaptive_freq += 0.9 * np.sin(freq_mod * 25 * np.pi * x_norm[i]) * np.exp(-0.4 * x_norm[i]**2)
        
        # Combined penalty term
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.4 * (x_norm[i]**8 - 4 * x_norm[i]**6 + 6 * x_norm[i]**4 - 4 * x_norm[i]**2 + 1)
        
        # Global structure with radial symmetry
        global_structure = 0.0
        dist = np.sqrt(np.sum(x_norm**2))
        global_structure = 1.5 * np.exp(-0.5 * dist**2) * np.sin(12 * np.pi * dist)
        
        return quadratic + radial + phase_shifted + cross_interaction + chaotic + multi_scale + radial_basis + adaptive_freq + penalty + global_structure