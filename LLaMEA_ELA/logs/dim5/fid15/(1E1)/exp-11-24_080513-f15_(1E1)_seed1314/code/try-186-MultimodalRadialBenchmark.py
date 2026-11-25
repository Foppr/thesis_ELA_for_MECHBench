import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial basis function component with multiple centers
        rbfs = 0.0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        for i in range(self.dim):
            center_idx = i % len(centers)
            dist = np.abs(x_normalized[i] - centers[center_idx])
            rbfs += np.exp(-dist * 5.0) * np.sin(dist * 10.0)
        
        # Sinusoidal wave component with varying frequencies
        waves = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            waves += np.sin(x_normalized[i] * freq) * np.cos(x_normalized[i] * freq * 0.5)
        
        # Exponential decay component with radial symmetry
        decay = 0.0
        for i in range(self.dim):
            decay += np.exp(-np.abs(x_normalized[i]) * 2.0) * (1.0 + 0.5 * np.sin(x_normalized[i] * 7.0))
        
        # Cross-term interactions with polynomial coupling
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                cross += (x_normalized[i]**2) * (x_normalized[j]**3) * np.sin(x_normalized[i] + x_normalized[j])
        
        # Add noise component for increased complexity
        noise = 0.0
        for i in range(self.dim):
            noise += np.random.normal(0, 0.01) * np.cos(x_normalized[i] * 15.0)
        
        # Combine all components with adaptive weights
        return (0.3 * rbfs + 0.25 * waves + 0.2 * decay + 
                0.15 * cross + 0.1 * noise)