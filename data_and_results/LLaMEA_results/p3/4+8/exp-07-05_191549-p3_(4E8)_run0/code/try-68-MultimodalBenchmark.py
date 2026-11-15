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
        trig_term = np.sum(np.sin(27 * np.pi * x_scaled) * np.cos(16 * np.pi * x_scaled) * 
                          np.sin(11 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled))
        
        # Exponential barrier with radial dependency and multiple peaks
        exp_term = np.sum(np.exp(-2.7 * x_scaled**2) * (np.sin(7.5 * np.pi * x_scaled)**3 + 
                                                     0.85 * np.cos(11.5 * np.pi * x_scaled)**3))
        
        # Radial interaction term with adaptive scaling
        radial_term = np.sum((np.linalg.norm(x_scaled, axis=0) + 0.16) * 
                            np.sin(6.5 * np.pi * x_scaled) * np.cos(4.5 * np.pi * x_scaled))
        
        # Mixed harmonic and exponential coupling
        coupling_term = np.sum(np.exp(-0.85 * x_scaled**2) * np.sin(10.5 * np.pi * x_scaled) * 
                              np.cos(6.5 * np.pi * x_scaled) * x_scaled**3)
        
        # Additional chaotic modulation for enhanced complexity
        chaos_mod = np.sum(np.sin(31 * np.pi * x_scaled**2) * np.cos(21 * np.pi * x_scaled**2))
        
        # Combine all terms with optimized weights
        return 0.32 * poly_term + 0.36 * trig_term + 0.14 * exp_term + 0.11 * radial_term + 0.07 * coupling_term + 0.02 * chaos_mod