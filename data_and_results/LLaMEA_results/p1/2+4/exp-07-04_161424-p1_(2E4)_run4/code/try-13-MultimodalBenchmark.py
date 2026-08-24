import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base term with conditioning
        quadratic = np.sum(x_norm**2 * (1 + 0.5 * np.sin(5 * x_norm)))
        
        # Chaotic sinusoidal terms with varying frequencies and amplitudes
        sinusoidal = np.sum(np.exp(3 * np.abs(x_norm)) * np.sin(20 * np.pi * x_norm)**3 + 
                           np.cos(15 * np.pi * x_norm)**2 * np.sin(8 * np.pi * x_norm))
        
        # Polynomial interaction terms with non-integer exponents
        polynomial = np.sum((x_norm**3.5 + 0.3 * x_norm**2.7 + 0.05 * x_norm**1.8) * 
                           np.cos(5 * np.pi * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Cross-dimensional interaction with chaotic decay
        cross_term = np.exp(-np.sum(np.abs(x_norm)**1.5)) * np.prod(np.sin(3 * np.pi * x_norm)**2 + 
                                                                   np.cos(2 * np.pi * x_norm)**2)
        
        # Perturbation with chaotic behavior
        perturbation = 0.02 * np.sum(np.sin(25 * x_norm)**5 + np.cos(12 * x_norm)**3)
        
        # Add a complex global minimum structure
        global_structure = 0.1 * np.sum(np.sin(7 * x_norm) * np.cos(4 * x_norm) * np.exp(-0.1 * x_norm**2))
        
        # Combine all terms with varying weights
        return 1.5 * quadratic + 0.8 * sinusoidal + 0.3 * polynomial + 0.1 * cross_term + 0.05 * perturbation + global_structure