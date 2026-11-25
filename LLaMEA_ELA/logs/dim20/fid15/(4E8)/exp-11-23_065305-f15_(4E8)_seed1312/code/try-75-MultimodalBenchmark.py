import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Enhanced radial basis function component with chaotic centers and varying widths
        rbfs = 0
        for i in range(15):
            center = np.sin(i * np.pi / 7.0) * 0.9
            width = 15 + 5 * np.cos(i * np.pi / 8.0)
            rbfs += np.exp(-width * np.sum((x_norm - center)**2)) * np.sin(12 * i * x_norm[0] + 2 * np.cos(i))
        
        # Sinusoidal coupling with adaptive frequency and phase modulation
        coupling = 0
        for i in range(self.dim):
            freq = 3 + 4 * np.sin(i * np.pi / (self.dim + 1))
            phase = np.cos(i * np.pi / 6.0)
            coupling += np.sin(freq * x_norm[i] + phase) * np.cos(freq * x_norm[(i + 1) % self.dim] + phase)
        
        # Enhanced dimensional interaction with cubic and quartic terms
        dim_interaction = 0
        for i in range(self.dim):
            weight = np.exp(-0.3 * i)
            dim_interaction += weight * (x_norm[i]**4 + 0.5 * x_norm[i]**3) * np.sin(9 * x_norm[i])
        
        # Chaotic modulation with cross-dimensional interference and dynamic coupling
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(12 * x_norm[i] + np.cos(6 * x_norm[(i + 3) % self.dim]) + 0.5 * np.sin(3 * x_norm[i])) * np.cos(10 * x_norm[i])
        
        # Multi-scale sinusoidal structure with dynamic frequency modulation and amplitude scaling
        multiscale = 0
        for scale in [1, 2, 4, 8]:
            multiscale += np.sum(np.sin(scale * x_norm) * np.cos(scale * x_norm**3) * (1 + 0.3 * np.sin(scale * x_norm[0])))
        
        # Non-linear transformation with enhanced penalty for deviation from global optimum
        shift = 0.25
        shifted = x_norm - shift
        penalty = 0.3 * np.sum(shifted**5) + 0.1 * np.sum(shifted**6)
        
        result = rbfs + coupling + dim_interaction + chaotic + multiscale + penalty
        
        return result