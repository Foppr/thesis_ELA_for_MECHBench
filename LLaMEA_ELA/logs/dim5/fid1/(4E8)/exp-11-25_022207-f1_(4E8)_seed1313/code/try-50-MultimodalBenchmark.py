import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced chaotic exponential decay with modified rates
        exp_decay = np.sum(np.exp(-np.abs(x_normalized) * (1 + 0.5 * np.sin(2 * np.pi * x_normalized))) * 
                          np.sin(3 * np.pi * x_normalized)**2)
        
        # Multi-scale trigonometric oscillations with varying amplitudes and frequencies
        trig_osc = np.sum(1.5 * np.sin(6 * x_normalized) * np.cos(5 * x_normalized) + 
                          1.0 * np.sin(10 * x_normalized) * np.cos(3 * x_normalized) +
                          0.5 * np.sin(15 * x_normalized) * np.cos(2 * x_normalized))
        
        # Enhanced asymmetric saddle points with fractal-like curvature variations
        saddle = np.sum(np.where(x_normalized >= 0, 
                                0.6 * x_normalized**4 - 0.4 * x_normalized**2 + 0.1 * x_normalized**6,
                                0.8 * x_normalized**4 - 0.5 * x_normalized**2 + 0.15 * x_normalized**6))
        
        # Complex cross-terms with non-linear coupling and pathologically difficult interactions
        cross_term = 0.4 * np.sum((x_normalized[:-1] + x_normalized[1:])**3 * 
                                 (1 + 0.2 * np.abs(x_normalized[:-1] - x_normalized[1:]) + 
                                  0.1 * (x_normalized[:-1] * x_normalized[1:])**2))
        
        # Higher-order polynomial interactions with fractal-like scaling
        poly_interaction = 0.3 * np.sum(x_normalized**4 * np.sin(x_normalized) + 
                                       x_normalized**6 * np.cos(x_normalized) +
                                       0.5 * x_normalized**8 * np.sin(0.5 * x_normalized))
        
        # Additional chaotic modulation to increase landscape complexity
        chaotic_mod = 0.2 * np.sum(np.sin(7 * x_normalized) * np.cos(4 * x_normalized) * 
                                  np.exp(-0.5 * x_normalized**2))
        
        # Combine all terms with adjusted weights for balanced contribution
        return exp_decay + trig_osc + saddle + cross_term + poly_interaction + chaotic_mod