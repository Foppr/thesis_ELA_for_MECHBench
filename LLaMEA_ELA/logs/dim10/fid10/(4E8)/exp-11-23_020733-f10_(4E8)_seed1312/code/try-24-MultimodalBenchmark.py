import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Higher-order polynomial term with mixed degrees
        poly_term = np.sum(0.7 * x_scaled**6 + 0.5 * x_scaled**5 + 0.3 * x_scaled**4 + 0.1 * x_scaled**3)
        
        # Multiple trigonometric components with different frequencies and amplitudes
        trig_term = np.sum(
            2.0 * np.sin(5 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) +
            1.5 * np.sin(7 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled) +
            0.8 * np.sin(9 * np.pi * x_scaled)
        )
        
        # Complex exponential barrier with multiple peaks
        exp_barrier = np.sum(
            np.exp(-x_scaled**2 / 0.3) * (1 - np.exp(-x_scaled**2 / 0.1)) +
            0.5 * np.exp(-x_scaled**2 / 0.7) * (1 - np.exp(-x_scaled**2 / 0.4))
        )
        
        # Enhanced cross-dimensional coupling with sine interaction
        cross_term = np.sum(
            x_scaled[:-1] * x_scaled[1:] * np.sin(np.pi * (x_scaled[:-1] + x_scaled[1:])) +
            0.5 * x_scaled[:-2] * x_scaled[1:-1] * x_scaled[2:] * np.cos(2 * np.pi * x_scaled[:-2])
        )
        
        # Additional harmonic terms for increased complexity
        harmonic_term = np.sum(
            0.3 * np.sin(10 * np.pi * x_scaled) +
            0.2 * np.cos(8 * np.pi * x_scaled) +
            0.1 * np.sin(15 * np.pi * x_scaled)
        )
        
        # Combine all terms with adjusted weights
        return (
            1.0 * poly_term + 
            0.8 * trig_term + 
            0.6 * exp_barrier + 
            0.3 * cross_term + 
            0.2 * harmonic_term
        )