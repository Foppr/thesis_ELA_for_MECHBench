import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of squares term
        f1 = np.sum(x_norm**2)
        
        # Multimodal term with increased frequency and amplitude
        f2 = 2.5 * np.sum(np.cos(40 * np.pi * x_norm))
        
        # Additional quartic term with modified coefficient
        f3 = 0.3 * np.sum(x_norm**4)
        
        # Cross-term interaction to increase conditioning
        f4 = 0.7 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Additional quadratic interaction term
        f5 = 0.4 * np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Fifth power term for added complexity
        f6 = 0.15 * np.sum(np.abs(x_norm)**5)
        
        # Additional sine term for increased multimodality
        f7 = 0.8 * np.sum(np.sin(35 * np.pi * x_norm))
        
        # Sixth power term for enhanced curvature
        f8 = 0.1 * np.sum(x_norm**6)
        
        # Additional cosine term with different frequency for more structure
        f9 = 0.35 * np.sum(np.cos(25 * np.pi * x_norm))
        
        # Modified quadratic interaction with higher weight
        f10 = 0.45 * np.sum((x_norm[:-2] - x_norm[2:])**2)
        
        # Additional higher-order interaction term
        f11 = 0.2 * np.sum((x_norm[:-3] - x_norm[3:])**2)
        
        # Increased penalty for large values
        f12 = 0.15 * np.sum(np.abs(x_norm)**7)
        
        # New Gaussian-like penalty term with modified decay rate and amplitude
        f13 = 0.2 * np.sum(np.exp(-3.0 * x_norm**2))
        
        # Chaotic interaction term using sine and cosine combinations
        f14 = 0.3 * np.sum(np.sin(45 * np.pi * x_norm) * np.cos(25 * np.pi * x_norm))
        
        # High-frequency oscillation component
        f15 = 0.2 * np.sum(np.sin(80 * x_norm))
        
        # Exponential decay with modified base
        f16 = 0.15 * np.sum(np.exp(-5.0 * np.abs(x_norm)))
        
        # Cubic interaction term
        f17 = 0.15 * np.sum(x_norm**3)
        
        # Mixed power and trigonometric term
        f18 = 0.1 * np.sum(np.sin(20 * x_norm**2))
        
        # Additional chaotic sine-cosine interaction
        f19 = 0.2 * np.sum(np.sin(30 * np.pi * x_norm) * np.cos(40 * np.pi * x_norm))
        
        # Additional exponential term with negative base
        f20 = 0.12 * np.sum(np.exp(-2.0 * x_norm**2))
        
        # Increased penalty for extreme values
        f21 = 0.1 * np.sum(np.abs(x_norm)**8)
        
        # Enhanced cubic term with different coefficient
        f22 = 0.15 * np.sum(x_norm**5)
        
        # Additional high-frequency cosine term
        f23 = 0.25 * np.sum(np.cos(50 * np.pi * x_norm))
        
        # Complex interaction with 4-dimensional jumps
        f24 = 0.15 * np.sum((x_norm[:-4] - x_norm[4:])**2)
        
        # Additional chaotic sine-cosine interaction with different frequencies
        f25 = 0.18 * np.sum(np.sin(35 * np.pi * x_norm) * np.cos(45 * np.pi * x_norm))
        
        # Additional exponential term with modified base
        f26 = 0.08 * np.sum(np.exp(-1.0 * x_norm**2))
        
        # Increased penalty for very large values
        f27 = 0.05 * np.sum(np.abs(x_norm)**9)
        
        # Additional high-order power term
        f28 = 0.06 * np.sum(x_norm**8)
        
        # Additional chaotic sine term with different frequency
        f29 = 0.1 * np.sum(np.sin(50 * x_norm))
        
        # Additional interaction term with 5-dimensional jumps
        f30 = 0.1 * np.sum((x_norm[:-5] - x_norm[5:])**2)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20 + f21 + f22 + f23 + f24 + f25 + f26 + f27 + f28 + f29 + f30