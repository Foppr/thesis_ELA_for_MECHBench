import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Chaotic exponential decay terms with varying rates
        exp_decay = np.sum(np.exp(-np.abs(x_normalized)) * np.sin(3 * np.pi * x_normalized)**2)
        
        # Trigonometric oscillations with multiple frequencies and amplitudes
        trig_osc = np.sum(1.2 * np.sin(5 * x_normalized) * np.cos(4 * x_normalized) + 
                          0.8 * np.sin(9 * x_normalized) * np.cos(2 * x_normalized))
        
        # Asymmetric saddle points with different curvature in positive and negative directions
        saddle = np.sum(np.where(x_normalized >= 0, 
                                0.5 * x_normalized**4 - 0.3 * x_normalized**2,
                                0.7 * x_normalized**4 - 0.4 * x_normalized**2))
        
        # Cross-terms creating complex interactions between dimensions
        cross_term = 0.3 * np.sum((x_normalized[:-1] + x_normalized[1:])**2 * 
                                 (1 + 0.1 * np.abs(x_normalized[:-1] - x_normalized[1:])))
        
        # Non-separable higher-order polynomial interactions
        poly_interaction = 0.2 * np.sum(x_normalized**3 * np.sin(x_normalized) + 
                                       x_normalized**5 * np.cos(x_normalized))
        
        # Combine all terms with adjusted weights for balanced contribution
        return exp_decay + trig_osc + saddle + cross_term + poly_interaction