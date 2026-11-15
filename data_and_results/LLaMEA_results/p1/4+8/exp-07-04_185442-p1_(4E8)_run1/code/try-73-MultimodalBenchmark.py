import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Enhanced exponential decay with multiple decay rates
        exp_decay = np.sum(np.exp(-x_norm**2) * np.sin(2 * np.pi * x_norm)**2) + \
                    0.3 * np.sum(np.exp(-0.5 * x_norm**2) * np.cos(3 * np.pi * x_norm)**2)
        
        # Increased trigonometric couplings with higher frequencies
        trig_coupling = np.sum(np.cos(5 * np.pi * x_norm) * np.sin(9 * np.pi * x_norm)) + \
                        0.5 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm)) + \
                        0.2 * np.sum(np.cos(4 * np.pi * x_norm) * np.sin(8 * np.pi * x_norm))
        
        # Enhanced polynomial cross-terms with higher degrees
        poly_cross = np.sum((x_norm**2 + x_norm**3 + x_norm**4 + 0.5 * x_norm**5) * np.sin(4 * np.pi * x_norm))
        
        # Adaptive conditioning with more complex scaling
        condition_factor = np.sum((x_norm**2 + 0.1) * np.exp(-x_norm**2) * np.cos(2 * np.pi * x_norm))
        
        # Complex interaction term with multiple sinusoidal components
        interaction = np.sum(np.sin(np.pi * x_norm) * np.cos(2 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Add structured noise to increase ruggedness
        noise = 0.1 * np.sum(np.sin(13 * np.pi * x_norm) * np.cos(17 * np.pi * x_norm))
        
        # Combine all terms to form the final landscape
        return exp_decay + trig_coupling + poly_cross + condition_factor + interaction + noise