import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential decay term with chaotic modulation
        exp_term = np.sum(np.exp(-np.abs(x_scaled)) * np.cos(2 * np.pi * x_scaled))
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(5 * np.pi * x_scaled) * np.sin(3 * np.pi * x_scaled**2))
        
        # Saddle-point structure using hyperbolic tangent
        tanh_term = np.sum(np.tanh(x_scaled)**2 - 0.5 * x_scaled**2)
        
        # Chaotic component with recursive scaling
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10 * x_scaled[i] + np.cos(7 * x_scaled[i]))
        
        # Combine all components with adaptive weights
        return 0.3 * exp_term + 0.4 * sin_term + 0.2 * tanh_term + 0.1 * chaotic + 0.05 * np.sum(x_scaled**4)