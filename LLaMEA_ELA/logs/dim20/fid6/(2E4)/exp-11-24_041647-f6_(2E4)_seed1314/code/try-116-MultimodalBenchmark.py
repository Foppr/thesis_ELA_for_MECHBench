import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Fractal-like radial term with multi-scale exponential decay and quantum interference
        radial_term = np.sum(np.exp(-np.abs(x_normalized)**2.5) * 
                           (1 + 0.4 * np.sin(x_normalized * 5) + 
                            0.2 * np.cos(x_normalized * 11) + 
                            0.1 * np.sin(x_normalized * 17)))
        
        # Quantum-inspired sinusoidal modulation with complex phase coupling and dynamic amplitude
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 3 ** (i % 4) * (1 + 0.15 * np.sin(i * 0.5))
            amp = 1.0 / (1.0 + 0.25 * np.exp(-0.3 * i**1.2))
            phase = 0.5 * np.cos(i * 0.7 + 0.3 * np.sin(i * 0.4))
            modulated_term += amp * np.sin(freq * x_normalized[i] + phase) * np.cos(freq * x_normalized[i] * 0.8 + phase)
        
        # Fractal curvature with self-similar interaction scaling and multi-dimensional coupling (modified)
        curvature_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_normalized[i] - x_normalized[j])
                coupling = np.exp(-distance * (3.5 + 0.6 * np.sin(i * 0.2 + j * 0.1) + 
                                             0.35 * np.cos(i * 0.1 + j * 0.3)))  # Slight increase in coupling strength
                curvature_term += coupling * (x_normalized[i]**5 + x_normalized[j]**5) * (1 + 0.25 * np.cos(i * 1.5 + j * 0.8))  # Increased cosine weight
        
        # Quantum chaotic gradient with multi-frequency entanglement and dynamic scaling
        chaotic_gradient = 0.0
        for i in range(self.dim):
            base_freq = 7 * (1 + 0.4 * np.sin(i * 0.7))
            perturbation = np.sin(base_freq * x_normalized[i]) * np.cos(base_freq * x_normalized[i] * 0.6)
            scaling = 1.0 / (1.0 + 0.3 * i**0.8)
            chaotic_gradient += perturbation * scaling * (1 + 0.25 * np.sin(i * 0.5 + 0.3 * np.cos(i * 0.3)))  # Increased sinusoidal influence
        
        # Quantum interference with fractional weights and multi-dimensional phase shifts (modified)
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + (i + j) * 0.35 * np.sin(i * 0.2 + j * 0.1))  # Slight increase in weight sensitivity
                phase_shift = 0.65 * np.sin(i * 0.4 + j * 0.3 + 0.2 * np.cos(i * 0.1 + j * 0.2))  # Increased phase shift magnitude
                interference_term += weight * np.sin(15 * x_normalized[i] * x_normalized[j] + phase_shift) * \
                                  np.cos(12 * x_normalized[i] + 9 * x_normalized[j])
        
        # Combined function with optimized fractal weighting and additional nonlinearity
        return (0.25 * radial_term + 
                0.3 * modulated_term + 
                0.22 * curvature_term +  # Slight increase in curvature influence
                0.16 * chaotic_gradient +  # Slight increase in chaotic gradient influence
                0.37 * interference_term)  # Slight increase in interference influence