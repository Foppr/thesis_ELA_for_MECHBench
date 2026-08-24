import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced exponential barrier with varying strength
        barrier = np.sum(np.exp(-15 * np.abs(x_scaled)) + 0.5 * np.exp(-5 * np.abs(x_scaled)))
        
        # Multi-frequency sinusoidal modulations with varying amplitudes
        modulation = np.sum(
            0.8 * np.sin(12 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled) +
            0.3 * np.sin(8 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled)
        )
        
        # Perturbed quadratic term with chaotic modulation
        quadratic = np.sum(
            x_scaled**2 * (1 + 0.2 * np.sin(25 * np.pi * x_scaled) + 0.1 * np.cos(15 * np.pi * x_scaled))
        )
        
        # Chaotic component with enhanced non-linearity
        chaotic = 0.02 * np.sum(
            np.sin(np.exp(2 * x_scaled)) * np.cos(np.exp(-x_scaled)) +
            0.5 * np.sin(np.exp(-2 * x_scaled)) * np.cos(np.exp(x_scaled))
        )
        
        # Add a small radial bias term to increase conditioning
        radial_bias = 0.01 * np.sum(x_scaled**4)
        
        # Combine all components
        return barrier + 0.6 * modulation + quadratic + chaotic + radial_bias