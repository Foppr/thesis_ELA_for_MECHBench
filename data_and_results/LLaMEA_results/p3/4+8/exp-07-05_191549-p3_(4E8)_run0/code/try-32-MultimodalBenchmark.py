import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial basis component with chaotic modulation
        r = np.sqrt(np.sum(x_scaled**2, axis=0, keepdims=True))
        radial_term = np.sum(np.exp(-5 * r) * np.sin(10 * np.pi * r) * np.cos(5 * np.pi * r))
        
        # Chaotic sine wave component with multiple frequencies and amplitudes
        chaotic_term = np.sum(np.sin(20 * np.pi * x_scaled + np.sin(5 * np.pi * x_scaled)) * 
                             np.cos(15 * np.pi * x_scaled + np.cos(7 * np.pi * x_scaled)) * 
                             np.sin(8 * np.pi * x_scaled))
        
        # Adaptive conditioning based on dimensionality
        cond_term = np.sum((x_scaled**2 + 0.1 * np.sin(30 * np.pi * x_scaled))**3)
        
        # Interaction between dimensions with exponential decay
        interaction_term = np.sum(np.exp(-0.5 * np.sum((x_scaled[:, np.newaxis] - x_scaled[np.newaxis, :])**2, axis=0)) * 
                                np.sin(4 * np.pi * x_scaled))
        
        # Combine all terms with optimized weights
        return 0.3 * radial_term + 0.4 * chaotic_term + 0.2 * cond_term + 0.1 * interaction_term