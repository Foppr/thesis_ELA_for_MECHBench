import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global quadratic term for convergence
        f1 = np.sum(x**2)
        
        # Chaotic trigonometric component with varying frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(10.0 * np.sin(3.0 * x)) * np.cos(7.0 * np.cos(2.0 * x)))
        
        # Radial basis function with adaptive scaling based on distance from origin
        f3 = 0.3 * np.sum(np.exp(-0.5 * np.sum(x**2)) * np.sin(5.0 * np.sum(x**2)))
        
        # Asymmetric polynomial coupling with mixed powers
        f4 = 0.25 * np.sum(x**3 * np.sin(4.0 * x) + x**5 * np.cos(3.0 * x))
        
        # Multi-scale sinusoidal modulation with dynamic frequency adjustment
        f5 = 0.2 * np.sum(np.sin(15.0 * x) * np.cos(12.0 * x) * np.sin(9.0 * x))
        
        # Adaptive conditioning through exponential decay and polynomial interaction
        f6 = 0.15 * np.sum(np.exp(-0.1 * np.sum(x**2)) * x**4 * np.sin(6.0 * x))
        
        # Cross-dimension coupling with chaotic sine-wave interactions
        f7 = 0.1 * np.sum(np.sin(8.0 * x) * np.cos(5.0 * x) * np.sin(3.0 * x))
        
        # Novel asymmetric Gaussian interaction term for enhanced multimodality
        f8 = 0.12 * np.sum(np.exp(-0.3 * np.sum((x - 0.5)**2)) * np.sin(10.0 * x) * np.cos(7.0 * x))
        
        # Higher-order polynomial with trigonometric modulation
        f9 = 0.08 * np.sum((x**7) * np.sin(2.0 * x) * np.cos(4.0 * x))
        
        # Dynamic noise modulation to increase problem difficulty
        f10 = 0.06 * np.sum(np.sin(18.0 * x) * np.cos(14.0 * x) * np.exp(-0.2 * np.sum(x**2)))
        
        # Combined term for increased nonlinearity and complexity
        f11 = 0.1 * np.sum(np.sin(20.0 * x) * np.cos(16.0 * x) * x**6)
        
        # Final interaction term with adaptive amplitude and phase
        f12 = 0.09 * np.sum(np.exp(-0.1 * np.sum(x**2)) * np.sin(13.0 * x) * np.cos(9.0 * x) * x**3)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12