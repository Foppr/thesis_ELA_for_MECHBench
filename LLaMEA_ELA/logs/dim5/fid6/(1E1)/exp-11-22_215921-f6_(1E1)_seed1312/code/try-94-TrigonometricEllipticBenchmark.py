import numpy as np

class TrigonometricEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base elliptical valley term with adaptive eccentricity and dynamic scaling
        ellipse = np.sum((x_norm[:-1]**2 + 0.3 * x_norm[1:]**2) * np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Chaotic trigonometric oscillations with varying frequencies and amplitudes
        trig_term = np.sum(np.sin(12 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                          np.exp(-0.4 * x_norm**2))
        
        # Saddle point structure with hyperbolic tangent interactions and dynamic positioning
        saddle = np.sum(np.tanh(4 * x_norm[:-1]) * np.tanh(4 * x_norm[1:]) * 
                       (x_norm[:-1]**2 - x_norm[1:]**2) * np.exp(-0.1 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Adaptive Gaussian peaks with elliptical contours and dynamic positioning
        gaussian_elliptic = 1.0 * np.sum(np.exp(-4 * ((x_norm[:-1] - 0.4 * np.sin(5 * x_norm[:-1]))**2 + 
                                                      (x_norm[1:] + 0.3 * np.cos(4 * x_norm[1:]))**2)))
        
        # Cross-dimensional coupling with logarithmic spiral pattern and chaotic modulation
        spiral_coupling = 0.7 * np.sum(np.exp(-0.6 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                     np.sin(15 * np.pi * np.arctan2(x_norm[1:], x_norm[:-1])) * 
                                     np.cos(3 * np.pi * x_norm[:-1]))
        
        # High-frequency modulated sinusoidal component with chaotic behavior
        high_freq = 1.5 * np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * 
                               np.exp(-0.3 * x_norm**2))
        
        # Low-frequency chaotic modulation for increased complexity
        chaos_mod = 0.8 * np.sum(np.sin(7 * np.pi * np.abs(x_norm)) * 
                               np.cos(5 * np.pi * np.abs(x_norm)) * 
                               np.exp(-0.2 * x_norm**2))
        
        # Dimension-dependent conditioning factor with exponential growth and chaotic scaling
        condition_factor = 1.2 + 0.8 * np.log(self.dim + 1) + 0.3 * np.sin(0.5 * self.dim)
        
        # Combine all terms
        return condition_factor * (ellipse + trig_term + saddle + gaussian_elliptic + 
                                 spiral_coupling + high_freq + chaos_mod)