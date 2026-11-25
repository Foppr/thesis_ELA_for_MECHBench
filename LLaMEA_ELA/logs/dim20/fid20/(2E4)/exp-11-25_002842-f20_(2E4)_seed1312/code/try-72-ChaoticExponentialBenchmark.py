import numpy as np

class ChaoticExponentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range
        scaled_x = x * np.pi / 5.0
        
        # Exponential decay base component with varying rates
        exp_decay = np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(scaled_x) + 
                          np.exp(-0.3 * np.abs(x)) * np.cos(scaled_x))
        
        # Multi-scale trigonometric wave interactions
        waves = 0.5 * np.sum(np.sin(2 * scaled_x) * np.cos(3 * scaled_x) + 
                           np.sin(4 * scaled_x) * np.cos(5 * scaled_x) + 
                           np.sin(6 * scaled_x) * np.cos(7 * scaled_x))
        
        # Fractal-like nested structure with recursive exponential terms
        fractal = 0.3 * np.sum(np.exp(-0.1 * np.abs(x[:-1])) * np.exp(-0.1 * np.abs(x[1:])) * 
                              np.sin(10 * scaled_x[:-1]) * np.cos(10 * scaled_x[1:]))
        
        # Cross-dimensional coupling with exponential interactions
        cross_coupling = 0.25 * np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * 
                                     np.sin(8 * scaled_x[:-1]) * np.cos(8 * scaled_x[1:]))
        
        # Multi-scale sinusoidal components with varying amplitudes
        multi_freq = 0.4 * np.sum(np.sin(15 * scaled_x) + np.cos(12 * scaled_x) + 
                                np.sin(18 * scaled_x) + np.cos(16 * scaled_x))
        
        # Chaotic interaction through non-linear polynomial combinations
        chaotic_poly = 0.35 * np.sum((x[:-1] ** 3) * np.sin(scaled_x[1:]) + 
                                   (x[1:] ** 3) * np.cos(scaled_x[:-1]))
        
        # High-frequency oscillation with amplitude modulation
        high_freq_osc = 0.2 * np.sum(np.sin(25 * scaled_x) * np.cos(20 * scaled_x) * 
                                   np.exp(-0.05 * np.abs(x)))
        
        # Logarithmic curvature adjustment for varied landscape steepness
        log_curvature = 0.15 * np.sum(np.log(1 + np.abs(x)) * (np.sin(scaled_x) ** 2))
        
        # Multi-dimensional exponential interaction with varying coupling strengths
        exp_interaction = 0.3 * np.sum(np.exp(-0.1 * np.abs(x[:-2])) * 
                                    np.exp(-0.1 * np.abs(x[1:-1])) * 
                                    np.exp(-0.1 * np.abs(x[2:])) * 
                                    np.sin(15 * scaled_x[:-2]) * np.cos(15 * scaled_x[2:]))
        
        # Quadratic basin with exponential modulation
        quadratic_modulated = 0.2 * np.sum((x**2) * (1 + 0.1 * np.exp(-0.05 * np.abs(x))))
        
        # Nested chaotic structure with recursive pattern
        nested_chaos = 0.25 * np.sum(np.sin(30 * scaled_x) * np.cos(28 * scaled_x) * 
                                   np.exp(-0.03 * np.abs(x)) + 
                                   np.sin(32 * scaled_x) * np.cos(34 * scaled_x) * 
                                   np.exp(-0.04 * np.abs(x)))
        
        # Fractional dimensionality interaction
        fractional_interaction = 0.18 * np.sum(np.sin(5 * scaled_x[:-1]) * np.cos(6 * scaled_x[1:]) * 
                                            (1 + 0.05 * np.abs(x[:-1] - x[1:])))
        
        # Final combined landscape with adjusted weights
        return 1.2 * (exp_decay + waves + fractal + cross_coupling + multi_freq + 
                     chaotic_poly + high_freq_osc + log_curvature + exp_interaction + 
                     quadratic_modulated + nested_chaos + fractional_interaction)