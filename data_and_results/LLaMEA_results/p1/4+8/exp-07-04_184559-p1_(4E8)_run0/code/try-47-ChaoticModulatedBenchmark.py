import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Enhanced sinusoidal modulation with multiple frequencies
        f2 = np.sum(np.sin(np.pi * x_norm) * np.sin(2 * np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Enhanced exponential barrier terms with higher order polynomial
        barriers = np.exp(-0.2 * np.sum(np.abs(x_norm)**4))
        
        # Chaotic component with cross-term interactions
        chaotic = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * 
                        np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Cross-term interaction to increase conditioning difficulty
        cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Combine all components with adjusted weights
        return f1 + 1.5 * f2 + 0.7 * barriers + 0.4 * chaotic + 0.2 * cross_term