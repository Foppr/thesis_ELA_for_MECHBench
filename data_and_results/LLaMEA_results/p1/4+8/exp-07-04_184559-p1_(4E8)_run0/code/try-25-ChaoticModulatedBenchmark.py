import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced exponential barrier terms with varying exponents
        barrier = np.sum(np.exp(-15 * np.abs(x_scaled)) + 0.5 * np.exp(-5 * np.abs(x_scaled)))
        
        # Multi-frequency sinusoidal modulation
        modulation = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) + 
                           0.3 * np.sin(25 * np.pi * x_scaled) * np.cos(12 * np.pi * x_scaled))
        
        # Perturbed quadratic term with chaotic scaling factor
        quadratic = np.sum(x_scaled**2 * (1 + 0.2 * np.sin(30 * np.pi * x_scaled) + 
                                         0.1 * np.cos(15 * np.pi * x_scaled)))
        
        # Enhanced chaotic component with combined trigonometric functions
        chaotic = 0.02 * np.sum(np.sin(np.exp(2 * x_scaled)) * np.cos(np.exp(-x_scaled)) + 
                               0.5 * np.sin(np.exp(-x_scaled)) * np.cos(np.exp(x_scaled)))
        
        # Add a small cubic term to increase landscape complexity
        cubic = 0.005 * np.sum(x_scaled**3 * np.sin(10 * np.pi * x_scaled))
        
        # Combine all components
        return barrier + 0.6 * modulation + quadratic + chaotic + cubic