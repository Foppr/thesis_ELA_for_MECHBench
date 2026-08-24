import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Modified polynomial term with different exponents
        poly_term = np.sum(x_scaled**6 - 3*x_scaled**4 + 2*x_scaled**2)
        
        # Altered trigonometric term with higher frequencies
        trig_term = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Exponential barrier term with modified exponent
        exp_term = np.sum(np.exp(-2*x_scaled**2) * np.sin(4 * np.pi * x_scaled)**2)
        
        # Cross-terms to increase interaction between dimensions
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(2 * np.pi * x_scaled[:-1]))
        
        # Combine all terms with modified coefficients
        return 0.4 * poly_term + 0.35 * trig_term + 0.25 * exp_term + 0.1 * cross_term