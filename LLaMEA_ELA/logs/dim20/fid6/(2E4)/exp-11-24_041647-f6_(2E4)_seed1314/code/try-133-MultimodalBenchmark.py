import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced fractal radial term with multi-scale exponential decay and quantum interference
        radial_term = np.sum(np.exp(-np.abs(x_normalized)**3.2) * 
                           (1 + 0.55 * np.sin(x_normalized * 7) + 
                            0.35 * np.cos(x_normalized * 13) + 
                            0.25 * np.sin(x_normalized * 19) + 
                            0.18 * np.cos(x_normalized * 23)))
        
        # Quantum-inspired sinusoidal modulation with complex phase coupling and dynamic amplitude
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 4 ** (i % 5) * (1 + 0.3 * np.sin(i * 0.6))
            amp = 1.0 / (1.0 + 0.4 * np.exp(-0.4 * i**1.3))
            phase = 0.7 * np.cos(i * 0.8 + 0.4 * np.sin(i * 0.5))
            modulated_term += amp * np.sin(freq * x_normalized[i] + phase) * np.cos(freq * x_normalized[i] * 0.9 + phase)
        
        # Fractal curvature with self-similar interaction scaling and multi-dimensional coupling
        curvature_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_normalized[i] - x_normalized[j])
                coupling = np.exp(-distance * (4.2 + 0.8 * np.sin(i * 0.25 + j * 0.15) + 
                                             0.5 * np.cos(i * 0.15 + j * 0.35)))  
                curvature_term += coupling * (x_normalized[i]**6 + x_normalized[j]**6) * (1 + 0.4 * np.cos(i * 1.7 + j * 0.9))
        
        # Quantum chaotic gradient with multi-frequency entanglement and dynamic scaling
        chaotic_gradient = 0.0
        for i in range(self.dim):
            base_freq = 9.0 * (1 + 0.5 * np.sin(i * 0.8))
            perturbation = np.sin(base_freq * x_normalized[i]) * np.cos(base_freq * x_normalized[i] * 0.7)
            scaling = 1.0 / (1.0 + 0.4 * i**0.9)
            chaotic_gradient += perturbation * scaling * (1 + 0.4 * np.sin(i * 0.6 + 0.4 * np.cos(i * 0.35)))  
        
        # Quantum interference with fractional weights and multi-dimensional phase shifts
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + (i + j) * 0.5 * np.sin(i * 0.25 + j * 0.15))  
                phase_shift = 0.8 * np.sin(i * 0.5 + j * 0.4 + 0.3 * np.cos(i * 0.15 + j * 0.25))  
                interference_term += weight * np.sin(18 * x_normalized[i] * x_normalized[j] + phase_shift) * \
                                  np.cos(15 * x_normalized[i] + 12 * x_normalized[j])
        
        # Combined function with optimized fractal weighting and additional nonlinearity
        return (0.3 * radial_term + 
                0.35 * modulated_term + 
                0.28 * curvature_term +  
                0.22 * chaotic_gradient +  
                0.42 * interference_term)