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
        f2 = 1.5 * np.sum(np.cos(30 * np.pi * x_norm))
        
        # Additional quartic term with modified coefficient
        f3 = 0.2 * np.sum(x_norm**4)
        
        # Cross-term interaction to increase conditioning
        f4 = 0.5 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Additional quadratic interaction term
        f5 = 0.3 * np.sum((x_norm[:-1] - x_norm[1:])**2)
        
        # Fifth power term for added complexity
        f6 = 0.08 * np.sum(np.abs(x_norm)**5)
        
        # Additional sine term for increased multimodality
        f7 = 0.6 * np.sum(np.sin(25 * np.pi * x_norm))
        
        # Sixth power term for enhanced curvature
        f8 = 0.05 * np.sum(x_norm**6)
        
        # Additional cosine term with different frequency for more structure
        f9 = 0.25 * np.sum(np.cos(15 * np.pi * x_norm))
        
        # Modified quadratic interaction with higher weight
        f10 = 0.3 * np.sum((x_norm[:-2] - x_norm[2:])**2)
        
        # Additional higher-order interaction term
        f11 = 0.12 * np.sum((x_norm[:-3] - x_norm[3:])**2)
        
        # Increased penalty for large values
        f12 = 0.06 * np.sum(np.abs(x_norm)**7)
        
        # New Gaussian-like penalty term with modified decay rate and amplitude
        f13 = 0.12 * np.sum(np.exp(-2.5 * x_norm**2))
        
        # Chaotic interaction term using sine and cosine combinations
        f14 = 0.2 * np.sum(np.sin(35 * np.pi * x_norm) * np.cos(18 * np.pi * x_norm))
        
        # High-frequency oscillation component
        f15 = 0.1 * np.sum(np.sin(60 * x_norm))
        
        # Exponential decay with modified base
        f16 = 0.07 * np.sum(np.exp(-3.5 * np.abs(x_norm)))
        
        # Cubic interaction term
        f17 = 0.09 * np.sum(x_norm**3)
        
        # Mixed power and trigonometric term
        f18 = 0.06 * np.sum(np.sin(12 * x_norm**2))
        
        # Additional complex interaction term for better conditioning
        f19 = 0.04 * np.sum(np.sin(8 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Additional penalty term with higher nonlinearity
        f20 = 0.03 * np.sum(np.exp(-1.5 * x_norm**4))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20