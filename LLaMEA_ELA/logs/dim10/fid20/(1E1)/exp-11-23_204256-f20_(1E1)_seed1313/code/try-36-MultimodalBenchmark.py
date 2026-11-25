import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_normalized**2)
        
        # Highly chaotic sinusoidal perturbations with varying frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(13 * np.pi * x_normalized + np.sin(5 * x_normalized)) ** 2)
        f3 = 0.25 * np.sum(np.sin(17 * np.pi * x_normalized + np.cos(7 * x_normalized)) ** 2)
        
        # Added cubic and higher-order polynomial terms with skewness
        f4 = 0.1 * np.sum(x_normalized**3)
        f5 = 0.05 * np.sum(x_normalized**5)
        f6 = 0.02 * np.sum(np.abs(x_normalized)**7)
        
        # Exponentially decaying cross-terms to create complex interactions
        cross_term = 0.0
        for i in range(self.dim - 1):
            decay_factor = np.exp(-0.1 * i)
            cross_term += decay_factor * x_normalized[i] * x_normalized[i+1]**3
        
        # Additional chaotic cosine interaction
        f7 = 0.15 * np.sum(np.cos(5 * np.pi * x_normalized + np.sin(3 * x_normalized)) ** 2)
        
        # Adaptive scaling factor based on dimensionality with exponential growth
        adaptive_scale = 1.0 + 0.2 * np.log(self.dim + 1) + 0.05 * np.log(self.dim + 1)**2
        
        return adaptive_scale * (f1 + f2 + f3 + f4 + f5 + f6 + cross_term + f7)