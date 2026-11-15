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
        
        # Introduce a new adaptive component to improve conditioning
        adaptive_term = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled) * 
                              np.exp(-0.6 * x_scaled**2) * (1 + 0.15 * np.sin(20 * np.pi * x_scaled)))
        
        # Combine all terms with optimized weights
        return 0.25 * poly_term + 0.2 * trig_term + 0.18 * exp_term + 0.16 * radial_term + 0.07 * coupling_term + 0.03 * chaos_term + 0.04 * adaptive_term