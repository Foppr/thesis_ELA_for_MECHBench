import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with different frequencies
        sinusoidal = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        
        # Add a more complex trigonometric term to increase multimodality
        complex_trig = np.sum(np.sin(10 * np.pi * x_norm) ** 4)
        
        # Add polynomial interaction terms for increased landscape complexity
        polynomial = 0.1 * np.sum(x_norm**4)
        
        # Combine all terms to create a more challenging multimodal landscape
        return quadratic + 0.5 * sinusoidal + 0.3 * complex_trig + polynomial