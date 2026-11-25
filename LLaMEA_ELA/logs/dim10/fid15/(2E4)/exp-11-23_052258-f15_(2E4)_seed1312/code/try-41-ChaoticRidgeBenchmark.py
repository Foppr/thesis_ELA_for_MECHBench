import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map component with dynamic coupling
        f1 = 0.3 * np.sum(np.log(1 + np.abs(np.sin(3.2 * x) * np.cos(2.7 * x))) * np.exp(-0.5 * x**2))
        
        # Spherical harmonic interaction terms for multidirectional complexity
        f2 = 0.25 * np.sum((x[:-1]**2 + x[1:]**2)**1.8 * np.sin(3.0 * np.arctan2(x[1:], x[:-1])))
        
        # Fractional polynomial ridge with variable exponent and noise
        f3 = 0.35 * np.sum(np.abs(x[:-1] - x[1:])**(1.3 + 0.2 * np.sin(5.0 * x[:-1])) + 
                          0.1 * np.cos(10.0 * (x[:-1]**2 + x[1:]**2)))
        
        # High-frequency chaotic sine-wave modulation with radial basis influence
        f4 = 0.2 * np.sum(np.sin(20.0 * x + np.exp(-0.3 * x**2)) * 
                         np.exp(-0.4 * (x - np.mean(x))**2))
        
        # Asymmetric multimodal perturbation with cubic and quintic terms
        f5 = 0.15 * np.sum((x**5 - 2.5 * x**3 + 1.8 * x) * np.sin(4.0 * x) * np.cos(2.0 * x))
        
        # Combined chaotic landscape with adaptive weights
        return f1 + f2 + f3 + f4 + f5