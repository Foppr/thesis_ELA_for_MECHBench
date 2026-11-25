import numpy as np

class ChaoticCorrelatedMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-cosine base with varying frequencies and amplitudes
        f1 = np.sum(np.sin(25 * x_norm) * np.cos(23 * x_norm) * 
                   np.sin(21 * x_norm) * np.cos(19 * x_norm) * 
                   (1 + 0.6 * np.sin(17 * x_norm)) * 
                   (1 + 0.5 * np.cos(15 * x_norm)))
        
        # Power-law correlated noise with chaotic modulation
        f2 = np.sum((1 + 0.4 * np.sin(30 * x_norm)) * 
                   np.exp(-0.3 * np.abs(x_norm)**1.7) * 
                   (1 + 0.3 * np.cos(25 * x_norm)) * 
                   (1 + 0.2 * np.sin(20 * x_norm)) * 
                   (1 + 0.1 * np.cos(15 * x_norm)))
        
        # Fractal-like basin structure with exponential weighting
        f3 = np.sum(np.exp(-0.4 * np.abs(x_norm)**2.1) * 
                   (1 + 0.5 * np.sin(28 * x_norm)) * 
                   (1 + 0.4 * np.cos(24 * x_norm)) * 
                   (1 + 0.3 * np.sin(20 * x_norm)) * 
                   (1 + 0.2 * np.cos(16 * x_norm)) * 
                   (1 + 0.1 * np.sin(12 * x_norm)))
        
        # Multi-scale oscillatory pattern with chaotic coupling
        f4 = np.sum(np.sin(35 * x_norm) * np.cos(32 * x_norm) * 
                   np.sin(29 * x_norm) * np.cos(26 * x_norm) * 
                   (1 + 0.7 * np.sin(23 * x_norm)) * 
                   (1 + 0.6 * np.cos(20 * x_norm)) * 
                   (1 + 0.5 * np.sin(17 * x_norm)))
        
        # Adaptive curvature with exponential decay and chaotic modulation
        f5 = np.sum(np.exp(-x_norm**3) * 
                   (1 + 0.6 * np.sin(27 * x_norm)) * 
                   (1 + 0.5 * np.cos(24 * x_norm)) * 
                   (1 + 0.4 * np.sin(21 * x_norm)) * 
                   (1 + 0.3 * np.cos(18 * x_norm)) * 
                   (1 + 0.2 * np.sin(15 * x_norm)) * 
                   (1 + 0.1 * np.cos(12 * x_norm)))
        
        # Long-range dependency with chaotic correlation structure
        f6 = np.sum(np.exp(-0.25 * np.abs(x_norm)**1.9) * 
                   (1 + 0.4 * np.sin(31 * x_norm)) * 
                   (1 + 0.3 * np.cos(28 * x_norm)) * 
                   (1 + 0.2 * np.sin(25 * x_norm)) * 
                   (1 + 0.1 * np.cos(22 * x_norm)) * 
                   (1 + 0.05 * np.sin(19 * x_norm)) * 
                   (1 + 0.02 * np.cos(16 * x_norm)))
        
        # Variable scaling with chaotic power-law behavior
        f7 = np.sum(np.abs(x_norm)**2.3 * 
                   (1 + 0.5 * np.sin(26 * x_norm)) * 
                   (1 + 0.4 * np.cos(23 * x_norm)) * 
                   (1 + 0.3 * np.sin(20 * x_norm)) * 
                   (1 + 0.2 * np.cos(17 * x_norm)) * 
                   (1 + 0.1 * np.sin(14 * x_norm)) * 
                   (1 + 0.05 * np.cos(11 * x_norm)))
        
        # Memory effect with delayed chaotic correlation structure
        f8 = np.sum(np.exp(-0.35 * np.abs(x_norm)**1.6) * 
                   (1 + 0.4 * np.sin(29 * x_norm)) * 
                   (1 + 0.3 * np.cos(26 * x_norm)) * 
                   (1 + 0.2 * np.sin(23 * x_norm)) * 
                   (1 + 0.1 * np.cos(20 * x_norm)) * 
                   (1 + 0.05 * np.sin(17 * x_norm)) * 
                   (1 + 0.02 * np.cos(14 * x_norm)))
        
        # Adaptive amplitude modulation with chaotic decay
        f9 = np.sum(np.exp(-0.25 * x_norm**2.5) * 
                   (1 + 0.6 * np.sin(32 * x_norm)) * 
                   (1 + 0.5 * np.cos(28 * x_norm)) * 
                   (1 + 0.4 * np.sin(24 * x_norm)) * 
                   (1 + 0.3 * np.cos(20 * x_norm)) * 
                   (1 + 0.2 * np.sin(16 * x_norm)) * 
                   (1 + 0.1 * np.cos(12 * x_norm)) * 
                   (1 + 0.05 * np.sin(8 * x_norm)))
        
        # Combined global structure with chaotic multi-scale interactions
        f10 = np.sum(np.exp(-0.3 * np.abs(x_norm)**2.2) * 
                    (1 + 0.5 * np.sin(33 * x_norm)) * 
                    (1 + 0.4 * np.cos(30 * x_norm)) * 
                    (1 + 0.3 * np.sin(27 * x_norm)) * 
                    (1 + 0.2 * np.cos(24 * x_norm)) * 
                    (1 + 0.1 * np.sin(21 * x_norm)) * 
                    (1 + 0.05 * np.cos(18 * x_norm)) * 
                    (1 + 0.02 * np.sin(15 * x_norm)))
        
        # Final combination with chaotic scaling factor
        return 3.0 * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)