import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced chaotic sine wave component with multiple frequency modulations
        chaotic_term = np.sum(np.sin(15 * np.pi * x_scaled * (1 + 0.2 * np.sin(7 * x_scaled) + 0.1 * np.sin(13 * x_scaled)))**2)
        
        # Gradient-based quadratic with adaptive conditioning and dynamic scaling
        adaptive_quad = np.sum((x_scaled**2) * (1 + 0.7 * np.sin(3 * np.pi * x_scaled) + 0.3 * np.cos(5 * np.pi * x_scaled)))
        
        # Multi-harmonic oscillations with varying amplitudes, phases, and decay rates
        harmonic_osc = np.sum(0.8 * np.cos(5 * np.pi * x_scaled) * np.exp(-0.4 * x_scaled**2) + 
                             0.5 * np.cos(10 * np.pi * x_scaled) * np.exp(-0.2 * x_scaled**2) + 
                             0.3 * np.cos(15 * np.pi * x_scaled) * np.exp(-0.1 * x_scaled**2) +
                             0.2 * np.cos(20 * np.pi * x_scaled) * np.exp(-0.05 * x_scaled**2))
        
        # Enhanced cross-dimensional coupling with non-linear interaction terms
        cross_coupling = np.sum(np.exp(-0.3 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) * 
                               np.sin(2 * np.pi * (x_scaled[:-1] + x_scaled[1:]))**3 +
                               0.5 * np.exp(-0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) * 
                               np.cos(3 * np.pi * (x_scaled[:-1] - x_scaled[1:]))**2)
        
        # Complex saddle-point attractor with multiple local minima
        saddle_attractor = np.sum(np.sin(3 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled) + 
                                 0.5 * np.sin(6 * np.pi * x_scaled) * np.cos(6 * np.pi * x_scaled))
        
        # Additional chaotic noise component to increase landscape complexity
        noise = 0.1 * np.sum(np.sin(25 * x_scaled) * np.cos(25 * x_scaled))
        
        # Combine all terms with different weights
        return 0.7 * adaptive_quad + 0.6 * chaotic_term + 0.5 * harmonic_osc + 0.4 * cross_coupling + 0.3 * saddle_attractor + 0.1 * noise