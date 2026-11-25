import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced logarithmic barrier terms with variable steepness and adaptive scaling
        barrier = np.sum(np.log(1.0 + 0.4 * np.abs(x_scaled) + 0.12 * x_scaled**2 + 0.03 * np.abs(x_scaled)**3))
        
        # Complex trigonometric couplings with dynamic frequencies, phase shifts, and harmonic mixing
        freq_factor = 4.0 + 0.5 * np.sqrt(self.dim)
        phase_shift = 0.7 * np.sin(0.2 * self.dim)
        trig_coupling = np.sum(np.sin(freq_factor * x_scaled + phase_shift) * 
                              np.cos(freq_factor * x_scaled**2 + phase_shift * 0.7) * 
                              np.tanh(1.5 * x_scaled))
        
        # Adaptive radial terms with variable exponent, multi-scale influence, and coupling
        radial_base = x_scaled**2 + 0.1
        radial = (np.sum(radial_base**(-3.0)) * 0.9 + 
                  np.sum(radial_base**(-2.0)) * 0.1) * (1.0 + 0.15 * np.sin(2.5 * self.dim))
        
        # Coupled exponential and polynomial interactions with phase modulation and chaotic coupling
        exp_poly = np.sum(np.exp(-x_scaled**2) * (1.0 + x_scaled**3 + 0.2 * np.sin(6 * x_scaled)) * 
                         np.cos(0.5 * x_scaled**2))
        
        # Multi-scale chaotic modulation with varying amplitude, frequency, and temporal coupling
        chaotic = np.sum(np.sin(20 * np.sin(x_scaled)) * np.cos(16 * np.cos(x_scaled)) * 
                         np.tanh(3.0 * x_scaled) * (1.0 + 0.3 * np.sin(4 * x_scaled)) * 
                         np.exp(-0.5 * np.abs(x_scaled)))
        
        # Additional high-frequency oscillatory component with adaptive frequency and amplitude
        high_freq = np.sum(np.sin(35 * x_scaled) * np.cos(30 * x_scaled**3) * 
                          np.tanh(1.2 * x_scaled) * (1.0 + 0.1 * np.cos(7 * x_scaled)))
        
        # Cross-dimensional coupling with interaction terms between different dimensions
        cross_dim = np.sum(np.sin(x_scaled[:-1] + x_scaled[1:]) * 
                          np.cos(x_scaled[:-1] * x_scaled[1:]) * 
                          np.exp(-0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)))
        
        # Combined function with diverse curvature, multiple local minima, and enhanced conditioning
        return 5.0 * barrier + 1.5 * trig_coupling + 0.7 * radial + 0.5 * exp_poly + 0.4 * chaotic + 0.3 * high_freq + 0.2 * cross_dim