import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis components with chaotic modulation
        gaussian = 0
        for i in range(self.dim):
            gaussian += np.exp(-0.5 * ((x[i] - np.sin(i * np.pi / self.dim)) / (1.0 + 0.1 * np.abs(x[i])))**2)
        
        # Adaptive sine coupling terms with dynamic frequencies
        sine_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 2 * np.pi * (1 + 0.5 * np.sin(i * np.pi / self.dim))
                freq_j = 2 * np.pi * (1 + 0.5 * np.cos(j * np.pi / self.dim))
                sine_coupling += np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
        
        # Cross-dimensional quadratic interactions with varying weights
        quad_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.3 * (1 + np.sin((i + j) * np.pi / self.dim))
                quad_interaction += weight * (x[i] - x[j])**2
        
        # Chaotic cosine modulation with dynamic amplitude
        cos_modulation = 0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * np.pi / self.dim)
            cos_modulation += amp * np.cos(3 * np.pi * x[i] + 0.5 * np.sin(2 * np.pi * x[i]))
        
        # Global scaling and shifting
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        shift = 0.1 * np.sum(np.abs(x))
        
        # Combine all components
        return scale_factor * (0.5 * gaussian + 0.3 * sine_coupling + 0.2 * quad_interaction + 0.4 * cos_modulation) + shift