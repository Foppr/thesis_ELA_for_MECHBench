import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Spherical basin with exponential decay
        spherical = np.sum(x_normalized**2)
        exponential_decay = np.exp(-0.5 * spherical)
        
        # Trigonometric oscillations with varying frequencies and amplitudes
        trigonometric = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            amp = 0.3 + 0.7 * np.cos(i * 0.5)
            trigonometric += amp * np.sin(freq * np.pi * x_normalized[i]) * np.cos(freq * np.pi * x_normalized[i])
        
        # Cross-dimensional coupling with adaptive scaling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(2 * (x_normalized[i] - x_normalized[j]))
                scale_factor = 1.0 / (1.0 + np.exp(-0.5 * (i - j)))
                cross_coupling += coupling * scale_factor * (x_normalized[i]**2 + x_normalized[j]**2)
        
        # Multi-modal components with adaptive centers and widths
        multimodal = 0.0
        for i in range(self.dim):
            center = 0.5 * np.sin(i * 0.7)
            width = 0.2 + 0.3 * np.cos(i * 0.3)
            multimodal += np.exp(-0.5 * ((x_normalized[i] - center) / width)**2) * np.sin(3 * x_normalized[i])
        
        # Adaptive dimensionality scaling
        dim_scaling = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combine all components with carefully tuned weights
        return 0.3 * exponential_decay + 0.4 * trigonometric + 0.2 * cross_coupling + 0.1 * multimodal * dim_scaling