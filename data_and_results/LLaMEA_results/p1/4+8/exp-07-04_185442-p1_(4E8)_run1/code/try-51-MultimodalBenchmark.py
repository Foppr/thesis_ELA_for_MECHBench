import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Logistic map chaotic component
        chaotic = 0.0
        r = 3.9
        for i in range(10):
            chaotic += np.sum(np.sin(r * x_norm * (1 - x_norm)) ** 2)
        
        # Radial basis function components with varying centers and widths
        rbfs = 0.0
        centers = np.linspace(-1, 1, 5)
        widths = np.logspace(-2, 0, 5)
        for i, (c, w) in enumerate(zip(centers, widths)):
            rbfs += np.sum(np.exp(-w * (x_norm - c) ** 2))
        
        # Asymmetric polynomial distortions
        poly_distort = np.sum((x_norm ** 3) * (1 + 0.3 * np.sin(3 * np.pi * x_norm))) + \
                       0.5 * np.sum(np.abs(x_norm) ** 1.7 * np.cos(2 * np.pi * x_norm))
        
        # Cross-dimensional interaction with sine modulation
        cross_interaction = 0.3 * np.sum(np.sin(4 * np.pi * x_norm) * 
                                        np.cos(3 * np.pi * x_norm) * 
                                        np.sin(5 * np.pi * x_norm))
        
        # Add a global scaling term with noise
        scaling_term = 0.2 * np.sum(np.abs(x_norm) ** 2.5)
        noise = 0.01 * np.random.random()
        
        # Combine all components
        return chaotic + rbfs + poly_distort + cross_interaction + scaling_term + noise