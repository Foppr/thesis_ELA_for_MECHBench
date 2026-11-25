import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced logarithmic barrier terms with variable steepness and adaptive scaling
        barrier = np.sum(np.log(1.0 + 0.3 * np.abs(x_scaled) + 0.1 * x_scaled**2))
        
        # Complex trigonometric couplings with dynamic frequencies, phase shifts, and multi-dimensional modulation
        freq_factor = 2.5 + 0.4 * np.sqrt(self.dim)
        phase_shift = 0.3 * np.sin(0.15 * self.dim)
        trig_coupling = np.sum(np.sin(freq_factor * x_scaled + phase_shift) * 
                              np.cos(freq_factor * x_scaled**2 + phase_shift * 0.6) * 
                              np.tanh(0.4 * x_scaled))
        
        # Adaptive radial terms with variable exponent, multi-scale influence, and cross-term interactions
        radial_base = x_scaled**2 + 0.03
        radial = (np.sum(radial_base**(-2.5)) * 0.6 + 
                  np.sum(radial_base**(-1.8)) * 0.4 +
                  np.sum(np.abs(x_scaled)**(1.3)) * 0.3)
        
        # Coupled exponential and polynomial interactions with phase modulation and dynamic scaling
        exp_poly = np.sum(np.exp(-x_scaled**2) * (1.0 + x_scaled**3 + 0.15 * np.sin(4 * x_scaled)) * 
                         np.cos(0.4 * x_scaled**2))
        
        # Multi-scale chaotic modulation with varying amplitude, frequency, and non-linear feedback
        chaotic = np.sum(np.sin(12 * np.sin(x_scaled)) * np.cos(10 * np.cos(x_scaled)) * 
                         np.tanh(1.8 * x_scaled) * (1.0 + 0.25 * np.sin(2.5 * x_scaled)) * 
                         np.log(1.0 + 0.08 * np.abs(x_scaled)))
        
        # Additional high-frequency oscillatory component with multi-dimensional coupling
        high_freq = np.sum(np.sin(30 * x_scaled) * np.cos(25 * x_scaled**3) * 
                          np.exp(-0.08 * np.abs(x_scaled)))
        
        # Cross-dimensional interaction terms to increase conditioning and create complex curvature
        cross_dim = np.sum((x_scaled[:-1] - x_scaled[1:])**2 * np.sin(8 * x_scaled[:-1]) * 
                          np.cos(6 * x_scaled[1:]))
        
        # Novel hybrid term combining hyperbolic and polynomial components with dynamic phase modulation
        hybrid = np.sum(np.tanh(x_scaled**3) * np.sin(6 * x_scaled) * np.log(1.0 + 0.15 * x_scaled**2))
        
        # High-dimensional coupling with non-linear interaction weights
        coupling_weight = 0.7 + 0.15 * np.sin(0.4 * self.dim)
        coupling = coupling_weight * np.sum(np.sin(x_scaled) * np.cos(x_scaled**3) * 
                                          np.exp(-0.4 * x_scaled**2))
        
        # Combined function with diverse curvature, multiple local minima, and enhanced conditioning
        return 3.5 * barrier + 1.3 * trig_coupling + 0.6 * radial + 0.5 * exp_poly + 0.4 * chaotic + 0.25 * high_freq + 0.15 * cross_dim + 0.35 * hybrid + 0.25 * coupling