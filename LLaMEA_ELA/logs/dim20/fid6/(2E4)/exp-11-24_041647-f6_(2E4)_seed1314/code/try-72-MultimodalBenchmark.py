import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced radial basis with exponential scaling and polynomial modulation
        radial_term = np.sum(x_normalized**2)
        
        # Multi-scale trigonometric chaos with dynamic frequency modulation and amplitude variations
        chaotic_term = 0.0
        for i in range(self.dim):
            freq = 15 * (3.0 ** (i % 5)) * (1 + 0.4 * np.sin(i * 0.6))
            amp = 1.0 + 0.3 * np.cos(i * 0.8)
            chaotic_term += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.7) * np.tan(0.5 * x_normalized[i])
        
        # Fractal pattern with nested sinusoidal components and dynamic scaling factors
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.0 / (1.0 + np.exp(-0.8 * (i + j)))
                fractal_term += scale * np.sin(25 * x_normalized[i] * x_normalized[j]) * np.cos(20 * x_normalized[i] - 15 * x_normalized[j]) * np.log(1 + abs(x_normalized[i] - x_normalized[j]))
        
        # Radial symmetry with perturbed peaks and valleys using hyperbolic functions
        symmetry_term = 0.0
        for i in range(self.dim):
            symmetry_term += np.sin(10 * np.sqrt(x_normalized[i]**2 + 0.01)) * np.cos(5 * np.arctan2(x_normalized[i], 1.0)) * np.exp(-0.5 * x_normalized[i]**2)
        
        # Multi-resolution interference pattern with adaptive coupling strengths and phase shifts
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended interaction range
                coupling = 0.6 * (1 + np.sin(0.4 * (i + j))) * np.cos(0.2 * (i - j))
                phase_shift = 0.3 * np.sin(0.5 * (i + j))
                interference_term += coupling * np.sin(30 * x_normalized[i] + 20 * x_normalized[j] + phase_shift) * np.cos(22 * x_normalized[i] - 16 * x_normalized[j] + phase_shift)
        
        # Enhanced landscape with adaptive dimension-dependent scaling and cross-terms
        return (0.4 * radial_term + 
                0.35 * chaotic_term + 
                0.25 * fractal_term + 
                0.15 * symmetry_term + 
                0.35 * interference_term)