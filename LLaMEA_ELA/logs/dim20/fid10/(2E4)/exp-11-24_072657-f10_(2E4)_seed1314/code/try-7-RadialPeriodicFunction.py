import numpy as np

class RadialPeriodicFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        normalized_x = x / 5.0
        
        # Radial basis function component with multiple centers
        rb_centers = np.array([[i * 0.5 - 1.0, j * 0.5 - 1.0] for i in range(4) for j in range(4)])
        if self.dim >= 2:
            rb_sum = 0.0
            for center in rb_centers:
                distance = np.sum((normalized_x[:2] - center)**2)
                rb_sum += np.exp(-5 * distance) * np.sin(3 * distance)
        
        # Periodic component with varying frequencies
        periodic_term = np.sum(np.sin(2 * np.pi * normalized_x) * np.cos(4 * np.pi * normalized_x))
        
        # Additional harmonic terms for increased complexity
        harmonic_term = 0.5 * np.sum(np.sin(6 * np.pi * normalized_x) + np.cos(8 * np.pi * normalized_x))
        
        # Combine all terms with appropriate weights
        result = periodic_term + harmonic_term
        
        # Add quadratic penalty to encourage convergence to origin
        penalty = 0.1 * np.sum(x**2)
        
        # Add small random perturbation for robustness testing
        noise = 0.001 * np.random.random()
        
        return result + penalty + noise