import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for global attraction
        quadratic = np.sum(x_scaled**2)
        
        # Periodic trigonometric components with varying frequencies
        trigonometric = np.sum(np.sin(10 * x_scaled) + np.cos(15 * x_scaled) + np.sin(20 * x_scaled))
        
        # Cross-dimensional coupling with sine modulation
        coupling = np.sum(np.sin(5 * x_scaled[:-1] * x_scaled[1:]) * (x_scaled[:-1]**2 + x_scaled[1:]**2))
        
        # High-order polynomial terms for increased ruggedness
        polynomial = np.sum(0.5 * x_scaled**6 - 0.3 * x_scaled**5 + 0.1 * x_scaled**4)
        
        # Saddle point structure with cubic and quartic terms
        saddle = np.sum(x_scaled**3 - 1.5 * x_scaled**2 + 0.8 * x_scaled**4)
        
        # Exponential barrier terms to prevent boundary escape
        barriers = np.sum(np.exp(-2.0 * x_scaled**2) * (np.sin(3 * x_scaled)**2 + np.cos(4 * x_scaled)**2))
        
        # Additional chaotic modulation using a sinusoidal function
        chaotic = np.sum(np.sin(7 * np.pi * x_scaled) * np.cos(9 * np.pi * x_scaled))
        
        # Combine all components with adjusted weights
        return 0.4 * quadratic + 1.8 * trigonometric + 0.3 * coupling + 0.2 * polynomial + 0.1 * saddle + 0.25 * barriers + 0.15 * chaotic