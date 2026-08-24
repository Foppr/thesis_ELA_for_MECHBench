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
        sinusoidal1 = np.sum(np.sin(7 * np.pi * x_norm)**4)
        sinusoidal2 = np.sum(np.sin(13 * np.pi * x_norm)**4)
        sinusoidal3 = np.sum(np.sin(29 * np.pi * x_norm)**4)
        sinusoidal4 = np.sum(np.sin(53 * np.pi * x_norm)**4)
        
        # Higher-order polynomial terms with mixed exponents
        polynomial = np.sum(0.7 * x_norm**6 + 0.6 * x_norm**5 + 0.5 * x_norm**4 + 0.4 * x_norm**3 + 0.3 * x_norm**2)
        
        # Enhanced interaction terms between dimensions with quartic coupling
        interaction = np.sum(x_norm[:-1]**5 * x_norm[1:]**3)
        
        # Mixed trigonometric and polynomial term with chaotic modulation
        chaotic = np.sum(np.sin(np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * x_norm**5)
        
        # Exponential decay term with multiple scales
        exponential = np.sum(np.exp(-x_norm**2) + np.exp(-0.3 * x_norm**2) + np.exp(-0.7 * x_norm**2) - 3.0)
        
        # Multiple radial basis functions with different widths
        rbf1 = np.sum(np.exp(-2.0 * x_norm**2))
        rbf2 = np.sum(np.exp(-6.0 * x_norm**2))
        rbf3 = np.sum(np.exp(-10.0 * x_norm**2))
        rbf4 = np.sum(np.exp(-15.0 * x_norm**2))
        
        # Chaotic component using logistic map for added complexity
        chaotic_component = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic_component += np.sin(150 * x_norm[i] * x_norm[i+1]) + np.cos(120 * x_norm[i] * x_norm[i+1])
        
        # Add a small random perturbation for non-triviality
        noise = 0.01 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.25 * quadratic + 
                0.3 * sinusoidal1 + 
                0.25 * sinusoidal2 + 
                0.2 * sinusoidal3 + 
                0.15 * sinusoidal4 + 
                0.3 * polynomial + 
                0.15 * interaction + 
                0.1 * chaotic + 
                0.2 * exponential + 
                0.09 * rbf1 + 
                0.07 * rbf2 + 
                0.05 * rbf3 + 
                0.03 * rbf4 + 
                0.06 * chaotic_component + 
                noise)