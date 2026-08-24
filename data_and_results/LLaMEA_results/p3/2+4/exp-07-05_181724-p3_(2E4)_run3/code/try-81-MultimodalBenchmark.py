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
        
        # Multi-frequency sinusoidal terms with varying amplitudes and phases
        sinusoidal1 = np.sum(np.sin(5 * np.pi * x_norm)**3)
        sinusoidal2 = np.sum(np.sin(11 * np.pi * x_norm)**3)
        sinusoidal3 = np.sum(np.sin(23 * np.pi * x_norm)**3)
        sinusoidal4 = np.sum(np.sin(47 * np.pi * x_norm)**3)
        
        # Higher-order polynomial terms with mixed exponents
        polynomial = np.sum(0.6 * x_norm**5 + 0.5 * x_norm**4 + 0.4 * x_norm**3 + 0.3 * x_norm**2)
        
        # Enhanced interaction terms between dimensions with cubic coupling
        interaction = np.sum(x_norm[:-1]**4 * x_norm[1:]**2)
        
        # Mixed trigonometric and polynomial term with chaotic modulation
        chaotic = np.sum(np.sin(np.pi * x_norm) * np.cos(2 * np.pi * x_norm) * x_norm**4)
        
        # Exponential decay term with multiple scales
        exponential = np.sum(np.exp(-x_norm**2) + np.exp(-0.5 * x_norm**2) - 2.0)
        
        # Multiple radial basis functions with different widths
        rbf1 = np.sum(np.exp(-3.0 * x_norm**2))
        rbf2 = np.sum(np.exp(-7.0 * x_norm**2))
        rbf3 = np.sum(np.exp(-11.0 * x_norm**2))
        
        # Chaotic component using logistic map for added complexity
        chaotic_component = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic_component += np.sin(100 * x_norm[i] * x_norm[i+1])
        
        # Additional chaotic sine-wave component for increased complexity
        chaotic_sine = np.sum(np.sin(13 * np.pi * x_norm) * np.sin(17 * np.pi * x_norm))
        
        # Add a small random perturbation for non-triviality
        noise = 0.005 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.3 * quadratic + 
                0.3 * sinusoidal1 + 
                0.25 * sinusoidal2 + 
                0.2 * sinusoidal3 + 
                0.15 * sinusoidal4 + 
                0.25 * polynomial + 
                0.1 * interaction + 
                0.1 * chaotic + 
                0.15 * exponential + 
                0.08 * rbf1 + 
                0.06 * rbf2 + 
                0.04 * rbf3 + 
                0.05 * chaotic_component + 
                0.03 * chaotic_sine + 
                noise)