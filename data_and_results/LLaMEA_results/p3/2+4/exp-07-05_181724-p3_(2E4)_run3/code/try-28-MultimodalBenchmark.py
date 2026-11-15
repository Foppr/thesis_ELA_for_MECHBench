import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term with slight modification
        quadratic = np.sum(x_norm**2 * (1.0 + 0.1 * np.sin(5 * x_norm)))
        
        # Enhanced chaotic multi-frequency sinusoidal terms with varying amplitudes
        sinusoidal1 = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * (1.0 + 0.2 * np.sin(7 * x_norm)))
        sinusoidal2 = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(11 * np.pi * x_norm) * (1.0 + 0.15 * np.cos(13 * x_norm)))
        sinusoidal3 = np.sum(np.sin(13 * np.pi * x_norm) * np.cos(17 * np.pi * x_norm) * (1.0 + 0.1 * np.sin(19 * x_norm)))
        
        # Higher-order polynomial terms with mixed exponents and interaction
        polynomial = np.sum(0.5 * x_norm**6 + 0.4 * x_norm**5 + 0.3 * x_norm**4 + 0.2 * x_norm**3 + 0.1 * x_norm**2)
        
        # Improved interaction terms with cross-dimensional coupling
        interaction = np.sum(x_norm[:-1]**3 * x_norm[1:]**3 + 0.5 * x_norm[:-1]**2 * x_norm[1:]**2)
        
        # Modified radial basis function component with multiple peaks and varying widths
        rbf = np.sum(np.exp(-3.0 * (x_norm**2 + 0.3 * x_norm[:-1]**2 + 0.2 * x_norm[1:]**2)) + 
                     0.5 * np.exp(-7.0 * (x_norm**2 + 0.4 * x_norm[:-1]**2 + 0.3 * x_norm[1:]**2)))
        
        # Enhanced mixed trigonometric and polynomial term with non-linear coupling
        mixed = np.sum(np.sin(np.pi * x_norm) * x_norm**4 * np.cos(np.pi * x_norm) * (1.0 + 0.1 * np.sin(2 * x_norm)))
        
        # Modified exponential decay with variable rate to create varied curvature
        exponential = np.sum(np.exp(-x_norm**2) - 1.0 + 0.1 * np.sin(10 * x_norm) + 0.05 * np.cos(15 * x_norm))
        
        # Enhanced chaotic component with fractal-like behavior and additional frequency
        chaotic = np.sum(np.sin(20 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm) * x_norm**3 + 
                         0.3 * np.sin(25 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm) * x_norm**2)
        
        # Additional coupling term between all dimensions
        coupling = np.sum(np.sin(np.pi * x_norm) * np.cos(np.pi * x_norm) * np.prod(x_norm, axis=0, keepdims=True))
        
        # Add a small random perturbation for non-triviality
        noise = 0.01 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.35 * quadratic + 
                0.25 * sinusoidal1 + 
                0.2 * sinusoidal2 + 
                0.15 * sinusoidal3 + 
                0.2 * polynomial + 
                0.1 * interaction + 
                0.15 * rbf + 
                0.05 * mixed + 
                0.1 * exponential + 
                0.05 * chaotic + 
                0.03 * coupling + 
                noise)