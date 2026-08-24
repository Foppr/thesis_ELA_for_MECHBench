import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quadratic basin term with conditioning
        f1 = 0.5 * np.sum(x**2) + 0.1 * np.sum(x**4)
        
        # Stronger multimodal term with chaotic sine-wave perturbations
        f2 = 0.3 * np.sum(np.sin(20 * x) * np.exp(-0.3 * x**2))
        
        # High-frequency oscillatory component with varying amplitude
        f3 = 0.25 * np.sum(np.sin(35 * x) * np.exp(-0.2 * x**2))
        
        # Modified cosine term with enhanced nonlinearity
        f4 = 0.2 * np.sum(np.cos(25 * x) * np.exp(-0.15 * x**2))
        
        # Cross-term interactions with nonlinear coupling
        f5 = 0.1 * np.sum(x[:-1] * x[1:] * np.sin(10 * (x[:-1] + x[1:])))
        
        # Additional polynomial cross-term interaction
        f6 = 0.15 * np.sum((x[:-1]**3) * (x[1:]**3) * np.sin(5 * (x[:-1] + x[1:])))
        
        # Logarithmic conditioning term to increase ill-conditioning
        f7 = 0.05 * np.sum(np.log(1 + 0.1 * x**2))
        
        # Chaotic perturbation term for added complexity
        f8 = 0.1 * np.sum(np.sin(50 * x) * np.cos(15 * x) * np.exp(-0.1 * x**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8