import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial term with varying degrees and adaptive coefficients
        poly_base = 0.0
        for i in range(self.dim):
            deg = (i % 5) + 2
            coeff = 1.0 + 0.5 * np.sin(i * 0.3)
            poly_base += coeff * (x[i]**deg) / (deg + 1)
        
        # Trigonometric coupling with recursive frequency modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            freq_i = 2 * (i % 6 + 1) * (1 + 0.3 * np.cos(i * 0.5))
            amp_i = 1.2 + 0.8 * np.sin(i * 0.4)
            for j in range(i+1, self.dim):
                freq_j = 3 * (j % 5 + 1) * (1 + 0.2 * np.sin(j * 0.6))
                amp_j = 1.0 + 0.6 * np.cos(j * 0.3)
                trig_coupling += amp_i * amp_j * np.sin(freq_i * x[i]) * np.cos(freq_j * x[j])
        
        # Multi-scale chaotic modulation with fractal-like behavior
        chaotic_mod = 0.0
        for i in range(self.dim):
            scale = 1.0 / (1.0 + np.exp(-2 * x[i]))
            chaotic_mod += scale * np.sin(25 * x[i]) * np.cos(20 * x[i]) * np.exp(-0.3 * x[i]**2)
        
        # Adaptive noise with recursive scaling and dimension-dependent strength
        adaptive_noise = 0.0
        for i in range(self.dim):
            noise_amp = 0.4 + 0.3 * np.sin(i * 0.7)
            adaptive_noise += noise_amp * np.sin(15 * x[i]) * np.cos(10 * x[i])
        
        # Cross-dimensional interaction with recursive coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * np.exp(-0.15 * (x[i]**2 + x[j]**2))
        
        # Ruggedness via recursive harmonic components with varying amplitudes
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += 0.6 * np.sin(35 * x[i]) * np.cos(25 * x[i]) + 0.4 * np.sin(45 * x[i])**2 + 0.2 * np.cos(55 * x[i])
        
        # Asymmetric potential wells with recursive depth modulation
        wells = 0.0
        for i in range(self.dim):
            wells += 0.7 * (x[i] - 1.8)**4 + 0.5 * (x[i] + 2.2)**3 + 0.3 * np.sin(12 * x[i])
        
        # Exponential interaction term with recursive scaling
        exp_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_interaction += np.exp(-0.4 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
        
        # Fractal-like scaling and recursive component
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += 0.3 * np.sin(50 * x[i]) * np.cos(40 * x[i]) * (1 + 0.2 * np.sin(i * 0.8))
        
        # Final combination with recursive weighted components
        return 0.6 * poly_base + 0.9 * trig_coupling + 0.7 * chaotic_mod + 0.5 * adaptive_noise + \
               0.8 * cross_interaction + 1.0 * ruggedness + 0.6 * wells + 0.4 * exp_interaction + 0.3 * fractal_component