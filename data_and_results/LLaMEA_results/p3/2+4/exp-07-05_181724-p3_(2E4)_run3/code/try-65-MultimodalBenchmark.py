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
        sinusoidal1 = np.sum(np.sin(3 * np.pi * x_norm)**2)
        sinusoidal2 = np.sum(np.sin(7 * np.pi * x_norm)**2)
        sinusoidal3 = np.sum(np.sin(13 * np.pi * x_norm)**2)
        sinusoidal4 = np.sum(np.sin(29 * np.pi * x_norm)**2)
        
        # Higher-order polynomial terms with mixed exponents
        polynomial = np.sum(0.5 * x_norm**6 + 0.4 * x_norm**5 + 0.3 * x_norm**4 + 0.2 * x_norm**3)
        
        # Enhanced interaction terms between dimensions with quartic coupling
        interaction = np.sum(x_norm[:-1]**3 * x_norm[1:]**3)
        
        # Mixed trigonometric and polynomial term with chaotic modulation
        chaotic = np.sum(np.sin(np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * x_norm**3)
        
        # Exponential decay term with multiple scales
        exponential = np.sum(np.exp(-x_norm**2) + np.exp(-0.3 * x_norm**2) - 2.0)
        
        # Multiple radial basis functions with different widths
        rbf1 = np.sum(np.exp(-2.0 * x_norm**2))
        rbf2 = np.sum(np.exp(-5.0 * x_norm**2))
        rbf3 = np.sum(np.exp(-9.0 * x_norm**2))
        
        # Quaternion-inspired rotational component for non-separability
        rot_component = 0.0
        if self.dim > 1:
            for i in range(0, self.dim - 1, 2):
                if i + 1 < self.dim:
                    rot_component += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(10 * x_norm[i] * x_norm[i+1])
        
        # Add a small random perturbation for non-triviality
        noise = 0.003 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return (0.25 * quadratic + 
                0.2 * sinusoidal1 + 
                0.18 * sinusoidal2 + 
                0.15 * sinusoidal3 + 
                0.12 * sinusoidal4 + 
                0.2 * polynomial + 
                0.1 * interaction + 
                0.1 * chaotic + 
                0.15 * exponential + 
                0.08 * rbf1 + 
                0.06 * rbf2 + 
                0.04 * rbf3 + 
                0.05 * rot_component + 
                noise)