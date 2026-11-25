import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced logarithmic barrier terms with variable steepness and adaptive scaling
        barrier = np.sum(np.log(1.0 + 0.38 * np.abs(x_scaled) + 0.12 * x_scaled**2 + 0.04 * np.abs(x_scaled)**3))
        
        # Complex trigonometric couplings with dynamic frequencies, phase shifts and amplitude modulation
        freq_factor = 5.3 + 0.4 * np.sqrt(self.dim)
        phase_shift = 0.9 * np.sin(0.23 * self.dim)
        amp_mod = 1.0 + 0.38 * np.sin(0.29 * self.dim)
        trig_coupling = np.sum(amp_mod * np.sin(freq_factor * x_scaled + phase_shift) * 
                              np.cos(freq_factor * x_scaled**2 + phase_shift * 0.88))
        
        # Adaptive radial terms with variable exponent and multi-scale influence
        radial_base = x_scaled**2 + 0.13
        radial = np.sum(radial_base**(-3.9)) * 0.95 + np.sum(radial_base**(-2.2)) * 0.55
        
        # Coupled exponential and polynomial interactions with phase modulation and chaotic coupling
        exp_poly = np.sum(np.exp(-x_scaled**2) * (1.0 + x_scaled**3 + 0.23 * np.sin(7 * x_scaled) + 
                                                 0.08 * np.cos(5 * x_scaled**2)))
        
        # Multi-scale chaotic modulation with varying amplitude, frequency and coupling strength
        chaotic = np.sum(np.sin(27 * np.sin(x_scaled)) * np.cos(21 * np.cos(x_scaled)) * 
                         np.tanh(3.3 * x_scaled) * (1.0 + 0.4 * np.sin(5 * x_scaled)) * 
                         (0.9 + 0.3 * np.cos(2.7 * self.dim)))
        
        # Additional high-frequency oscillatory component with adaptive frequency
        high_freq = np.sum(np.sin(39 * x_scaled) * np.cos(33 * x_scaled**3) * 
                          (1.0 + 0.16 * np.sin(0.65 * self.dim)))
        
        # Add cross-dimensional coupling terms for increased conditioning
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(x_scaled[i] * x_scaled[j]) * (i + j) / (self.dim**2)
        
        # Combined function with diverse curvature and multiple local minima
        return 5.8 * barrier + 1.7 * trig_coupling + 0.69 * radial + 0.59 * exp_poly + 0.49 * chaotic + 0.37 * high_freq + 0.25 * cross_coupling