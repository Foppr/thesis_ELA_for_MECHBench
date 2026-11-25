import numpy as np

class AdaptiveMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Spherical component with adaptive radius
        spherical = np.sum(x**2) / (2.0 * self.dim)
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.5)
            amp = 1.0 + 0.3 * np.cos(i * 0.7)
            sinusoidal += amp * np.sin(freq * x[i])**2
        
        # Exponential barrier terms to create ruggedness
        exponential = 0.0
        for i in range(self.dim):
            exp_term = np.exp(-0.5 * (x[i] - 1.0)**2) + np.exp(-0.5 * (x[i] + 1.0)**2)
            exponential += exp_term * (1.0 + 0.2 * np.sin(i))
            
        # Cross-dimensional coupling with adaptive weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 * (1.0 + np.sin(i * j * 0.3))
                coupling += weight * np.sin(x[i] * x[j]) * np.cos(x[i] - x[j])
                
        # Asymmetric conditioning with dimension-dependent scaling
        conditioning = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(i * 0.8)
            conditioning += scale * (x[i]**4 - 2.0 * x[i]**2)
            
        # Central attraction with varying strength
        center_attraction = 0.0
        for i in range(self.dim):
            center_attraction += 0.3 * np.exp(-0.5 * (x[i] - 0.5)**2) * np.cos(2.0 * x[i])
            
        # Global minimum at origin with additional noise term
        result = spherical + sinusoidal + exponential + coupling + conditioning + center_attraction
        
        return result