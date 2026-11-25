import numpy as np

class TrigonometricEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base elliptical valley term with adaptive eccentricity and dynamic scaling
        ellipse = np.sum((x_norm[:-1]**2 + 0.3 * x_norm[1:]**2) * 
                        np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                        (1 + 0.2 * np.sin(5 * x_norm[:-1]) * np.cos(4 * x_norm[1:])))
        
        # Chaotic trigonometric oscillations with exponential frequency modulation
        trig_term = np.sum(np.sin(10 * np.pi * x_norm * np.exp(-0.1 * x_norm**2)) * 
                          np.cos(7 * np.pi * x_norm * np.exp(-0.15 * x_norm**2)) * 
                          np.exp(-0.4 * x_norm**2))
        
        # Saddle point structure with hyperbolic tangent and cubic interactions
        saddle = np.sum(np.tanh(2 * x_norm[:-1]) * np.tanh(2 * x_norm[1:]) * 
                       (x_norm[:-1]**3 - x_norm[1:]**3) * 
                       np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Adaptive Gaussian peaks with chaotic positioning and elliptical contours
        gaussian_elliptic = 1.0 * np.sum(np.exp(-4 * ((x_norm[:-1] - 0.4 * np.sin(6 * x_norm[:-1]))**2 + 
                                                      (x_norm[1:] + 0.3 * np.cos(5 * x_norm[1:]))**2)) * 
                                        np.exp(-0.2 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Cross-dimensional coupling with fractal-like logarithmic spiral pattern
        spiral_coupling = 0.7 * np.sum(np.exp(-0.4 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                     np.sin(15 * np.pi * np.arctan2(x_norm[1:], x_norm[:-1]) * 
                                            np.exp(-0.1 * (x_norm[:-1]**2 + x_norm[1:]**2))))
        
        # High-frequency modulated sinusoidal component with chaotic amplitude
        high_freq = 1.5 * np.sum(np.sin(25 * x_norm * np.exp(-0.05 * x_norm**2)) * 
                               np.cos(20 * x_norm * np.exp(-0.08 * x_norm**2)) * 
                               np.exp(-0.3 * x_norm**2))
        
        # Dimension-dependent conditioning factor with exponential growth and chaotic modulation
        condition_factor = 1.5 + 0.8 * np.log(self.dim + 1) * np.sin(0.5 * self.dim)
        
        # Combine all terms with added chaotic noise term
        noise_term = 0.2 * np.sum(np.random.uniform(-1, 1, self.dim - 1) * 
                                np.sin(30 * x_norm[:-1]) * np.cos(25 * x_norm[1:]))
        
        return condition_factor * (ellipse + trig_term + saddle + gaussian_elliptic + 
                                 spiral_coupling + high_freq + noise_term)