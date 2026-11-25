import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range for sinusoidal components
        scaled_x = x * (np.pi / 5.0)
        
        # Main sinusoidal term with multiple peaks and valleys
        main_term = np.sum(np.sin(scaled_x) * np.cos(2 * scaled_x))
        
        # Additional quadratic penalty term to encourage convergence to origin
        penalty_term = 0.1 * np.sum(x**2)
        
        # Add a small noise component to make it more challenging
        noise = 0.01 * np.random.random()
        
        return main_term + penalty_term + noise