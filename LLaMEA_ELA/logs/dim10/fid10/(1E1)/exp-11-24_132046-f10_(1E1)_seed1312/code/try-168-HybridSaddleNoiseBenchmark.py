import numpy as np

class HybridSaddleNoiseBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical component with varying radius
        spherical = np.sum(x_norm**2 * (1 + 0.3 * np.sin(5 * np.pi * x_norm)))
        
        # Saddle point structure with varying curvature
        saddle = np.sum((x_norm[:-1]**2 - x_norm[1:]**2) * (1 + 0.2 * np.cos(3 * np.pi * x_norm[:-1])))
        
        # Noise component with amplitude modulation
        noise = np.sum(np.random.normal(0, 0.1, self.dim) * (1 + 0.5 * np.sin(2 * np.pi * x_norm)))
        
        # Non-separable correlation with dimensionally dependent strength
        correlation = np.sum((x_norm[:-1] * x_norm[1:] * 
                             (1 + 0.4 * np.sin(4 * np.pi * x_norm[:-1]) * 
                              np.cos(3 * np.pi * x_norm[1:]))))
        
        # Asymmetric barrier with varying height
        barrier = np.sum(np.exp(-0.5 * (x_norm - 0.5)**2) * (1 + 0.3 * np.sin(6 * np.pi * x_norm)))
        
        # Dimensionally varying difficulty with power scaling
        difficulty = np.sum(np.abs(x_norm)**(1.5 + 0.5 * np.sin(2 * np.pi * x_norm)))
        
        # Combined landscape with weighted components
        return 0.8 * spherical + 0.6 * saddle + 0.3 * noise + 0.7 * correlation + 0.5 * barrier + 0.4 * difficulty