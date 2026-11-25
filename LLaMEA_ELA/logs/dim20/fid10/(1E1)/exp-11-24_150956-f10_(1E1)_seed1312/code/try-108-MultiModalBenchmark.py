import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponentially decaying sinusoidal waves with varying frequencies
        wave_terms = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * 
                           (np.sin(8.0 * x_scaled) + 0.7 * np.sin(12.0 * x_scaled) + 
                            0.3 * np.sin(20.0 * x_scaled)))
        
        # Cubic polynomial interactions with asymmetric coefficients
        poly_terms = np.sum(0.5 * x_scaled**3 + 0.3 * x_scaled**2 - 0.8 * x_scaled)
        
        # Asymmetric gradient field with directional preference
        grad_field = np.sum((x_scaled**2) * np.exp(-0.5 * x_scaled**2) * 
                           (1.0 + 0.5 * np.sin(3.0 * x_scaled)))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = np.sum(np.exp(-0.3 * np.abs(x_scaled[:-1] - x_scaled[1:])) * 
                              (x_scaled[:-1]**2 + x_scaled[1:]**2))
        
        # Multi-scale harmonic interference with phase shifts
        harmonic_terms = np.sum(0.6 * np.sin(6.0 * x_scaled) * np.cos(9.0 * x_scaled) + 
                              0.4 * np.sin(15.0 * x_scaled**2) * np.cos(18.0 * x_scaled**2) + 
                              0.2 * np.sin(25.0 * x_scaled**3) * np.cos(30.0 * x_scaled**3))
        
        # Asymmetric landscape with weighted sum of components
        return 0.4 * wave_terms + 0.25 * poly_terms + 0.2 * grad_field + 0.1 * cross_coupling + 0.05 * harmonic_terms + 2.1