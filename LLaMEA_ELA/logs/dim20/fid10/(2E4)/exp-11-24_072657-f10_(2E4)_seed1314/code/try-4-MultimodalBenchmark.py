import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial terms with different degrees
        poly_term = np.sum(x_scaled**4) + 0.5 * np.sum(x_scaled**3) + 0.1 * np.sum(x_scaled**2)
        
        # Trigonometric components creating periodic structure
        trig_term = np.sum(np.sin(3 * np.pi * x_scaled)**2) + np.sum(np.cos(2 * np.pi * x_scaled)**2)
        
        # Radial basis function component
        radial_term = np.sum(np.exp(-np.sum(x_scaled**2, axis=0, keepdims=True)) * 
                            np.cos(2 * np.pi * np.sum(x_scaled**2, axis=0, keepdims=True)))
        
        # Cross-term interaction
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:]) if self.dim > 1 else 0
        
        # Add small random perturbation for additional challenge
        noise = 0.05 * np.random.random()
        
        return 0.8 * poly_term + 0.6 * trig_term + 0.4 * radial_term + 0.2 * cross_term + noise