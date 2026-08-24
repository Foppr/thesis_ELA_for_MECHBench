import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # High-order polynomial with chaotic interactions
        poly_term = np.sum(x_scaled**10 - 5*x_scaled**8 + 10*x_scaled**6 - 10*x_scaled**4 + 5*x_scaled**2 - 1)
        
        # Chaotic trigonometric term with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(30 * np.pi * x_scaled) * np.cos(20 * np.pi * x_scaled) * 
                          np.sin(15 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled))
        
        # Exponential barrier with radial dependency and multiple peaks
        exp_term = np.sum(np.exp(-5 * x_scaled**2) * (np.sin(8 * np.pi * x_scaled)**4 + 
                                                     0.9 * np.cos(13 * np.pi * x_scaled)**4))
        
        # Radial interaction term with adaptive scaling
        radial_term = np.sum((np.linalg.norm(x_scaled, axis=0) + 0.2) * 
                            np.sin(7 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Mixed harmonic and exponential coupling
        coupling_term = np.sum(np.exp(-x_scaled**2) * np.sin(12 * np.pi * x_scaled) * 
                              np.cos(8 * np.pi * x_scaled) * x_scaled**5)
        
        # Additional chaotic sine wave for increased complexity
        chaos_term = np.sum(np.sin(35 * np.pi * x_scaled**2) * np.cos(25 * np.pi * x_scaled**2))
        
        # Combine all terms with optimized weights
        return 0.35 * poly_term + 0.3 * trig_term + 0.25 * exp_term + 0.1 * radial_term + 0.05 * coupling_term + 0.05 * chaos_term