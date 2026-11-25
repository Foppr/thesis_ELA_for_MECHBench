import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis components with enhanced chaotic modulation
        gaussian = 0
        for i in range(self.dim):
            gaussian += np.exp(-0.5 * ((x[i] - np.sin(i * np.pi / self.dim)) / (1.0 + 0.2 * np.abs(x[i])))**2)
        
        # Modified adaptive sine coupling terms with altered frequencies
        sine_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 3 * np.pi * (1 + 0.3 * np.sin(i * np.pi / self.dim))
                freq_j = 3 * np.pi * (1 + 0.3 * np.cos(j * np.pi / self.dim))
                sine_coupling += np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
        
        # Altered cross-dimensional quadratic interactions with different weights
        quad_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 * (1 + np.sin((i + j) * np.pi / self.dim))
                quad_interaction += weight * (x[i] - x[j])**2
        
        # Enhanced chaotic cosine modulation with variable amplitude
        cos_modulation = 0
        for i in range(self.dim):
            amp = 1.5 + 0.3 * np.sin(i * np.pi / self.dim)
            cos_modulation += amp * np.cos(4 * np.pi * x[i] + 0.4 * np.sin(3 * np.pi * x[i]))
        
        # Global scaling and shifting
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        shift = 0.15 * np.sum(np.abs(x))
        
        # Combine all components
        return scale_factor * (0.4 * gaussian + 0.35 * sine_coupling + 0.25 * quad_interaction + 0.45 * cos_modulation) + shift