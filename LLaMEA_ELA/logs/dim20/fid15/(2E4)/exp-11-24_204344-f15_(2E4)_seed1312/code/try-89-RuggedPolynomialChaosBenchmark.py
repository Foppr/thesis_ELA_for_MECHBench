import numpy as np

class RuggedPolynomialChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial term with varying degrees
        poly_base = 0.0
        for i in range(self.dim):
            poly_base += (x[i]**(i % 4 + 2)) / (i % 3 + 1)
        
        # Trigonometric coupling with adaptive frequencies and amplitudes
        trig_coupling = 0.0
        for i in range(self.dim):
            freq_i = 2 * (i % 5 + 1)
            amp_i = 1.5 + 0.5 * np.sin(i * 0.7)
            for j in range(i+1, self.dim):
                freq_j = 3 * (j % 4 + 1)
                amp_j = 1.2 + 0.8 * np.cos(j * 0.9)
                trig_coupling += amp_i * amp_j * np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
        
        # Multi-scale chaotic modulation with exponential decay
        chaotic_mod = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-x[i]))
            chaotic_mod += scale * np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.exp(-0.5 * x[i]**2)
        
        # Adaptive noise with dimension-dependent strength
        adaptive_noise = 0.0
        for i in range(self.dim):
            noise_amp = 0.3 + 0.2 * np.sin(i * 0.5)
            adaptive_noise += noise_amp * np.sin(12 * x[i]) * np.cos(8 * x[i])
        
        # Cross-dimensional interaction with non-linear coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Ruggedness via multiple harmonic components with varying amplitudes
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += 0.5 * np.sin(30 * x[i]) * np.cos(18 * x[i]) + 0.3 * np.sin(40 * x[i])**2 + 0.1 * np.cos(50 * x[i])
        
        # Asymmetric potential wells with varying depth
        wells = 0.0
        for i in range(self.dim):
            wells += 0.6 * (x[i] - 1.5)**4 + 0.4 * (x[i] + 2.0)**3 + 0.2 * np.sin(10 * x[i])
        
        # Exponential interaction term with adaptive scaling
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_interaction += np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(4 * (x[i] + x[j]))
        
        # Enhanced cross-dimensional coupling with modified interaction weights
        enhanced_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                enhanced_coupling += 0.5 * np.sin(2 * x[i]) * np.cos(3 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Final combination with modified component weights
        return 0.6 * poly_base + 0.9 * trig_coupling + 0.7 * chaotic_mod + 0.5 * adaptive_noise + \
               0.8 * cross_interaction + 1.0 * ruggedness + 0.6 * wells + 0.4 * exp_interaction + 0.3 * enhanced_coupling