import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Nested fractal terrain using multiple sine-wave recursive modulations
        fractal = np.sum(np.sin(15 * np.pi * x_norm) * np.sin(30 * np.pi * x_norm) * 
                         np.sin(60 * np.pi * x_norm) * np.sin(120 * np.pi * x_norm) * 
                         np.sin(240 * np.pi * x_norm))
        
        # Adaptive radial gradient field with dynamic scaling
        radial = np.sum((np.linalg.norm(x_norm, axis=0) + 0.05) * 
                       np.cos(7 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm) * 
                       np.cos(3 * np.pi * x_norm))
        
        # Asymmetric Gaussian peaks with dynamic widths and heights
        gaussian = np.sum(np.exp(-0.5 * ((x_norm - 0.3)**2 / 0.08 + (x_norm + 0.7)**2 / 0.15)) * 
                         np.sin(10 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) * 
                         np.sin(6 * np.pi * x_norm))
        
        # Complex cross-term interactions with higher-order polynomial mixing
        cross = np.sum(np.sin(20 * np.pi * x_norm) * np.cos(18 * np.pi * x_norm) * 
                      np.sin(16 * np.pi * x_norm) * np.cos(14 * np.pi * x_norm) * 
                      np.sin(12 * np.pi * x_norm))
        
        # Chaotic modulation using higher-frequency logistic-like behavior
        chaotic = np.sum(np.sin(40 * np.pi * x_norm**2) * np.cos(45 * np.pi * x_norm**2) * 
                        np.sin(50 * np.pi * x_norm**2) * np.cos(55 * np.pi * x_norm**2))
        
        # Additional non-separable mixed terms
        mixed = np.sum(np.sin(25 * np.pi * x_norm) * np.cos(22 * np.pi * x_norm) * 
                      np.sin(19 * np.pi * x_norm) * np.cos(17 * np.pi * x_norm) * 
                      np.sin(14 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm))
        
        # Combine all terms with optimized weights
        return 0.2 * fractal + 0.18 * radial + 0.22 * gaussian + 0.18 * cross + 0.15 * chaotic + 0.07 * mixed