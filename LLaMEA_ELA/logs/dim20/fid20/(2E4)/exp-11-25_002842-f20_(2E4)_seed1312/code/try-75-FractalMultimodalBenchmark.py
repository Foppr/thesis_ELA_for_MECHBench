import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range
        scaled_x = x * np.pi / 5.0
        
        # Base fractal component with recursive structure
        fractal = np.sum(np.sin(2 ** (np.floor(np.log2(np.abs(scaled_x)) + 1))) * 
                        np.cos(3 ** (np.floor(np.log2(np.abs(scaled_x)) + 1))))
        
        # Multi-scale sinusoidal components with varying frequencies
        multiscale = 0.5 * np.sum(np.sin(10 * scaled_x) * np.cos(15 * scaled_x) + 
                                np.sin(20 * scaled_x) * np.cos(25 * scaled_x) + 
                                np.sin(30 * scaled_x) * np.cos(35 * scaled_x))
        
        # Discontinuous gradient components using sign and step functions
        discontinuous = 0.3 * np.sum(np.sign(np.sin(scaled_x)) * np.cos(scaled_x) + 
                                   np.sign(np.cos(scaled_x)) * np.sin(scaled_x))
        
        # Chaotic logistic map component for irregular behavior
        logistic = 0.4 * np.sum(4 * np.abs(x) * (1 - np.abs(x)))
        
        # Scale-invariant complexity through power-law interactions
        power_law = 0.25 * np.sum(np.abs(x) ** 1.7 + np.abs(x) ** 2.3)
        
        # Recursive fractal pattern with nested exponential decay
        recursive = 0.35 * np.sum(np.exp(-np.abs(x)) * np.sin(5 * x) + 
                                np.exp(-np.abs(x)**2) * np.cos(3 * x))
        
        # Multi-resolution harmonic components
        resolution_harmonics = 0.4 * np.sum(np.sin(50 * scaled_x) * np.cos(60 * scaled_x) + 
                                          np.sin(70 * scaled_x) * np.cos(80 * scaled_x))
        
        # Discrete jump terms for discontinuous landscape
        jumps = 0.2 * np.sum(np.floor(np.abs(scaled_x)) * np.sin(scaled_x) + 
                           np.ceil(np.abs(scaled_x)) * np.cos(scaled_x))
        
        # Combined complex interaction term
        interaction = 0.3 * np.sum(np.sin(2 * scaled_x[:-1]) * np.cos(3 * scaled_x[1:]) * 
                                 np.sin(4 * scaled_x[:-2]) * np.cos(5 * scaled_x[2:]))
        
        # Fractal dimension scaling component
        fractal_dim = 0.2 * np.sum(np.log(1 + np.abs(x)) ** 2 + np.log(1 + np.abs(x)) ** 3)
        
        # High-order polynomial with chaotic coefficients
        chaotic_poly = 0.15 * np.sum((x**7) * np.sin(x) + (x**8) * np.cos(x))
        
        # Final composite function with varying weights
        return 0.9 * (fractal + multiscale + discontinuous + logistic + power_law + 
                     recursive + resolution_harmonics + jumps + interaction + fractal_dim + chaotic_poly)