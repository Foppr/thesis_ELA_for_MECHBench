import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced logarithmic barrier terms with variable steepness and adaptive scaling
        barrier = np.sum(np.log(1.0 + 0.3 * np.abs(x_scaled) + 0.08 * x_scaled**2 + 0.02 * np.abs(x_scaled)**3))
        
        # Complex trigonometric couplings with dynamic frequencies, phase shifts and amplitude modulation
        freq_factor = 4.0 + 0.5 * np.sqrt(self.dim)
        phase_shift = 0.7 * np.sin(0.15 * self.dim)
        amp_mod = 1.0 + 0.3 * np.sin(0.2 * self.dim)
        trig_coupling = np.sum(amp_mod * np.sin(freq_factor * x_scaled + phase_shift) * 
                              np.cos(freq_factor * x_scaled**2 + phase_shift * 0.7))
        
        # Adaptive radial terms with variable exponent and multi-scale influence
        radial_base = x_scaled**2 + 0.1
        radial = np.sum(radial_base**(-3.0)) * 0.8 + np.sum(radial_base**(-1.5)) * 0.4
        
        # Coupled exponential and polynomial interactions with phase modulation and chaotic coupling
        exp_poly = np.sum(np.exp(-x_scaled**2) * (1.0 + x_scaled**3 + 0.15 * np.sin(6 * x_scaled) + 
                                                 0.05 * np.cos(4 * x_scaled**2)))
        
        # Multi-scale chaotic modulation with varying amplitude, frequency and coupling strength
        chaotic = np.sum(np.sin(20 * np.sin(x_scaled)) * np.cos(15 * np.cos(x_scaled)) * 
                         np.tanh(2.5 * x_scaled) * (1.0 + 0.3 * np.sin(4 * x_scaled)) * 
                         (0.8 + 0.2 * np.cos(2 * self.dim)))
        
        # Additional high-frequency oscillatory component with adaptive frequency
        high_freq = np.sum(np.sin(30 * x_scaled) * np.cos(25 * x_scaled**3) * 
                          (1.0 + 0.1 * np.sin(0.5 * self.dim)))
        
        # Add cross-dimensional coupling terms for increased conditioning
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(x_scaled[i] * x_scaled[j]) * (i + j) / (self.dim**2)
        
        # Combined function with diverse curvature and multiple local minima
        return 5.0 * barrier + 1.5 * trig_coupling + 0.6 * radial + 0.5 * exp_poly + 0.4 * chaotic + 0.3 * high_freq + 0.2 * cross_coupling