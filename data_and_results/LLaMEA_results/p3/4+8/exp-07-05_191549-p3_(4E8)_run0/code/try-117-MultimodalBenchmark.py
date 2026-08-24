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
        
        # Exponential barrier with radial dependency and multiple peaks
        exp_term = np.sum(np.exp(-2.5 * x_scaled**2) * (np.sin(7 * np.pi * x_scaled)**3 + 
                                                     0.8 * np.cos(11 * np.pi * x_scaled)**3))
        
        # Radial interaction term with adaptive scaling
        radial_term = np.sum((np.linalg.norm(x_scaled, axis=0) + 0.15) * 
                            np.sin(6 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Mixed harmonic and exponential coupling
        coupling_term = np.sum(np.exp(-0.8 * x_scaled**2) * np.sin(10 * np.pi * x_scaled) * 
                              np.cos(6 * np.pi * x_scaled) * x_scaled**3)
        
        # Additional chaotic modulation for enhanced complexity
        chaos_mod = np.sum(np.sin(30 * np.pi * x_scaled**2) * np.cos(20 * np.pi * x_scaled**2))
        
        # Introduce asymmetric distortion to improve conditioning
        asymmetry = np.sum(np.abs(x_scaled)**1.5 * np.sin(8 * np.pi * x_scaled))
        
        # Combine all terms with optimized weights
        return 0.25 * poly_term + 0.3 * trig_term + 0.15 * exp_term + 0.12 * radial_term + 0.08 * coupling_term + 0.03 * chaos_mod + 0.07 * asymmetry