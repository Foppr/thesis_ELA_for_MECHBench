import numpy as np

class ExponentialValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hyperbolic tangent chaotic coupling with fractional exponents
        f1 = np.sum(np.tanh(x_norm**2.3) * np.sin(np.pi * x_norm**1.8) * 
                   np.cos(1.7 * np.pi * x_norm**2.1))
        
        # Fractional Brownian motion inspired cross-dimensional interactions
        f2 = np.sum(np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   (np.tanh(x_norm[:-1]) * np.tanh(x_norm[1:]) + 0.5 * (x_norm[:-1]**2.5 - x_norm[1:]**2.5)) * 
                   np.exp(-0.4 * np.abs(x_norm[:-1] - x_norm[1:])**1.8))
        
        # Hyperbolic secant modulated polynomial terms with dynamic scaling
        f3 = np.sum(np.sech(0.8 * x_norm) * (x_norm**3.2 + 0.6 * x_norm**2.7) * 
                   np.sin(4.5 * x_norm) * np.cos(3.2 * x_norm))
        
        # Multi-scale chaotic oscillations with fractional power nonlinearities
        f4 = np.sum(np.abs(x_norm)**1.9 * np.tanh(2.8 * x_norm) * np.exp(-0.15 * x_norm**2.4))
        
        # Higher-order hyperbolic coupling with dynamic conditioning
        f5 = np.sum((np.cosh(x_norm[:-1]**3.0) + np.cosh(x_norm[1:]**3.0)) * 
                   np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                   np.sin(1.5 * (x_norm[:-1] - x_norm[1:])**3))
        
        # Dynamic conditioning based on dimensionality with hyperbolic functions
        condition_factor = 1.2 + 0.4 * np.log(self.dim + 1) + 0.15 * np.tanh(self.dim * 0.8)
        
        # Combined chaotic landscape with enhanced multi-modal structure
        result = (f1 + 0.7 * f2 + 0.5 * f3 + 0.8 * f4 + 0.6 * f5) * condition_factor
        
        # Add hyperbolic chaotic noise for increased complexity
        noise = 0.003 * np.random.random() * np.tanh(self.dim * 0.7)
        
        return result + noise