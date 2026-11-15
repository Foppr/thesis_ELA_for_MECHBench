import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Enhanced fractal terrain with higher frequency components and chaos
        fractal = np.sum(np.sin(20 * np.pi * x_norm) * np.sin(40 * np.pi * x_norm) * 
                         np.sin(80 * np.pi * x_norm) * np.sin(160 * np.pi * x_norm) * 
                         np.cos(30 * np.pi * x_norm**2))
        
        # Adaptive radial scaling with exponential barrier terms
        radial = np.sum(np.exp(-0.5 * (np.linalg.norm(x_norm, axis=0)**2)) * 
                       np.cos(10 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm))
        
        # Mixed exponential-barrier Gaussian peaks with varying intensities
        gaussian = np.sum(np.exp(-0.5 * ((x_norm - 0.3)**2 / 0.05 + (x_norm + 0.3)**2 / 0.1)) * 
                         np.sin(12 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm))
        
        # Cross-term interactions with polynomial and trigonometric mixing
        cross = np.sum((x_norm**3 + x_norm**2) * np.sin(25 * np.pi * x_norm) * 
                      np.cos(20 * np.pi * x_norm) * np.sin(15 * np.pi * x_norm))
        
        # Chaotic modulation with logistic-like behavior and multiple feedback loops
        chaotic = np.sum(np.sin(35 * np.pi * x_norm**3) * np.cos(40 * np.pi * x_norm**3) * 
                        np.sin(45 * np.pi * x_norm**3) * np.cos(50 * np.pi * x_norm**3))
        
        # Additional mixed barrier terms for increased conditioning
        barriers = np.sum(np.exp(-0.5 * (x_norm**2 + 0.5 * x_norm**4)) * 
                         np.sin(18 * np.pi * x_norm) * np.cos(14 * np.pi * x_norm))
        
        # Combine all terms with optimized weights for challenging landscape
        return 0.3 * fractal + 0.25 * radial + 0.2 * gaussian + 0.15 * cross + 0.08 * chaotic + 0.02 * barriers