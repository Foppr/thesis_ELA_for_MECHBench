import numpy as np

class MultimodalGaussianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute cluster centers in a structured pattern
        self.clusters = np.random.randn(10, dim) * 2.0
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        x_normalized = x / 5.0
        
        # Gaussian cluster component with varying scales and positions
        gaussian = 0.0
        for i in range(10):
            center = self.clusters[i]
            scale = 0.5 + 0.5 * np.sin(i * 0.5)
            dist = np.sum((x_normalized - center)**2)
            gaussian += scale * np.exp(-dist / (2 * 0.3**2))
        
        # Sine-wave modulation to create periodic structure
        sine_mod = 0.0
        for i in range(self.dim):
            freq = 1.0 + 2.0 * np.sin(i * 0.3)
            sine_mod += np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i])
        
        # Adaptive conditioning based on dimension index
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 2.0 * np.sin(i * 0.4)
            conditioning += cond_factor * x_normalized[i]**4
        
        # Cross-term interactions with cosine coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.cos(x_normalized[i] * x_normalized[j]) * (x_normalized[i] - x_normalized[j])**2
        
        # Add noise to create ruggedness
        noise = 0.1 * np.random.rand()
        
        # Combine all components with weighted contributions
        return 0.4 * gaussian + 0.3 * sine_mod + 0.2 * conditioning + 0.08 * cross_term + noise