import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced radial term with inverse exponential decay
        radial_term = np.sum(np.exp(-x_normalized**2) * (1 + 0.5 * np.sin(x_normalized * 3)))
        
        # Improved sinusoidal modulation with frequency adaptation and amplitude scaling
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 3 ** (i % 4) * (1 + 0.3 * np.cos(i * 0.5))
            amp = 1.0 / (1.0 + 0.5 * np.exp(-0.3 * i))
            modulated_term += amp * np.sin(freq * x_normalized[i]) * np.cos(freq * x_normalized[i] * 0.8)
        
        # Enhanced adaptive curvature with directional coupling
        curvature_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_normalized[i] - x_normalized[j])
                coupling = np.exp(-distance * (1.5 + 0.3 * np.sin(i * 0.5 + j * 0.2)))
                curvature_term += coupling * (x_normalized[i]**3 + x_normalized[j]**3)
        
        # Enhanced chaotic gradient with multi-frequency perturbations
        chaotic_gradient = 0.0
        for i in range(self.dim):
            base_freq = 7 * (1 + 0.4 * np.sin(i * 0.7))
            perturbation = np.sin(base_freq * x_normalized[i]) * np.cos(base_freq * x_normalized[i] * 0.4)
            chaotic_gradient += perturbation * np.exp(-0.15 * i) * (1 + 0.2 * np.cos(i * 0.3))
        
        # Multi-scale interference with varying weights and phase shifts
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + (i + j) * 0.15)
                phase_shift = 0.5 * np.sin(i * 0.4 + j * 0.3)
                interference_term += weight * np.sin(12 * x_normalized[i] * x_normalized[j] + phase_shift) * np.cos(10 * x_normalized[i] + 8 * x_normalized[j])
        
        # Combined function with optimized weighting
        return (0.35 * radial_term + 
                0.25 * modulated_term + 
                0.2 * curvature_term + 
                0.15 * chaotic_gradient + 
                0.4 * interference_term)