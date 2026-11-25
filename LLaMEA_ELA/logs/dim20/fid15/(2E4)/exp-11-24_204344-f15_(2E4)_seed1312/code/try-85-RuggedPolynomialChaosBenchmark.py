import numpy as np

class RuggedPolynomialChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial term with varying degrees and adaptive coefficients
        poly_base = 0.0
        for i in range(self.dim):
            degree = i % 5 + 2
            coeff = 1.0 + 0.3 * np.sin(i * 0.8)
            poly_base += coeff * (x[i]**degree) / (degree + 1)
        
        # Enhanced trigonometric coupling with dynamic frequencies and amplitudes
        trig_coupling = 0.0
        for i in range(self.dim):
            freq_i = 2.5 * (i % 6 + 1)
            amp_i = 1.8 + 0.4 * np.cos(i * 0.6)
            for j in range(i+1, self.dim):
                freq_j = 3.5 * (j % 5 + 1)
                amp_j = 1.5 + 0.5 * np.sin(j * 0.7)
                trig_coupling += amp_i * amp_j * np.cos(freq_i * x[i]) * np.sin(freq_j * x[j])
        
        # Multi-scale chaotic modulation with complex interaction
        chaotic_mod = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-x[i]))
            chaotic_mod += scale * np.cos(25 * x[i]) * np.sin(20 * x[i]) * np.exp(-0.3 * x[i]**2)
        
        # Adaptive noise with multi-frequency components
        adaptive_noise = 0.0
        for i in range(self.dim):
            noise_amp = 0.4 + 0.3 * np.cos(i * 0.4)
            adaptive_noise += noise_amp * (np.sin(15 * x[i]) * np.cos(10 * x[i]) + 
                                          0.5 * np.sin(25 * x[i])**2)
        
        # Cross-dimensional interaction with non-linear coupling and exponential decay
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = (x[i]**2 + x[j]**2)
                cross_interaction += dist * np.cos(x[i] * x[j]) * np.exp(-0.15 * dist)
        
        # Enhanced ruggedness via multiple harmonic components with varying amplitudes and frequencies
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += 0.6 * np.cos(35 * x[i]) * np.sin(22 * x[i]) + 0.4 * np.sin(45 * x[i])**2 + 0.2 * np.cos(55 * x[i])
        
        # Asymmetric potential wells with varying depth and complex structure
        wells = 0.0
        for i in range(self.dim):
            wells += 0.7 * (x[i] - 1.8)**4 + 0.5 * (x[i] + 2.5)**3 + 0.3 * np.cos(12 * x[i])
        
        # Exponential interaction term with adaptive scaling and additional coupling
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_interaction += np.exp(-0.4 * (x[i] - x[j])**2) * np.cos(5 * (x[i] + x[j]))
        
        # Additional high-frequency oscillation term
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += 0.3 * np.sin(60 * x[i]) * np.cos(40 * x[i])
        
        # Final combination with weighted components
        return 0.6 * poly_base + 0.9 * trig_coupling + 0.7 * chaotic_mod + 0.5 * adaptive_noise + \
               0.8 * cross_interaction + 1.0 * ruggedness + 0.6 * wells + 0.4 * exp_interaction + 0.2 * high_freq