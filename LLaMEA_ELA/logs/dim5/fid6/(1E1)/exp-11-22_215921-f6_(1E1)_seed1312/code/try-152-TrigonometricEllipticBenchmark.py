import numpy as np

class TrigonometricEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base elliptical valley term with adaptive eccentricity and dynamic scaling
        ellipse = np.sum((x_norm[:-1]**2 + 0.3 * x_norm[1:]**2) * np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Chaotic trigonometric oscillations with fractional frequencies and dynamic amplitudes
        trig_term = np.sum(np.sin(12 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                          np.exp(-0.4 * x_norm**2) * (1 + 0.5 * np.sin(5 * x_norm)))
        
        # Saddle point structure with hyperbolic tangent and cubic interactions
        saddle = np.sum(np.tanh(4 * x_norm[:-1]) * np.tanh(4 * x_norm[1:]) * 
                       (x_norm[:-1]**3 - x_norm[1:]**3))
        
        # Adaptive Gaussian peaks with elliptical contours, dynamic positioning, and chaotic modulation
        gaussian_elliptic = 1.0 * np.sum(np.exp(-4 * ((x_norm[:-1] - 0.4 * np.sin(5 * x_norm[:-1]))**2 + 
                                                      (x_norm[1:] + 0.3 * np.cos(4 * x_norm[1:]))**2)) * 
                                        (1 + 0.3 * np.cos(7 * x_norm[:-1])))
        
        # Cross-dimensional coupling with logarithmic spiral pattern and chaotic phase shifts
        spiral_coupling = 0.8 * np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                     np.sin(15 * np.pi * np.arctan2(x_norm[1:], x_norm[:-1]) + 
                                            0.5 * np.sin(3 * x_norm[:-1])))
        
        # High-frequency modulated sinusoidal component with chaotic amplitude modulation
        high_freq = 1.5 * np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * 
                               np.exp(-0.3 * x_norm**2) * (1 + 0.4 * np.sin(8 * x_norm)))
        
        # Dimension-dependent conditioning factor with exponential growth and chaotic perturbation
        condition_factor = 1.5 + 0.7 * np.log(self.dim + 1) + 0.2 * np.sin(3 * self.dim)
        
        # Combine all terms
        return condition_factor * (ellipse + trig_term + saddle + gaussian_elliptic + 
                                 spiral_coupling + high_freq)