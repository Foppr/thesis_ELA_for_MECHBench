import numpy as np

class WaveBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Periodic wave interactions with varying frequencies and amplitudes
        wave_sum = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.5 * i)
            amp = 1.5 + 0.5 * np.cos(0.3 * i)
            wave_sum += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 0.7)
        
        # Exponential barrier structures with adaptive heights and widths
        barriers = 0.0
        for i in range(self.dim):
            height = 2.0 + 1.5 * np.sin(0.4 * i)
            width = 0.3 + 0.2 * np.cos(0.6 * i)
            barrier = height * np.exp(-0.5 * ((x_scaled[i] - 0.2 * np.sin(i)) / width)**2)
            barriers += barrier
        
        # Adaptive conditioning with dimension-wise scaling factors
        condition = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 2.0 * np.sin(0.3 * i)**2
            condition += cond_factor * x_scaled[i]**2
        
        # Multi-scale harmonic interference with complex phase relationships
        harmonic = 0.0
        scales = [1, 2, 3, 4, 5]
        for scale in scales:
            for i in range(self.dim):
                phase = np.sin(scale * x_scaled[i] + 0.5 * np.cos(scale * x_scaled[i]))
                harmonic += phase * np.exp(-0.1 * scale * np.abs(x_scaled[i]))
        
        # Complex valley structure with sigmoidal transitions and varying steepness
        valleys = 0.0
        for i in range(self.dim):
            steepness = 1.5 + 2.0 * np.sin(0.7 * i)
            valley1 = 1.0 / (1.0 + np.exp(-steepness * (x_scaled[i] - 0.3)))
            valley2 = 1.0 / (1.0 + np.exp(-steepness * (x_scaled[i] + 0.3)))
            valleys += (valley1 - 0.5)**2 + (valley2 - 0.5)**2
        
        # Combined function with carefully balanced components
        return 1.5 * wave_sum + 2.0 * barriers + 0.8 * condition + 1.2 * harmonic + 1.8 * valleys