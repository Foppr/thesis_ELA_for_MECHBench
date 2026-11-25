import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Fractal-like radial term with multi-scale exponential decay and quantum interference
        radial_term = np.sum(np.exp(-np.abs(x_normalized)**2.7) * 
                           (1 + 0.4 * np.sin(x_normalized * 5.5) + 
                            0.2 * np.cos(x_normalized * 11.5) + 
                            0.1 * np.sin(x_normalized * 17.5)))
        
        # Quantum-inspired sinusoidal modulation with complex phase coupling and dynamic amplitude
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 3 ** (i % 4) * (1 + 0.15 * np.sin(i * 0.55))
            amp = 1.0 / (1.0 + 0.25 * np.exp(-0.3 * i**1.1))
            phase = 0.5 * np.cos(i * 0.75 + 0.3 * np.sin(i * 0.45))
            modulated_term += amp * np.sin(freq * x_normalized[i] + phase) * np.cos(freq * x_normalized[i] * 0.85 + phase)
        
        # Fractal curvature with self-similar interaction scaling and multi-dimensional coupling
        curvature_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_normalized[i] - x_normalized[j])
                coupling = np.exp(-distance * (3.5 + 0.5 * np.sin(i * 0.25 + j * 0.15) + 
                                             0.3 * np.cos(i * 0.15 + j * 0.35)))
                curvature_term += coupling * (x_normalized[i]**5.5 + x_normalized[j]**5.5) * (1 + 0.2 * np.cos(i * 1.6 + j * 0.85))
        
        # Quantum chaotic gradient with multi-frequency entanglement and dynamic scaling
        chaotic_gradient = 0.0
        for i in range(self.dim):
            base_freq = 7.5 * (1 + 0.4 * np.sin(i * 0.75))
            perturbation = np.sin(base_freq * x_normalized[i]) * np.cos(base_freq * x_normalized[i] * 0.65)
            scaling = 1.0 / (1.0 + 0.3 * i**0.85)
            chaotic_gradient += perturbation * scaling * (1 + 0.2 * np.sin(i * 0.55 + 0.3 * np.cos(i * 0.35)))
        
        # Quantum interference with fractional weights and multi-dimensional phase shifts
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + (i + j) * 0.35 * np.sin(i * 0.25 + j * 0.15))
                phase_shift = 0.65 * np.sin(i * 0.45 + j * 0.35 + 0.2 * np.cos(i * 0.15 + j * 0.25))
                interference_term += weight * np.sin(15.5 * x_normalized[i] * x_normalized[j] + phase_shift) * \
                                  np.cos(12.5 * x_normalized[i] + 9.5 * x_normalized[j])
        
        # Combined function with optimized fractal weighting and additional nonlinearity
        return (0.23 * radial_term + 
                0.32 * modulated_term + 
                0.22 * curvature_term + 
                0.16 * chaotic_gradient + 
                0.37 * interference_term)