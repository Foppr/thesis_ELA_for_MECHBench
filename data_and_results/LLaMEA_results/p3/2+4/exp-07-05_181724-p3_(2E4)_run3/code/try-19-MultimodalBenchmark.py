import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Enhanced quadratic terms with variable coefficients
        quadratic = np.sum((1 + 0.5 * np.sin(2 * np.pi * x_norm)) * x_norm**2)
        
        # Nested trigonometric terms with varying frequencies and amplitudes
        sinusoidal = np.sum(np.sin(10 * np.pi * x_norm)**2 + 
                           0.7 * np.sin(15 * np.pi * x_norm)**2 + 
                           0.3 * np.sin(20 * np.pi * x_norm)**2)
        
        # High-order polynomial terms with non-uniform exponents
        polynomial = np.sum(x_norm**6 + 0.4 * x_norm**8 + 0.1 * x_norm**10)
        
        # Product of all dimensions with nonlinear transformation
        product = np.prod(np.sin(np.pi * x_norm))
        
        # Chaotic interaction terms using nested trigonometric functions
        interaction = np.sum(np.sin(5 * np.pi * np.sin(3 * np.pi * x_norm)) + 
                            0.5 * np.sin(7 * np.pi * np.cos(4 * np.pi * x_norm)) + 
                            0.3 * np.sin(9 * np.pi * np.tan(2 * np.pi * x_norm)))
        
        # Cross-terms with exponential decay and chaotic coupling
        cross_terms = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * 
                            np.sin(8 * np.pi * x_norm[:-1])**2 * 
                            np.cos(6 * np.pi * x_norm[1:])**2)
        
        # Additional chaotic and fractal-like components
        fractal = np.sum(np.sin(np.pi * x_norm) * np.cos(np.pi * x_norm) * 
                        np.sin(2 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Add a small chaotic noise term
        noise = 0.03 * np.random.random()
        
        # Combine all terms with carefully adjusted weights
        return 0.3 * quadratic + 0.25 * sinusoidal + 0.2 * polynomial + 0.1 * product + 0.1 * interaction + 0.05 * cross_terms + 0.05 * fractal + noise