import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Fractal-like terrain using recursive sine modulation
        fractal = np.sum(np.sin(10 * np.pi * x_norm) * np.sin(20 * np.pi * x_norm) * 
                         np.sin(40 * np.pi * x_norm) * np.sin(80 * np.pi * x_norm))
        
        # Radial gradient field with varying intensity
        radial = np.sum((np.linalg.norm(x_norm, axis=0) + 0.1) * 
                       np.cos(5 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Asymmetric Gaussian peaks with varying widths and heights
        gaussian = np.sum(np.exp(-0.5 * ((x_norm - 0.5)**2 / 0.1 + (x_norm + 0.5)**2 / 0.2)) * 
                         np.sin(8 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Cross-term interactions creating non-separability
        cross = np.sum(np.sin(15 * np.pi * x_norm) * np.cos(12 * np.pi * x_norm) * 
                      np.sin(9 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Chaotic modulation using logistic map-like behavior
        chaotic = np.sum(np.sin(25 * np.pi * x_norm**2) * np.cos(30 * np.pi * x_norm**2) * 
                        np.sin(35 * np.pi * x_norm**2))
        
        # Combine all terms with adaptive weights
        return 0.25 * fractal + 0.2 * radial + 0.25 * gaussian + 0.15 * cross + 0.15 * chaotic