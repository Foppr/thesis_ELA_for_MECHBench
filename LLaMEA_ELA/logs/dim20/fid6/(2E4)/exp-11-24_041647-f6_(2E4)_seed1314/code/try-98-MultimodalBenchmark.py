import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced radial term with inverse exponential decay and additional harmonic components
        radial_term = np.sum(np.exp(-x_normalized**2) * (1 + 0.5 * np.sin(x_normalized * 3) + 0.3 * np.cos(x_normalized * 7)))
        
        # Improved sinusoidal modulation with frequency adaptation, amplitude scaling, and phase shifting
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 5) * (1 + 0.2 * np.sin(i * 0.4))
            amp = 1.0 / (1.0 + 0.3 * np.exp(-0.2 * i))
            phase = 0.3 * np.cos(i * 0.6)
            modulated_term += amp * np.sin(freq * x_normalized[i] + phase) * np.cos(freq * x_normalized[i] * 0.7 + phase)
        
        # Enhanced adaptive curvature with directional coupling and interaction scaling
        curvature_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_normalized[i] - x_normalized[j])
                coupling = np.exp(-distance * (2.0 + 0.4 * np.sin(i * 0.3 + j * 0.1)))
                curvature_term += coupling * (x_normalized[i]**4 + x_normalized[j]**4) * (1 + 0.1 * np.cos(i + j))
        
        # Enhanced chaotic gradient with multi-frequency perturbations and dynamic scaling
        chaotic_gradient = 0.0
        for i in range(self.dim):
            base_freq = 5 * (1 + 0.3 * np.sin(i * 0.6))
            perturbation = np.sin(base_freq * x_normalized[i]) * np.cos(base_freq * x_normalized[i] * 0.5)
            scaling = 1.0 / (1.0 + 0.2 * i**0.5)
            chaotic_gradient += perturbation * scaling * (1 + 0.15 * np.sin(i * 0.4))
        
        # Multi-scale interference with varying weights, phase shifts, and interaction types
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + (i + j) * 0.2)
                phase_shift = 0.4 * np.sin(i * 0.3 + j * 0.2)
                interference_term += weight * np.sin(10 * x_normalized[i] * x_normalized[j] + phase_shift) * np.cos(8 * x_normalized[i] + 6 * x_normalized[j])
        
        # Combined function with optimized weighting and additional nonlinearity
        return (0.3 * radial_term + 
                0.25 * modulated_term + 
                0.18 * curvature_term + 
                0.17 * chaotic_gradient + 
                0.3 * interference_term)