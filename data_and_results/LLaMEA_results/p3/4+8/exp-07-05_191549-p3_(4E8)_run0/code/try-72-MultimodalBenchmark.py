import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced high-order polynomial with chaotic interactions
        poly_term = np.sum(0.5 * (x_scaled**12 - 6*x_scaled**10 + 15*x_scaled**8 - 20*x_scaled**6 + 15*x_scaled**4 - 6*x_scaled**2 + 1)**2)
        
        # Enhanced chaotic trigonometric term with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(30 * np.pi * x_scaled) * np.cos(20 * np.pi * x_scaled) * 
                          np.sin(15 * np.pi * x_scaled) * np.cos(10 * np.pi * x_scaled))
        
        # Improved exponential barrier with radial dependency and multiple peaks
        exp_term = np.sum(np.exp(-1.5 * x_scaled**2) * (np.sin(8 * np.pi * x_scaled)**4 + 
                                                     0.9 * np.cos(13 * np.pi * x_scaled)**4))
        
        # Enhanced radial interaction term with adaptive scaling
        radial_term = np.sum((np.linalg.norm(x_scaled, axis=0) + 0.2) * 
                            np.sin(7 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Enhanced mixed harmonic and exponential coupling
        coupling_term = np.sum(np.exp(-0.3 * x_scaled**2) * np.sin(12 * np.pi * x_scaled) * 
                              np.cos(8 * np.pi * x_scaled) * x_scaled**5)
        
        # Additional cross-term interaction for increased complexity
        cross_term = np.sum(np.sin(4 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) * 
                           np.exp(-0.2 * x_scaled**2) * (x_scaled**3 + 0.6))
        
        # Combine all terms with optimized weights
        return 0.35 * poly_term + 0.2 * trig_term + 0.25 * exp_term + 0.1 * radial_term + 0.07 * coupling_term + 0.03 * cross_term