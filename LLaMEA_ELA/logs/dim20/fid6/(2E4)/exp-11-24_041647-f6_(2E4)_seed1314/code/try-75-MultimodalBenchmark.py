import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced radial basis with exponential scaling and perturbed peaks
        radial_term = np.sum(x_normalized**2) * (1.0 + 0.2 * np.sin(5.0 * np.sum(x_normalized**2)))
        
        # Multi-scale trigonometric chaos with adaptive frequencies and amplitudes
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 15.0 * (2.0 ** (i % 5)) * (1 + 0.4 * np.sin(i * 0.6))
            amp = 1.0 + 0.3 * np.cos(i * 0.8)
            chaotic_term += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.7) * np.exp(-0.5 * (x_normalized[i]**2))
        
        # Enhanced fractal pattern with nested sinusoidal components and variable scaling
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.0 / (1.0 + np.exp(-0.3 * (i + j)))
                fractal_term += scale * np.sin(25 * x_normalized[i] * x_normalized[j]) * np.cos(20 * x_normalized[i] - 15 * x_normalized[j])
        
        # Enhanced radial symmetry with multi-frequency modulation
        symmetry_term = 0.0
        for i in range(self.dim):
            symmetry_term += (np.sin(10 * np.sqrt(x_normalized[i]**2 + 0.01)) * 
                             np.cos(5 * np.arctan2(x_normalized[i], 1.0)) * 
                             np.exp(-0.3 * np.abs(x_normalized[i])))
        
        # Improved interference pattern with dynamic coupling and phase modulation
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended interaction range
                coupling = 0.6 * (1 + np.sin(0.4 * (i + j)) * np.cos(0.3 * (i - j)))
                phase_shift = 0.2 * np.sin(0.5 * i) * np.cos(0.5 * j)
                interference_term += coupling * np.sin(30 * x_normalized[i] + 20 * x_normalized[j] + phase_shift) * np.cos(25 * x_normalized[i] - 18 * x_normalized[j])
        
        # Combined landscape with enhanced dimension-dependent scaling and adaptive weights
        return (0.4 * radial_term + 
                0.35 * chaotic_term + 
                0.25 * fractal_term + 
                0.15 * symmetry_term + 
                0.3 * interference_term)