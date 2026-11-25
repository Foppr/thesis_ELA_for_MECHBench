import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Layered sinusoidal components with varying frequencies and amplitudes
        layer1 = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        layer2 = np.sum(np.sin(8 * np.pi * x_norm**2) * np.cos(4 * np.pi * x_norm**2))
        layer3 = np.sum(np.sin(10 * np.pi * x_norm**3) * np.cos(5 * np.pi * x_norm**3))
        
        # Polynomial basin terms with mixed degrees
        poly_basin = np.sum(0.5 * x_norm**4 + 0.3 * x_norm**3 + 0.1 * x_norm**2)
        
        # Cross-dimensional interaction using Gaussian kernel
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                cross_interaction += np.exp(-dist**2) * np.sin(2 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Asymmetric saddle structure with higher-order terms
        saddle = np.sum(x_norm**5 * np.cos(2 * np.pi * x_norm))
        
        # Add noise and scale the function
        noise = 0.01 * np.random.random()
        
        return 1.5 * (layer1 + layer2 + layer3) + 0.8 * poly_basin + 0.6 * cross_interaction + 0.4 * saddle + noise