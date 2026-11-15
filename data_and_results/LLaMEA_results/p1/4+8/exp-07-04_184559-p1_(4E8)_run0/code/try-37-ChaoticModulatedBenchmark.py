import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced exponential barrier terms with stronger conditioning
        barrier = np.sum(np.exp(-15 * np.abs(x_scaled)) + 0.5 * np.exp(-5 * np.abs(x_scaled)))
        
        # Modified sinusoidal modulation with higher frequency components
        modulation = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) + 
                           0.3 * np.sin(25 * np.pi * x_scaled))
        
        # Quadratic term with enhanced chaotic scaling factor and radial bias
        radial_bias = np.sum(x_scaled**2 * (1 + 0.2 * np.sin(30 * np.pi * x_scaled) + 0.1 * x_scaled**2))
        
        # Enhanced chaotic component with combined exponential and trigonometric terms
        chaotic = 0.02 * np.sum(np.sin(np.exp(1.5 * x_scaled)) * np.cos(np.exp(-1.2 * x_scaled)) + 
                               0.5 * np.sin(np.exp(-0.5 * x_scaled)) * np.cos(np.exp(0.8 * x_scaled)))
        
        # Combine all components
        return barrier + 0.7 * modulation + radial_bias + chaotic