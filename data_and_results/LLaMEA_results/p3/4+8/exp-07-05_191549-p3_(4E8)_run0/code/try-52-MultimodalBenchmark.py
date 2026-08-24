import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced high-order polynomial with chaotic interactions
        poly_term = np.sum(0.5 * (x_scaled**10 - 5*x_scaled**8 + 10*x_scaled**6 - 10*x_scaled**4 + 5*x_scaled**2 - 1)**2)
        
        # Enhanced chaotic trigonometric term with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(25 * np.pi * x_scaled) * np.cos(15 * np.pi * x_scaled) * 
                          np.sin(10 * np.pi * x_scaled) * np.cos(5 * np.pi * x_scaled))
        
        # Improved exponential barrier with radial dependency and multiple peaks
        exp_term = np.sum(np.exp(-2 * x_scaled**2) * (np.sin(7 * np.pi * x_scaled)**4 + 
                                                     0.8 * np.cos(11 * np.pi * x_scaled)**4))
        
        # Enhanced radial interaction term with adaptive scaling
        radial_term = np.sum((np.linalg.norm(x_scaled, axis=0) + 0.15) * 
                            np.sin(6 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Enhanced mixed harmonic and exponential coupling
        coupling_term = np.sum(np.exp(-0.5 * x_scaled**2) * np.sin(10 * np.pi * x_scaled) * 
                              np.cos(6 * np.pi * x_scaled) * x_scaled**4)
        
        # Additional cross-term interaction for increased complexity
        cross_term = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled) * 
                           np.exp(-0.3 * x_scaled**2) * (x_scaled**2 + 0.5))
        
        # Combine all terms with optimized weights
        return 0.3 * poly_term + 0.25 * trig_term + 0.2 * exp_term + 0.15 * radial_term + 0.08 * coupling_term + 0.02 * cross_term