import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced radial basis with exponential scaling and perturbed peaks
        radial_term = np.sum(x_normalized**2) * (1.0 + 0.3 * np.sin(7.0 * np.sum(x_normalized**2)))
        
        # Multi-scale trigonometric chaos with adaptive frequencies and amplitudes
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 25.0 * (2.0 ** (i % 7)) * (1 + 0.6 * np.sin(i * 0.8))
            amp = 1.3 + 0.5 * np.cos(i * 1.1)
            chaotic_term += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.7) * np.exp(-0.5 * (x_normalized[i]**2))
        
        # Enhanced fractal pattern with nested sinusoidal components and variable scaling
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.0 / (1.0 + np.exp(-0.5 * (i + j)))
                fractal_term += scale * np.sin(35 * x_normalized[i] * x_normalized[j]) * np.cos(30 * x_normalized[i] - 25 * x_normalized[j])
        
        # Enhanced radial symmetry with multi-frequency modulation
        symmetry_term = 0.0
        for i in range(self.dim):
            symmetry_term += (np.sin(15 * np.sqrt(x_normalized[i]**2 + 0.01)) * 
                             np.cos(8 * np.arctan2(x_normalized[i], 1.0)) * 
                             np.exp(-0.5 * np.abs(x_normalized[i])))
        
        # Improved interference pattern with dynamic coupling and phase modulation
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Extended interaction range
                coupling = 0.8 * (1 + np.sin(0.6 * (i + j)) * np.cos(0.5 * (i - j)))
                phase_shift = 0.4 * np.sin(0.7 * i) * np.cos(0.7 * j)
                interference_term += coupling * np.sin(40 * x_normalized[i] + 30 * x_normalized[j] + phase_shift) * np.cos(35 * x_normalized[i] - 25 * x_normalized[j])
        
        # Additional high-frequency oscillation component for increased complexity
        high_freq_term = 0.0
        for i in range(self.dim):
            high_freq_term += np.sin(60 * x_normalized[i]) * np.cos(50 * x_normalized[i]) * (1 + 0.3 * np.sin(4 * x_normalized[i]))
        
        # Combined landscape with enhanced dimension-dependent scaling and adaptive weights
        return (0.38 * radial_term + 
                0.32 * chaotic_term + 
                0.22 * fractal_term + 
                0.20 * symmetry_term + 
                0.28 * interference_term + 
                0.12 * high_freq_term)