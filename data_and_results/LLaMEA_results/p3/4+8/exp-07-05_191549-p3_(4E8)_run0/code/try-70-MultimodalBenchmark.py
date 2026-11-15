import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced high-order polynomial with chaotic interactions and additional peaks
        poly_term = np.sum(0.7 * (x_scaled**12 - 6*x_scaled**10 + 15*x_scaled**8 - 20*x_scaled**6 + 15*x_scaled**4 - 6*x_scaled**2 + 1)**2)
        
        # Increased chaotic trigonometric term with higher frequencies and amplitude modulation
        trig_term = np.sum(np.sin(35 * np.pi * x_scaled) * np.cos(25 * np.pi * x_scaled) * 
                          np.sin(20 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled) * 
                          np.exp(-0.5 * x_scaled**2))
        
        # Novel exponential barrier with radial dependency and multiple sharp peaks
        exp_term = np.sum(np.exp(-3 * x_scaled**2) * (np.sin(9 * np.pi * x_scaled)**5 + 
                                                     0.9 * np.cos(13 * np.pi * x_scaled)**5 + 
                                                     0.7 * np.sin(17 * np.pi * x_scaled)**3))
        
        # Enhanced radial interaction term with adaptive scaling and additional harmonic components
        radial_term = np.sum((np.linalg.norm(x_scaled, axis=0) + 0.2) * 
                            np.sin(8 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled) * 
                            np.exp(-0.3 * x_scaled**2))
        
        # Modified mixed harmonic and exponential coupling with increased complexity
        coupling_term = np.sum(np.exp(-0.7 * x_scaled**2) * np.sin(12 * np.pi * x_scaled) * 
                              np.cos(8 * np.pi * x_scaled) * x_scaled**6)
        
        # New cross-term interaction with higher frequency oscillations and non-linear coupling
        cross_term = np.sum(np.sin(5 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) * 
                           np.exp(-0.4 * x_scaled**2) * (x_scaled**3 + 0.6 * x_scaled))
        
        # Combine all terms with optimized weights for increased multimodality and conditioning
        return 0.35 * poly_term + 0.3 * trig_term + 0.25 * exp_term + 0.1 * radial_term + 0.05 * coupling_term + 0.05 * cross_term