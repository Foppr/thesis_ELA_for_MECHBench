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
        f2 = 0.8 * np.sum(np.cos(17 * np.pi * x_norm))
        
        # Additional quartic term with modified coefficient
        f3 = 0.09 * np.sum(x_norm**4)
        
        # Cross-term interaction to increase conditioning
        f4 = 0.28 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Additional quadratic interaction term
        f5 = 0.17 * np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Fifth power term for added complexity
        f6 = 0.045 * np.sum(np.abs(x_norm)**5)
        
        # Additional sine term for increased multimodality
        f7 = 0.35 * np.sum(np.sin(14 * np.pi * x_norm))
        
        # Sixth power term for enhanced curvature
        f8 = 0.025 * np.sum(x_norm**6)
        
        # Additional cosine term with different frequency for more structure
        f9 = 0.14 * np.sum(np.cos(9 * np.pi * x_norm))
        
        # Modified quadratic interaction with higher weight
        f10 = 0.18 * np.sum((x_norm[:-2] - x_norm[2:])**2)
        
        # Additional higher-order interaction term
        f11 = 0.06 * np.sum((x_norm[:-3] - x_norm[3:])**2)
        
        # Increased penalty for large values
        f12 = 0.035 * np.sum(np.abs(x_norm)**7)
        
        # New Gaussian-like penalty term to increase conditioning
        f13 = 0.05 * np.sum(np.exp(-2.0 * x_norm**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13