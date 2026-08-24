import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Nested fractal terrain with self-similar sine-wave patterns at multiple scales
        fractal = np.sum(np.sin(20 * np.pi * x_norm) * np.sin(40 * np.pi * x_norm) * 
                         np.sin(80 * np.pi * x_norm) * np.sin(160 * np.pi * x_norm) * 
                         np.sin(320 * np.pi * x_norm))
        
        # Quantum-like interference patterns with phase modulation
        quantum = np.sum(np.sin(15 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm) * 
                         np.sin(25 * np.pi * x_norm) * np.cos(25 * np.pi * x_norm) * 
                         np.sin(35 * np.pi * x_norm))
        
        # Dynamic radial gradient with time-varying intensity
        radial = np.sum((np.linalg.norm(x_norm, axis=0) + 0.05) * 
                       np.cos(10 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm) * 
                       np.cos(5 * np.pi * x_norm))
        
        # Asymmetric Gaussian peaks with dynamic widths and heights
        gaussian = np.sum(np.exp(-0.5 * ((x_norm - 0.3)**2 / 0.05 + (x_norm + 0.3)**2 / 0.15)) * 
                         np.sin(12 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm) * 
                         np.exp(-0.1 * np.linalg.norm(x_norm, axis=0)**2))
        
        # Cross-term interactions with non-linear coupling
        cross = np.sum(np.sin(20 * np.pi * x_norm) * np.cos(18 * np.pi * x_norm) * 
                      np.sin(16 * np.pi * x_norm) * np.cos(14 * np.pi * x_norm) * 
                      np.sin(12 * np.pi * x_norm))
        
        # Chaotic modulation with double logistic map behavior
        chaotic = np.sum(np.sin(30 * np.pi * x_norm**2) * np.cos(35 * np.pi * x_norm**2) * 
                        np.sin(40 * np.pi * x_norm**2) * np.cos(45 * np.pi * x_norm**2) * 
                        np.sin(50 * np.pi * x_norm**2))
        
        # Dynamic scaling factor that varies with dimensionality
        scaling = 1.0 + 0.5 * np.sin(self.dim * np.pi / 4.0)
        
        # Combine all terms with adaptive weights and scaling
        return scaling * (0.3 * fractal + 0.2 * quantum + 0.2 * radial + 0.15 * gaussian + 0.1 * cross + 0.05 * chaotic)