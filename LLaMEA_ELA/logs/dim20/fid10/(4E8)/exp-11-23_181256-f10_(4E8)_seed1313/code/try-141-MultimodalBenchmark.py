import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced logarithmic barrier terms with variable steepness and adaptive scaling
        barrier = np.sum(np.log(1.0 + 0.4 * np.abs(x_scaled) + 0.1 * x_scaled**2 + 0.03 * np.abs(x_scaled)**3))
        
        # Complex trigonometric couplings with dynamic frequencies, phase shifts and amplitude modulation
        freq_factor = 5.0 + 0.5 * np.sqrt(self.dim)
        phase_shift = 0.8 * np.sin(0.2 * self.dim)
        amp_mod = 1.0 + 0.4 * np.sin(0.25 * self.dim)
        trig_coupling = np.sum(amp_mod * np.sin(freq_factor * x_scaled + phase_shift) * 
                              np.cos(freq_factor * x_scaled**2 + phase_shift * 0.8))
        
        # Adaptive radial terms with variable exponent and multi-scale influence
        radial_base = x_scaled**2 + 0.15
        radial = np.sum(radial_base**(-3.5)) * 0.9 + np.sum(radial_base**(-1.8)) * 0.5
        
        # Coupled exponential and polynomial interactions with phase modulation and chaotic coupling
        exp_poly = np.sum(np.exp(-x_scaled**2) * (1.0 + x_scaled**3 + 0.2 * np.sin(6 * x_scaled) + 
                                                 0.06 * np.cos(4 * x_scaled**2)))
        
        # Multi-scale chaotic modulation with varying amplitude, frequency and coupling strength
        chaotic = np.sum(np.sin(25 * np.sin(x_scaled)) * np.cos(20 * np.cos(x_scaled)) * 
                         np.tanh(3.0 * x_scaled) * (1.0 + 0.35 * np.sin(4 * x_scaled)) * 
                         (0.85 + 0.25 * np.cos(2 * self.dim)))
        
        # Additional high-frequency oscillatory component with adaptive frequency
        high_freq = np.sum(np.sin(35 * x_scaled) * np.cos(30 * x_scaled**3) * 
                          (1.0 + 0.15 * np.sin(0.6 * self.dim)))
        
        # Add cross-dimensional coupling terms for increased conditioning
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(x_scaled[i] * x_scaled[j]) * (i + j) / (self.dim**2)
        
        # Introduce a new hyperchaotic sine-cosine coupling mechanism
        hyperchaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range for hyperchaos
                hyperchaos += np.sin(7 * x_scaled[i]) * np.cos(8 * x_scaled[j]) * \
                              np.tanh(x_scaled[i] + x_scaled[j]) * \
                              (0.5 + 0.3 * np.sin(2.5 * self.dim + i - j))
        
        # Reshape radial components with new power laws and interaction terms
        radial_new = np.sum((x_scaled**2 + 0.2)**(-4.0)) * 1.1 + \
                     np.sum((x_scaled**2 + 0.1)**(-2.5)) * 0.7 + \
                     np.sum(np.abs(x_scaled)**(1.5)) * 0.3
        
        # Combined function with diverse curvature and multiple local minima
        return 6.0 * barrier + 1.8 * trig_coupling + 0.7 * radial_new + 0.6 * exp_poly + \
               0.5 * chaotic + 0.4 * high_freq + 0.3 * cross_coupling + 0.2 * hyperchaos