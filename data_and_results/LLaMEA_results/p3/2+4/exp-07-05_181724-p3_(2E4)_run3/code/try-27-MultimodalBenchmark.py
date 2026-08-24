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
        
        # Chaotic multi-frequency sinusoidal terms with irregular amplitudes
        sinusoidal1 = np.sum(np.sin(2 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        sinusoidal2 = np.sum(np.sin(7 * np.pi * x_norm) * np.sin(11 * np.pi * x_norm))
        sinusoidal3 = np.sum(np.sin(13 * np.pi * x_norm) * np.sin(17 * np.pi * x_norm))
        
        # Higher-order polynomial terms with mixed exponents
        polynomial = np.sum(0.5 * x_norm**6 + 0.4 * x_norm**5 + 0.3 * x_norm**4 + 0.2 * x_norm**3)
        
        # Interaction terms with cross-dimensional coupling
        interaction = np.sum(x_norm[:-1]**2 * x_norm[1:]**2)
        
        # Radial basis function component with multiple peaks
        rbf = np.sum(np.exp(-5.0 * (x_norm**2 + 0.5 * x_norm[:-1]**2 + 0.3 * x_norm[1:]**2)))
        
        # Mixed trigonometric and polynomial term with non-linear coupling
        mixed = np.sum(np.sin(np.pi * x_norm) * x_norm**3 * np.cos(np.pi * x_norm))
        
        # Exponential decay with variable rate to create varied curvature
        exponential = np.sum(np.exp(-x_norm**2) - 1.0 + 0.1 * np.sin(10 * x_norm))
        
        # Additional chaotic component with fractal-like behavior
        chaotic = np.sum(np.sin(20 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm) * x_norm**2)
        
        # Add a small random perturbation for non-triviality
        noise = 0.01 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.4 * quadratic + 
                0.3 * sinusoidal1 + 
                0.2 * sinusoidal2 + 
                0.1 * sinusoidal3 + 
                0.2 * polynomial + 
                0.1 * interaction + 
                0.15 * rbf + 
                0.05 * mixed + 
                0.1 * exponential + 
                0.05 * chaotic + 
                noise)