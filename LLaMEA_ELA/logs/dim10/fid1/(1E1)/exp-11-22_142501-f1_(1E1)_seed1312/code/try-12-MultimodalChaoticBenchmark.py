import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sinusoidal oscillation component with varying frequencies
        sin_term = np.sum(np.sin(5 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Adaptive polynomial distortion with dimension-dependent exponents
        poly_exponent = 2 + (self.dim / 10.0)
        poly_term = np.sum(x_scaled**poly_exponent - 2 * x_scaled**2 + 0.5 * x_scaled)
        
        # Ridge structure with Gaussian peaks
        ridge_term = np.sum(np.exp(-0.5 * (x_scaled**2)) * np.cos(2 * np.pi * x_scaled))
        
        # Saddle point structure with hyperbolic tangent components
        saddle_term = np.sum(np.tanh(x_scaled) * np.sin(0.5 * x_scaled))
        
        # Variable conditioning through dimension-dependent scaling
        condition_term = np.sum((1 + 0.1 * self.dim) * x_scaled**4 - 0.5 * x_scaled**2)
        
        # High-frequency noise component with amplitude modulation
        noise_term = np.sum(0.3 * np.sin(20 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled))
        
        # Combine all terms with adaptive weights based on dimension
        weight1 = 0.25
        weight2 = 0.2
        weight3 = 0.15
        weight4 = 0.15
        weight5 = 0.1
        weight6 = 0.15
        
        return (weight1 * sin_term + 
                weight2 * poly_term + 
                weight3 * ridge_term + 
                weight4 * saddle_term + 
                weight5 * condition_term + 
                weight6 * noise_term + 
                2.0)