import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # High-order polynomial with chaotic interactions
        poly_term = np.sum(x_scaled**8 - 4*x_scaled**6 + 6*x_scaled**4 - 4*x_scaled**2 + 1)
        
        # Chaotic trigonometric term with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(25 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled) * 
                          np.sin(10 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Modified exponential barrier with higher-order polynomial interaction
        exp_term = np.sum((np.exp(-2.5 * x_scaled**2) + 0.1 * x_scaled**6) * 
                         (np.sin(7 * np.pi * x_scaled)**3 + 0.8 * np.cos(11 * np.pi * x_scaled)**3))
        
        # Radial interaction term with adaptive scaling
        radial_term = np.sum((np.linalg.norm(x_scaled, axis=0) + 0.15) * 
                            np.sin(6 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Mixed harmonic and exponential coupling with enhanced complexity
        coupling_term = np.sum(np.exp(-x_scaled**2) * np.sin(10 * np.pi * x_scaled) * 
                              np.cos(6 * np.pi * x_scaled) * x_scaled**4)
        
        # Additional chaotic sine wave component with phase shift for increased complexity
        chaos_term = np.sum(np.sin(30 * np.pi * x_scaled**2 + 0.5 * np.pi) * 
                          np.cos(20 * np.pi * x_scaled**2 + 0.25 * np.pi))
        
        # Enhanced non-separability through coupled higher-order interactions
        coupled_term = np.sum((x_scaled**3 + 0.5 * x_scaled**5) * 
                             np.sin(8 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Combine all terms with optimized weights
        return 0.25 * poly_term + 0.2 * trig_term + 0.18 * exp_term + 0.12 * radial_term + 0.07 * coupling_term + 0.03 * chaos_term + 0.15 * coupled_term