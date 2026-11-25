import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced logarithmic barrier terms with variable steepness
        barrier = np.sum(np.log(1.0 + 0.35 * np.abs(x_scaled) + 0.09 * x_scaled**2))
        
        # Complex trigonometric couplings with dynamic frequencies and phase shifts
        freq_factor = 2.7 + 0.35 * np.sqrt(self.dim)
        phase_shift = 0.35 * np.sin(0.18 * self.dim)
        trig_coupling = np.sum(np.sin(freq_factor * x_scaled + phase_shift) * 
                              np.cos(freq_factor * x_scaled**2 + phase_shift * 0.65))
        
        # Adaptive radial terms with variable exponent and multi-scale influence
        radial_base = x_scaled**2 + 0.035
        radial = np.sum(radial_base**(-2.7)) * 0.65 + np.sum(radial_base**(-1.7)) * 0.35
        
        # Coupled exponential and polynomial interactions with phase modulation
        exp_poly = np.sum(np.exp(-x_scaled**2) * (1.0 + x_scaled**3.2 + 0.16 * np.sin(4.2 * x_scaled)))
        
        # Multi-scale chaotic modulation with varying amplitude and frequency
        chaotic = np.sum(np.sin(13 * np.sin(x_scaled)) * np.cos(11 * np.cos(x_scaled)) * 
                         np.tanh(1.6 * x_scaled) * (1.0 + 0.27 * np.sin(2.7 * x_scaled)))
        
        # Additional high-frequency oscillatory component
        high_freq = np.sum(np.sin(32 * x_scaled) * np.cos(27 * x_scaled**3.1))
        
        # Combined function with diverse curvature and multiple local minima
        return 3.7 * barrier + 1.3 * trig_coupling + 0.65 * radial + 0.55 * exp_poly + 0.42 * chaotic + 0.27 * high_freq