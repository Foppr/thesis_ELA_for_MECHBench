import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.chaos_factor = 3.0 + np.random.rand() * 2.0
        self.elliptic_strength = 0.5 + np.random.rand() * 1.5
        self.cosine_freq = 1.0 + np.random.rand() * 2.0
        self.time_varying_factor = 0.1 + np.random.rand() * 0.3
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic neural network component with time-varying weights
        chaotic_nn = 0.0
        for i in range(self.dim):
            weight = np.sin(i * self.chaos_factor + self.time_varying_factor * np.sum(x))
            chaotic_nn += weight * np.sin(x[i] * 2.0) * np.cos(x[i] * 1.5)
        
        # Adaptive elliptic potential with dimension-dependent scaling
        elliptic_potential = 0.0
        for i in range(self.dim):
            scale = 1.0 + self.elliptic_strength * np.sin(i * 0.5)
            elliptic_potential += scale * (x[i]**2) * (np.cos(x[i]) + 1.0)
        
        # Dynamic cosine wave interference pattern
        cosine_wave = 0.0
        for i in range(self.dim):
            freq = self.cosine_freq + np.sin(i * 0.3) * 0.5
            cosine_wave += np.cos(x[i] * freq) * np.sin(x[i] * 0.7)
        
        # Cross-dimensional coupling with adaptive weights
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] - x[j])**2 * np.sin((x[i] + x[j]) * 0.5)
        
        # Time-varying difficulty modifier
        difficulty = 1.0 + self.time_varying_factor * np.sum(np.sin(x))
        
        # Combine all components with dynamic weighting
        result = (0.4 * chaotic_nn + 
                 0.3 * elliptic_potential + 
                 0.2 * cosine_wave + 
                 0.1 * coupling) * difficulty
        
        return result