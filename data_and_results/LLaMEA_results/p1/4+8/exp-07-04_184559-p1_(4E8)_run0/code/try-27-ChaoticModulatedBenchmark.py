import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Compound exponential barrier with multiple peaks
        barrier = np.sum(np.exp(-5 * np.abs(x_scaled)) * np.exp(-2 * np.abs(x_scaled - 0.5)) * np.exp(-2 * np.abs(x_scaled + 0.5)))
        
        # Multi-frequency sinusoidal modulation with chaotic phase shifts
        modulation = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) * np.sin(3 * np.pi * x_scaled))
        
        # Adaptive quadratic term with variable conditioning
        adaptive_quad = np.sum(x_scaled**2 * (1 + 0.3 * np.sin(30 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled)))
        
        # Compound chaotic component with multiple interacting sinusoids
        chaotic = 0.02 * np.sum(np.sin(np.exp(x_scaled) + np.cos(x_scaled)) * np.cos(np.exp(-x_scaled) + np.sin(x_scaled)))
        
        # Ridge structure with varying heights
        ridges = np.sum(0.1 * np.abs(x_scaled) * np.sin(25 * np.pi * x_scaled)**2)
        
        # Combine all components with different weights
        return barrier + 0.7 * modulation + adaptive_quad + chaotic + ridges