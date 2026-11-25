import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range
        scaled_x = x * np.pi / 5.0
        
        # Polynomial valley component with varying degrees
        polynomial_valley = np.sum(0.1 * x**6 + 0.2 * x**4 + 0.3 * x**2)
        
        # Chaotic interaction terms with exponential decay
        chaotic_interaction = np.sum(np.exp(-0.5 * np.abs(x[:-1])) * np.sin(10 * scaled_x[1:]) * 
                                   np.exp(-0.3 * np.abs(x[1:])) * np.cos(12 * scaled_x[:-1]))
        
        # Multi-scale sinusoidal patterns with varying amplitudes
        multi_scale_sin = np.sum(0.5 * np.sin(8 * scaled_x) + 0.3 * np.cos(15 * scaled_x) + 
                               0.4 * np.sin(20 * scaled_x) + 0.2 * np.cos(25 * scaled_x))
        
        # Exponential noise component with chaotic frequency modulation
        exp_noise = np.sum(0.1 * np.exp(-np.abs(x)) * np.sin(30 * scaled_x + np.sin(5 * x)))
        
        # Cross-dimensional coupling with power-law interactions
        cross_coupling = np.sum((x[:-1]**2.5) * (x[1:]**1.5) + (x[:-1]**1.5) * (x[1:]**2.5))
        
        # Fractal-like structure using recursive polynomial terms
        fractal_poly = np.sum(0.05 * x**8 + 0.03 * x**7 + 0.02 * x**6)
        
        # High-frequency oscillation with amplitude modulation
        high_freq_osc = np.sum(0.3 * np.sin(50 * scaled_x) * (1 + 0.2 * np.sin(10 * x)))
        
        # Saddle point regions with mixed quadratic and quartic terms
        saddle_regions = np.sum(0.1 * x**4 - 0.2 * x**2)
        
        # Logarithmic curvature adjustment
        log_curvature = np.sum(0.05 * np.log(1 + np.abs(x)) * np.sin(3 * scaled_x))
        
        # Additional chaotic cross-term with non-linear coupling
        additional_chaos = np.sum(np.sin(7 * scaled_x[:-2]) * np.cos(9 * scaled_x[1:-1]) * 
                                 np.sin(11 * scaled_x[2:]) + 
                                 np.cos(8 * scaled_x[:-2]) * np.sin(10 * scaled_x[1:-1]) * 
                                 np.cos(12 * scaled_x[2:]))
        
        # Combined fitness function with weighted components
        return (polynomial_valley + chaotic_interaction + multi_scale_sin + exp_noise + 
                cross_coupling + fractal_poly + high_freq_osc + saddle_regions + 
                log_curvature + additional_chaos)