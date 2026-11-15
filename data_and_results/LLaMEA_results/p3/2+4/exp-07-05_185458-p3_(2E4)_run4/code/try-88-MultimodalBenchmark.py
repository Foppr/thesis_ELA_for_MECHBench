import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine wave with dynamic frequency modulation based on position
        f2 = np.sum(np.sin(20 * np.pi * x_norm * (1 + 0.5 * np.sin(5 * x_norm))) ** 2)
        
        # Asymmetric polynomial with varying exponents and cross-dimensional interactions
        f3 = np.sum(0.5 * x_norm**3 + 0.3 * x_norm**5 + 0.2 * x_norm**7 + 0.1 * x_norm**9)
        
        # Saddle point inducing term with trigonometric coupling
        f4 = np.sum(np.cos(10 * x_norm) * np.sin(10 * x_norm) * (x_norm[:-1] * x_norm[1:]))
        
        # Dynamic modulation with exponential decay and position-dependent scaling
        f5 = np.sum(np.exp(-0.5 * x_norm**2) * np.sin(15 * x_norm)**2)
        
        # Cross-dimensional coupling with variable interaction strength
        f6 = np.sum((x_norm[:-1] + x_norm[1:]) ** 2 * np.cos(x_norm[:-1] * x_norm[1:]))
        
        # Additional chaotic term with higher-order polynomial interaction
        f7 = np.sum(np.sin(25 * x_norm + np.sin(10 * x_norm)) ** 4)
        
        # Modified gradient-based term with non-uniform curvature
        f8 = np.sum((x_norm**2 + 0.5 * x_norm**4) * np.cos(5 * x_norm))
        
        # Final combination with dynamic weights
        return f1 + 0.8 * f2 + 0.4 * f3 + 0.3 * f4 + 0.25 * f5 + 0.35 * f6 + 0.2 * f7 + 0.15 * f8