import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced sinusoidal frequency interactions
        sin_freq = np.sum(np.sin(8 * x_norm) * np.cos(6 * x_norm)) + \
                   0.8 * np.sum(np.sin(12 * x_norm) * np.cos(10 * x_norm)) + \
                   0.6 * np.sum(np.sin(15 * x_norm) * np.cos(13 * x_norm))
        
        # Increased polynomial cross-terms with higher degrees
        poly_cross = np.sum((x_norm[0] * x_norm[1])**5) + \
                     0.7 * np.sum((x_norm[0] * x_norm[2])**3) + \
                     0.5 * np.sum(x_norm**7 * np.sin(5 * np.pi * x_norm))
        
        # Modified exponential decay with adaptive conditioning
        exp_decay = np.sum(np.exp(-0.3 * x_norm**2) * np.cos(5 * np.pi * x_norm)) + \
                    0.3 * np.sum(np.exp(-0.5 * x_norm**2) * np.sin(3 * np.pi * x_norm))
        
        # Additional trigonometric couplings with structured noise
        trig_coupling = np.sum(np.sin(7 * x_norm) * np.cos(9 * x_norm)) + \
                        0.9 * np.sum(np.sin(11 * x_norm) * np.cos(13 * x_norm)) + \
                        0.4 * np.sum(np.sin(14 * x_norm) * np.cos(16 * x_norm))
        
        # Adaptive conditioning based on dimensionality with modified scaling
        conditioning = np.sum((x_norm**2) * np.exp(-0.3 * np.abs(x_norm))) + \
                       0.2 * np.sum((x_norm**3) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Add structured noise term to increase landscape complexity
        noise = 0.03 * np.random.random()
        
        # Combine all terms to create a more complex multimodal landscape
        return sin_freq + poly_cross + exp_decay + trig_coupling + conditioning + noise