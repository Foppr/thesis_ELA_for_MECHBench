import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced logarithmic barrier terms with variable steepness and adaptive scaling
        barrier = np.sum(np.log(1.0 + 0.35 * np.abs(x_scaled) + 0.09 * x_scaled**2 + 0.025 * np.abs(x_scaled)**3))
        
        # Complex trigonometric couplings with dynamic frequencies, phase shifts and amplitude modulation
        freq_factor = 4.2 + 0.4 * np.sqrt(self.dim)
        phase_shift = 0.75 * np.sin(0.16 * self.dim)
        amp_mod = 1.0 + 0.32 * np.sin(0.21 * self.dim)
        trig_coupling = np.sum(amp_mod * np.sin(freq_factor * x_scaled + phase_shift) * 
                              np.cos(freq_factor * x_scaled**2 + phase_shift * 0.75))
        
        # Adaptive radial terms with variable exponent and multi-scale influence
        radial_base = x_scaled**2 + 0.12
        radial = np.sum(radial_base**(-3.2)) * 0.85 + np.sum(radial_base**(-1.6)) * 0.42
        
        # Coupled exponential and polynomial interactions with phase modulation and chaotic coupling
        exp_poly = np.sum(np.exp(-x_scaled**2) * (1.0 + x_scaled**3 + 0.16 * np.sin(6 * x_scaled) + 
                                                 0.055 * np.cos(4 * x_scaled**2)))
        
        # Multi-scale chaotic modulation with varying amplitude, frequency and coupling strength
        chaotic = np.sum(np.sin(21 * np.sin(x_scaled)) * np.cos(16 * np.cos(x_scaled)) * 
                         np.tanh(2.6 * x_scaled) * (1.0 + 0.31 * np.sin(4 * x_scaled)) * 
                         (0.81 + 0.21 * np.cos(2 * self.dim)))
        
        # Additional high-frequency oscillatory component with adaptive frequency
        high_freq = np.sum(np.sin(31 * x_scaled) * np.cos(26 * x_scaled**3) * 
                          (1.0 + 0.11 * np.sin(0.51 * self.dim)))
        
        # Add cross-dimensional coupling terms for increased conditioning
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(x_scaled[i] * x_scaled[j]) * (i + j) / (self.dim**2)
        
        # Combined function with diverse curvature and multiple local minima
        return 5.2 * barrier + 1.6 * trig_coupling + 0.62 * radial + 0.52 * exp_poly + 0.42 * chaotic + 0.32 * high_freq + 0.22 * cross_coupling