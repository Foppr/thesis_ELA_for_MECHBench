import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Nested polynomial potential with varying exponents and chaotic scaling
        poly_term = 0.0
        for i in range(self.dim):
            exp = 2 + (i % 4)  # Exponents: 2, 3, 4, 5 repeating
            scale = 0.15 * np.sin(0.8 * i) + 0.25
            poly_term += scale * (x[i] ** exp) * np.exp(-0.2 * np.abs(x[i]))
        
        # Coupled sine-wave modulation with chaotic frequency and phase shifts
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_i = 1.5 + 0.4 * np.sin(0.9 * i + 0.3 * np.cos(j))
                freq_j = 1.5 + 0.4 * np.cos(0.9 * j + 0.3 * np.sin(i))
                phase_shift = 0.2 * np.sin(0.6 * i * j)
                trig_coupling += 0.12 * np.sin(freq_i * x[i] + freq_j * x[j] + phase_shift) * np.cos(0.5 * x[i] * x[j])
        
        # Adaptive noise with chaotic amplitude modulation and multi-scale components
        noise = 0.0
        for i in range(self.dim):
            amp_mod = 0.1 * np.sin(20 * x[i]) + 0.15
            noise += amp_mod * np.sin(25 * x[i]) * np.cos(18 * x[i]) * (1 + 0.3 * i)
        
        # Cross-dimensional interaction with multi-scale cosine modulation and distance-dependent decay
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                scale_factor = 0.08 * np.sin(0.5 * i) * np.cos(0.5 * j)
                interaction += scale_factor * np.exp(-dist) * np.cos(5 * x[i]) * np.sin(4 * x[j])
        
        # Global shaping with nested sinusoidal terms and exponential decay
        global_shape = 0.0
        for i in range(self.dim):
            global_shape += 0.1 * np.sin(0.6 * x[i]) * np.cos(0.5 * x[i]) * (x[i]**3 + 2) * np.exp(-0.1 * x[i]**2)
        
        return poly_term + trig_coupling + noise + interaction + global_shape