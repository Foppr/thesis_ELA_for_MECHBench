import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Logarithmic barrier terms creating sharp gradients near boundaries
        f2 = 0.3 * np.sum(np.log(1 + 10 * np.abs(x_norm)) * np.sin(15 * x_norm))
        
        # Polynomial oscillation with adaptive frequency
        f3 = 0.4 * np.sum(x_norm**7 * np.cos(12 * x_norm * np.exp(-0.5 * x_norm**2)))
        
        # Multi-scale sinusoidal interaction with varying amplitudes
        f4 = 0.25 * np.sum(np.sin(20 * x_norm) * np.sin(8 * x_norm) * np.cos(4 * x_norm))
        
        # Gradient-adaptive cubic terms
        f5 = 0.35 * np.sum((x_norm**3 + 0.5 * x_norm**2) * np.exp(-0.3 * x_norm**2))
        
        # Cross-dimensional coupling with exponential interaction
        f6 = 0.2 * np.sum(np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                         (x_norm[:-1]**2 * x_norm[1:] + x_norm[1:]**2 * x_norm[:-1]))
        
        # Chaotic sine-wave with time-varying frequency
        f7 = 0.3 * np.sum(np.sin(25 * x_norm * np.cos(3 * x_norm)) * 
                         np.exp(-0.4 * x_norm**2) * np.sin(10 * x_norm))
        
        # Polynomial-weighted hyperbolic tangent interactions
        f8 = 0.2 * np.sum(np.tanh(5 * x_norm) * (x_norm**4 + 0.3 * x_norm**3))
        
        # Multi-modal exponential decay with directional preference
        f9 = 0.15 * np.sum(np.exp(-2 * np.abs(x_norm)) * np.sin(18 * x_norm))
        
        # Combined result with carefully balanced weights
        result = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
        
        return result