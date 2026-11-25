import numpy as np

class AdaptiveRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Periodic Gaussian ridges with adaptive widths and heights
        ridge = 0.0
        for i in range(self.dim):
            # Adaptive ridge parameters based on dimension index
            width = 0.5 + 0.3 * np.sin(i * 0.7)
            height = 1.5 + 0.8 * np.cos(i * 0.5)
            center = 0.4 * np.sin(i * 0.9)
            
            # Gaussian ridge function
            ridge += height * np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Exponential decay interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Exponentially decaying interaction with chaotic modulation
                dist = np.abs(x_scaled[i] - x_scaled[j])
                weight = 2.0 * np.exp(-dist * 3.0) * (1.0 + 0.3 * np.sin(i * j * 0.8))
                interaction += weight * np.cos(2.0 * (x_scaled[i] + x_scaled[j]))
        
        # Adaptive noise component with dimension-dependent intensity
        noise = 0.0
        for i in range(self.dim):
            # Chaotic noise intensity modulation
            intensity = 0.1 + 0.05 * np.sin(i * 0.6) * np.cos(i * 0.4)
            noise += intensity * np.random.normal(0, 1)
        
        # Multi-scale periodic structure with varying frequencies
        periodic = 0.0
        for scale in [1, 2, 3, 5]:
            for i in range(self.dim):
                freq = scale * (1.0 + 0.2 * np.sin(i * 0.5))
                periodic += np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Combined function with adaptive weights
        return 1.5 * ridge + 0.8 * interaction + 0.3 * noise + 1.2 * periodic