import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        quadratic = np.sum(x_norm**2)
        
        # Multi-frequency sinusoidal terms with varying amplitudes
        sinusoidal1 = np.sum(np.sin(2 * np.pi * x_norm)**2)
        sinusoidal2 = np.sum(np.sin(5 * np.pi * x_norm)**2)
        sinusoidal3 = np.sum(np.sin(10 * np.pi * x_norm)**2)
        
        # Higher-order polynomial terms for increased complexity
        polynomial = np.sum(0.3 * x_norm**4 + 0.2 * x_norm**3 + 0.1 * x_norm**2)
        
        # Interaction terms between dimensions
        interaction = np.sum(x_norm[:-1] * x_norm[1:])
        
        # Mixed trigonometric and polynomial term
        mixed = np.sum(np.sin(np.pi * x_norm) * x_norm**2)
        
        # Exponential decay term to create varied landscape curvature
        exponential = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Add a small random perturbation for non-triviality
        noise = 0.01 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.5 * quadratic + 
                0.3 * sinusoidal1 + 
                0.2 * sinusoidal2 + 
                0.1 * sinusoidal3 + 
                0.15 * polynomial + 
                0.05 * interaction + 
                0.05 * mixed + 
                0.1 * exponential + 
                noise)