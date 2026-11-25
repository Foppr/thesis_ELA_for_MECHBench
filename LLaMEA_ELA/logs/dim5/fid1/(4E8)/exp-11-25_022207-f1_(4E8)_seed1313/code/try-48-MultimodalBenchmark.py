import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic component using coupled logistic maps
        logistic_term = np.sum(4 * x_norm * (1 - x_norm) + 0.1 * np.sin(7 * x_norm))
        
        # Multi-frequency trigonometric oscillations with amplitude modulation
        trig_term = np.sum(np.cos(2 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm) * 
                          (1 + 0.3 * np.cos(3 * np.pi * x_norm)))
        
        # Adaptive polynomial saddle points with variable exponents
        saddle_term = np.sum(x_norm**4 * np.exp(-0.3 * x_norm**2) + 0.5 * x_norm**2 * np.sin(4 * x_norm))
        
        # Cross-dimensional interaction with dynamic weights based on position
        cross_term = 0.15 * np.sum(np.abs(x_norm[:-1] - x_norm[1:])**(1.7 + 0.3 * np.sin(x_norm[:-1])))
        
        # Add a global scaling factor and noise term to increase complexity
        return logistic_term + trig_term + saddle_term + cross_term + 0.05 * np.random.rand()