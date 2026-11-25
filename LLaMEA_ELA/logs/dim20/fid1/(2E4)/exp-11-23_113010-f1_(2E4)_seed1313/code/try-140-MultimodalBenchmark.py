import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component with Hermite polynomials
        chaos_component = 0.0
        for i in range(self.dim):
            # Hermite polynomial of degree 3
            h3 = 2 * x_norm[i]**3 - 3 * x_norm[i]
            chaos_component += h3 * np.exp(-0.5 * x_norm[i]**2)
        
        # Radial basis function with multi-scale centers and varying widths
        rbf_component = 0.0
        num_centers = min(10, self.dim * 2)
        for j in range(num_centers):
            center = np.sin(j * np.pi / num_centers) * 0.8
            width = 0.5 + 0.3 * np.cos(j * np.pi / num_centers)
            distance = np.sum((x_norm - center)**2)
            rbf_component += np.exp(-distance / (2 * width**2))
        
        # Sinusoidal modulation with frequency coupling and amplitude scaling
        sin_component = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1) * (1 + 0.2 * np.sin(i * np.pi / self.dim))
            amp = 1.0 + 0.5 * np.cos(i * np.pi / (self.dim + 1))
            sin_component += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2)
        
        # Cross-term interactions with chaotic coupling
        cross_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(3**(i+j) * np.pi * x_norm[i] * x_norm[j])
                cross_component += coupling * (x_norm[i]**2 + x_norm[j]**2)
        
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * np.pi / 4)
        
        # Combine all components with dynamic weighting
        return scale_factor * (0.6 * chaos_component + 
                              0.3 * rbf_component + 
                              0.2 * sin_component + 
                              0.1 * cross_component)