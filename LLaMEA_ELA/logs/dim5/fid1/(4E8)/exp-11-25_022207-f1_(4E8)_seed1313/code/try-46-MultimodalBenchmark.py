import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Chaotic exponential decay terms with varying rates
        exp_decay = np.sum(np.exp(-0.5 * np.abs(x_normalized)) * np.sin(4 * np.pi * x_normalized)**2)
        
        # Trigonometric oscillations with multiple frequencies and amplitudes
        trig_osc = np.sum(1.5 * np.sin(6 * x_normalized) * np.cos(3 * x_normalized) + 
                          0.9 * np.sin(10 * x_normalized) * np.cos(2.5 * x_normalized))
        
        # Asymmetric saddle points with different curvature in positive and negative directions
        saddle = np.sum(np.where(x_normalized >= 0, 
                                0.6 * x_normalized**4 - 0.25 * x_normalized**2,
                                0.8 * x_normalized**4 - 0.35 * x_normalized**2))
        
        # Cross-terms creating complex interactions between dimensions
        cross_term = 0.4 * np.sum((x_normalized[:-1] + x_normalized[1:])**2 * 
                                 (1 + 0.15 * np.abs(x_normalized[:-1] - x_normalized[1:])))
        
        # Non-separable higher-order polynomial interactions
        poly_interaction = 0.25 * np.sum(x_normalized**3 * np.sin(x_normalized) + 
                                       x_normalized**5 * np.cos(x_normalized))
        
        # Add a small noise term to increase landscape irregularity
        noise = 0.01 * np.sum(np.random.randn(self.dim) * x_normalized**2)
        
        # Combine all terms with adjusted weights for balanced contribution
        return exp_decay + trig_osc + saddle + cross_term + poly_interaction + noise