import numpy as np

class MultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial landscape with varying degrees and coefficients
        poly_term = np.sum(0.5 * x_scaled**4 + 0.3 * x_scaled**3 - 0.2 * x_scaled**2 + 0.1 * x_scaled)
        
        # Trigonometric components with multiple frequencies and amplitudes
        trig_term = np.sum(0.8 * np.sin(8.0 * x_scaled) + 0.6 * np.cos(6.0 * x_scaled) + 
                          0.4 * np.sin(12.0 * x_scaled**2) + 0.3 * np.cos(10.0 * x_scaled**2))
        
        # Exponential decay with sinusoidal modulation
        exp_term = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * (1.0 + 0.5 * np.sin(5.0 * x_scaled)))
        
        # Cross-dimensional interaction with asymmetric coupling
        cross_dim = np.sum((x_scaled[:-1]**2 * x_scaled[1:]**3 + 
                           x_scaled[1:]**2 * x_scaled[:-1]**3) * 
                          np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2))
        
        # Asymmetric peaks with varying heights and widths
        peak_term = np.sum(0.7 * np.exp(-3.0 * (x_scaled - 0.5)**2) + 
                          0.4 * np.exp(-5.0 * (x_scaled + 0.3)**2) + 
                          0.3 * np.exp(-2.0 * (x_scaled - 0.8)**2))
        
        # Combined function with weighted components
        return 0.25 * poly_term + 0.3 * trig_term + 0.15 * exp_term + 0.2 * cross_dim + 0.1 * peak_term + 1.5