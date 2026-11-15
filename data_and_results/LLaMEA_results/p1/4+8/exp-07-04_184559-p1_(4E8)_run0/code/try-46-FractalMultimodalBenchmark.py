import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Logarithmic barrier terms to create irregular landscapes
        barrier = np.sum(np.log(1.0 + 10.0 * x_scaled**2))
        
        # Polynomial oscillation component with varying degrees
        oscillation = np.sum((x_scaled**3 - 0.5 * x_scaled**2 + 0.1 * x_scaled)**4)
        
        # Fractal-like interaction term using sine of exponential functions
        fractal = np.sum(np.sin(np.exp(np.abs(x_scaled)) * np.pi))
        
        # Combine all components to form the final landscape
        return quadratic + 5.0 * barrier + 2.0 * oscillation + 3.0 * fractal