import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with multiple frequency harmonics
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.sin(5 * np.pi * r) * np.cos(3 * np.pi * r) + 0.5 * np.sin(12 * np.pi * r)
        
        # Periodic oscillations in each dimension with varying amplitudes
        periodic = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) + 
                         0.3 * np.sin(7 * np.pi * x_norm**2))
        
        # Cross-dimensional interaction terms with varying coupling strengths
        cross_dim = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim += np.sin(np.pi * (x_norm[i] + x_norm[j])) * np.cos(np.pi * (x_norm[i] - x_norm[j]))
        
        # Multi-scale fractal-like structure with nested minima
        fractal = 0.0
        for k in range(1, 6):
            fractal += (1.0 / k) * np.sin(k * np.pi * x_norm**1.5) * np.cos(k * np.pi * x_norm**1.3)
        
        # Adaptive noise-like perturbations based on position
        noise = np.sum(0.1 * np.sin(25 * x_norm) * np.cos(18 * x_norm))
        
        # Combine all components with appropriate weights
        return 2.0 * radial + 1.5 * periodic + 0.8 * cross_dim + 0.6 * fractal + 0.3 * noise