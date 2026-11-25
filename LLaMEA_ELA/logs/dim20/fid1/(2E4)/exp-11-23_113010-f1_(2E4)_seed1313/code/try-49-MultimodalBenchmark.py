import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced layered sinusoidal components with modified frequency ratios
        layer1 = np.sum(np.sin(8 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * np.exp(-0.5 * x_norm**2))
        layer2 = np.sum(np.sin(15 * np.pi * x_norm**1.3) * np.cos(5 * np.pi * x_norm**1.3) * np.exp(-0.4 * x_norm**2))
        layer3 = np.sum(np.sin(18 * np.pi * x_norm**2.2) * np.cos(9 * np.pi * x_norm**2.2) * np.exp(-0.6 * x_norm**2))
        
        # Modified polynomial basin terms with altered coefficients
        poly_basin = np.sum((0.7 * x_norm**5 + 0.3 * x_norm**4 + 0.1 * x_norm**3 + 0.05 * x_norm**2) / (1 + self.dim * 0.15))
        
        # Strengthened cross-dimensional interaction with modified kernel types
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                cross_interaction += (0.8 * np.exp(-dist**2) * np.sin(4 * np.pi * (x_norm[i] + x_norm[j])) + 
                                   0.3 * np.exp(-dist**3) * np.cos(3 * np.pi * (x_norm[i] - x_norm[j])))
        
        # Enhanced saddle structure with modified powers
        saddle = np.sum(x_norm**(4.0) * np.cos(2.5 * np.pi * x_norm) * np.sin(2.0 * np.pi * x_norm))
        
        # Modified chaotic component with altered coupling strength
        chaotic_component = 0.0
        if self.dim > 1:
            for i in range(self.dim):
                chaotic_component += 0.8 * np.sin(2.5 * np.pi * (x_norm[i] + 0.2 * x_norm[(i+1) % self.dim]))
        
        # Add noise and scale the function
        noise = 0.005 * np.random.random()
        
        return 2.2 * (layer1 + layer2 + layer3) + 1.3 * poly_basin + 0.9 * cross_interaction + 0.7 * saddle + 0.5 * chaotic_component + noise