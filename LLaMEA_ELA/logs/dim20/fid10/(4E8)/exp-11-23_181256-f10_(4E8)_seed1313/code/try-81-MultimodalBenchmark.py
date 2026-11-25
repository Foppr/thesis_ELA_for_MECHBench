import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logarithmic barrier terms creating sharp gradients near boundaries
        barrier = np.sum(np.log(1.0 + 10.0 * x_scaled**2))
        
        # Complex trigonometric couplings with varying frequencies and amplitudes
        trig_coupling = np.sum(np.sin(7 * x_scaled) * np.cos(5 * x_scaled) * 
                              np.sin(3 * x_scaled**2) * np.cos(2 * x_scaled**3))
        
        # Adaptive radial terms that change behavior based on distance from origin
        radial_adaptive = np.sum((1.0 + 0.5 * np.sin(4 * np.sqrt(np.sum(x_scaled**2)))) * 
                                np.exp(-0.2 * np.sum(x_scaled**2)))
        
        # Polynomial interaction with mixed powers and cross-terms
        poly_interaction = np.sum(x_scaled**6 + 0.8 * x_scaled[:-3]**2 * x_scaled[3:] + 
                                0.6 * x_scaled[:-2] * x_scaled[2:] + 0.4 * x_scaled[:-1]**3 * x_scaled[1:])
        
        # Saddle-point interactions with enhanced curvature variations
        saddle = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(2 * np.pi * x_scaled) * 
                       np.exp(-0.5 * np.sum(x_scaled**2)))
        
        # High-frequency oscillation component with amplitude modulation
        high_freq = np.sum(np.sin(20 * x_scaled) * np.cos(18 * x_scaled) * 
                          (1 + 0.3 * np.sin(10 * x_scaled)) * np.exp(-0.1 * np.abs(x_scaled)))
        
        # Combined function with diverse landscape characteristics
        return 1.5 * barrier + 1.2 * trig_coupling + 0.8 * radial_adaptive + 0.6 * poly_interaction + 0.4 * saddle + 0.3 * high_freq + np.sum(x_scaled**4)