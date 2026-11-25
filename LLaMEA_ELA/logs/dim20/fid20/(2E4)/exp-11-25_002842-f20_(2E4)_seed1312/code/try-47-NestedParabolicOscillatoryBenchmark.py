import numpy as np

class NestedParabolicOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] range
        scaled_x = x
        
        # Nested parabolic valleys with varying depths
        parabolic_valleys = np.sum(0.1 * (x**2) + 0.05 * (x**4) + 0.01 * (x**6))
        
        # Exponential noise component to increase landscape complexity
        exponential_noise = 0.3 * np.sum(np.exp(-0.5 * (x**2)) * np.sin(2 * x) + np.exp(-0.3 * (x**2)) * np.cos(3 * x))
        
        # Coupled oscillatory components with varying frequencies and coupling strengths
        coupled_oscillations = 0.2 * np.sum(np.sin(2 * scaled_x) * np.cos(3 * scaled_x) + 
                                           np.sin(4 * scaled_x) * np.cos(5 * scaled_x) + 
                                           np.sin(6 * scaled_x) * np.cos(7 * scaled_x))
        
        # Cross-dimensional interaction terms with polynomial coupling
        cross_terms = 0.15 * np.sum((x[:-1]**2) * (x[1:]**3) + x[:-1] * (x[1:]**4))
        
        # Chaotic sine-wave modulation with non-uniform frequency spacing
        chaotic_modulation = 0.25 * np.sum(np.sin(1.1 * scaled_x) * np.cos(1.3 * scaled_x) * 
                                          np.sin(1.7 * scaled_x) * np.cos(1.9 * scaled_x))
        
        # Asymmetric quadratic basin with offset
        asymmetric_basin = 0.1 * np.sum((x - 1.0)**2 + (x + 1.0)**2)
        
        # Higher-order polynomial terms for increased nonlinearity
        higher_order = 0.05 * np.sum(x**7 + x**8)
        
        # Logarithmic scaling of the landscape curvature
        log_curvature = 0.1 * np.sum(np.log(1 + 0.1 * np.abs(x)) * np.sin(0.5 * scaled_x))
        
        # Multi-scale oscillatory interference pattern
        multi_scale_osc = 0.18 * np.sum(np.sin(2 * scaled_x) * np.cos(4 * scaled_x) * 
                                      np.sin(6 * scaled_x) * np.cos(8 * scaled_x))
        
        return parabolic_valleys + exponential_noise + coupled_oscillations + cross_terms + chaotic_modulation + asymmetric_basin + higher_order + log_curvature + multi_scale_osc