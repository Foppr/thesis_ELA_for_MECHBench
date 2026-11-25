import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Nested sinusoidal components with chaotic frequency modulation
        nested_sin = np.sum(np.sin(20.0 * np.sin(15.0 * x_scaled)) * 
                           np.cos(18.0 * np.cos(13.0 * x_scaled)) + 
                           0.5 * np.sin(25.0 * np.sin(22.0 * x_scaled**2)) * 
                           np.cos(24.0 * np.cos(20.0 * x_scaled**2)))
        
        # Asymmetric saddle points with polynomial potential wells
        saddle_terms = np.sum((x_scaled**2 - 0.5 * x_scaled**4 + 0.1 * x_scaled**6) * 
                            np.exp(-0.5 * (x_scaled**2)) + 
                            0.3 * (x_scaled**3 - 0.7 * x_scaled**5) * 
                            np.exp(-0.3 * (x_scaled**2)))
        
        # Dynamic gradient field with time-like dimension coupling
        grad_field = np.sum(np.sin(10.0 * x_scaled) * np.cos(8.0 * x_scaled) * 
                           np.exp(-0.1 * np.abs(x_scaled)) + 
                           0.6 * np.sin(15.0 * x_scaled**2) * np.cos(12.0 * x_scaled**2) * 
                           np.exp(-0.2 * np.abs(x_scaled)))
        
        # Multi-scale chaotic interference with exponential decay
        chaotic_interference = np.sum(np.exp(-3.0 * np.abs(x_scaled)) * 
                                    (np.sin(7.0 * x_scaled) + 0.5 * np.cos(9.0 * x_scaled)) + 
                                    0.4 * np.exp(-2.0 * np.abs(x_scaled**2)) * 
                                    (np.sin(11.0 * x_scaled**2) + 0.3 * np.cos(13.0 * x_scaled**2)))
        
        # Cross-dimensional coupling with asymmetric interaction coefficients
        cross_dim = np.sum((x_scaled[:-1]**2 + 0.5 * x_scaled[1:]**2) * 
                          np.sin(5.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                          0.7 * (x_scaled[:-2]**3 - 0.3 * x_scaled[2:]**3) * 
                          np.cos(4.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Asymmetric landscape with weighted component blending
        return 0.4 * nested_sin + 0.3 * saddle_terms + 0.15 * grad_field + 0.1 * chaotic_interference + 0.05 * cross_dim + 2.1