import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.1
        self.c = 0.05
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Spherical component
        sphere = np.sum(x_norm**2)
        
        # Saddle region with asymmetric structure
        saddle = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**2)
        
        # Chaotic modulation using logistic map
        chaotic = 0.0
        for i in range(self.dim - 1):
            chaotic += np.sin(self.a * np.sin(self.b * x_norm[i]) + 
                            self.c * np.cos(self.a * x_norm[i+1]))
        
        # Dynamic conditioning based on position
        dynamic_cond = np.sum((1 + 0.5 * np.sin(3 * x_norm)) * 
                             (1 + 0.3 * np.cos(2 * x_norm)) * 
                             np.abs(x_norm)**1.5)
        
        # Asymmetric noise component
        noise = np.sum(np.exp(-self.b * (x_norm - 0.5)**2) * 
                      np.sin(5 * np.pi * x_norm) * 
                      (1 + 0.2 * np.random.rand()))
        
        # Cross-dimensional interaction with varying weights
        cross_interaction = 0.0
        for i in range(self.dim - 2):
            cross_interaction += (x_norm[i] * x_norm[i+1] * x_norm[i+2]) * \
                               np.cos(2 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Combined landscape
        return 0.5 * sphere + 0.3 * saddle + 0.2 * chaotic + \
               0.4 * dynamic_cond + 0.1 * noise + 0.3 * cross_interaction