import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial basis with fractal scaling and multi-resolution interference
        radial_term = np.sum(x_normalized**2)
        
        # Multi-scale trigonometric chaos with varying frequencies and amplitudes
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 10 * (2.0 ** (i % 4)) * (1 + 0.3 * np.sin(i * 0.5))
            amp = 0.8 + 0.2 * np.cos(i * 0.7)
            chaotic_term += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.5)
        
        # Self-similar fractal pattern with nested sinusoidal components
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.0 / (1.0 + np.exp(-0.5 * (i + j)))
                fractal_term += scale * np.sin(20 * x_normalized[i] * x_normalized[j]) * np.cos(15 * x_normalized[i] - 10 * x_normalized[j])
        
        # Radial symmetry with perturbed peaks and valleys
        symmetry_term = 0.0
        for i in range(self.dim):
            symmetry_term += np.sin(8 * np.sqrt(x_normalized[i]**2 + 0.01)) * np.cos(4 * np.arctan2(x_normalized[i], 1.0))
        
        # Multi-resolution interference pattern with varying coupling strengths
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction range
                coupling = 0.5 * (1 + np.sin(0.3 * (i + j)))
                interference_term += coupling * np.sin(25 * x_normalized[i] + 15 * x_normalized[j]) * np.cos(18 * x_normalized[i] - 12 * x_normalized[j])
        
        # Combined landscape with dimension-dependent scaling
        return (0.5 * radial_term + 
                0.3 * chaotic_term + 
                0.2 * fractal_term + 
                0.1 * symmetry_term + 
                0.4 * interference_term)