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
            freq = 20.0 * (2.0 ** (i % 6)) * (1 + 0.5 * np.sin(i * 0.7))
            amp = 1.2 + 0.4 * np.cos(i * 0.9)
            chaotic_term += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.6) * np.exp(-0.4 * (x_normalized[i]**2))
        
        # Enhanced fractal pattern with nested sinusoidal components and variable scaling
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.0 / (1.0 + np.exp(-0.4 * (i + j)))
                fractal_term += scale * np.sin(30 * x_normalized[i] * x_normalized[j]) * np.cos(25 * x_normalized[i] - 20 * x_normalized[j])
        
        # Enhanced radial symmetry with multi-frequency modulation
        symmetry_term = 0.0
        for i in range(self.dim):
            symmetry_term += (np.sin(12 * np.sqrt(x_normalized[i]**2 + 0.01)) * 
                             np.cos(6 * np.arctan2(x_normalized[i], 1.0)) * 
                             np.exp(-0.4 * np.abs(x_normalized[i])))
        
        # Improved interference pattern with dynamic coupling and phase modulation
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended interaction range
                coupling = 0.7 * (1 + np.sin(0.5 * (i + j)) * np.cos(0.4 * (i - j)))
                phase_shift = 0.3 * np.sin(0.6 * i) * np.cos(0.6 * j)
                interference_term += coupling * np.sin(35 * x_normalized[i] + 25 * x_normalized[j] + phase_shift) * np.cos(30 * x_normalized[i] - 22 * x_normalized[j])
        
        # Additional high-frequency oscillation component for increased complexity
        high_freq_term = 0.0
        for i in range(self.dim):
            high_freq_term += np.sin(50 * x_normalized[i]) * np.cos(40 * x_normalized[i]) * (1 + 0.2 * np.sin(3 * x_normalized[i]))
        
        # Combined landscape with enhanced dimension-dependent scaling and adaptive weights
        return (0.35 * radial_term + 
                0.3 * chaotic_term + 
                0.2 * fractal_term + 
                0.18 * symmetry_term + 
                0.25 * interference_term + 
                0.1 * high_freq_term)