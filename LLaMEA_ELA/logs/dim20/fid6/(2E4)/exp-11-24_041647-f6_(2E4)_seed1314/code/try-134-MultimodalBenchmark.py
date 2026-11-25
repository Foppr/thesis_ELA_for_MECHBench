import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced fractal radial term with higher-order polynomial and multi-scale oscillations
        radial_term = np.sum(np.exp(-np.abs(x_normalized)**3.2) * 
                           (1 + 0.5 * np.sin(x_normalized * 7) + 
                            0.3 * np.cos(x_normalized * 13) + 
                            0.2 * np.sin(x_normalized * 23) + 
                            0.1 * np.cos(x_normalized * 31)))
        
        # Quantum-inspired sinusoidal modulation with complex phase coupling and dynamic amplitude
        modulated_term = 0.0
        for i in range(self.dim):
            freq = 4 ** (i % 5) * (1 + 0.2 * np.sin(i * 0.6))
            amp = 1.0 / (1.0 + 0.3 * np.exp(-0.4 * i**1.3))
            phase = 0.6 * np.cos(i * 0.8 + 0.4 * np.sin(i * 0.5))
            modulated_term += amp * np.sin(freq * x_normalized[i] + phase) * np.cos(freq * x_normalized[i] * 0.9 + phase)
        
        # Enhanced fractal curvature with self-similar interaction scaling and multi-dimensional coupling
        curvature_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.abs(x_normalized[i] - x_normalized[j])
                coupling = np.exp(-distance * (4.0 + 0.8 * np.sin(i * 0.25 + j * 0.15) + 
                                             0.5 * np.cos(i * 0.15 + j * 0.35)))  
                curvature_term += coupling * (x_normalized[i]**6 + x_normalized[j]**6) * (1 + 0.3 * np.cos(i * 1.7 + j * 0.9))  
        
        # Enhanced quantum chaotic gradient with multi-frequency entanglement and dynamic scaling
        chaotic_gradient = 0.0
        for i in range(self.dim):
            base_freq = 9 * (1 + 0.5 * np.sin(i * 0.8))
            perturbation = np.sin(base_freq * x_normalized[i]) * np.cos(base_freq * x_normalized[i] * 0.7)
            scaling = 1.0 / (1.0 + 0.4 * i**0.9)
            chaotic_gradient += perturbation * scaling * (1 + 0.3 * np.sin(i * 0.6 + 0.4 * np.cos(i * 0.4)))  
        
        # Enhanced quantum interference with fractional weights and multi-dimensional phase shifts
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + (i + j) * 0.4 * np.sin(i * 0.25 + j * 0.15))  
                phase_shift = 0.7 * np.sin(i * 0.5 + j * 0.4 + 0.3 * np.cos(i * 0.15 + j * 0.25))  
                interference_term += weight * np.sin(18 * x_normalized[i] * x_normalized[j] + phase_shift) * \
                                  np.cos(14 * x_normalized[i] + 11 * x_normalized[j])
        
        # Enhanced hybrid coupling with additional nonlinearity and dynamic scaling
        hybrid_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add dynamic interaction strength based on dimension indices
                interaction_strength = (1 + 0.2 * np.sin(i * 0.3 + j * 0.4)) * (1 + 0.15 * np.cos(i * 0.2 + j * 0.3))
                # Add complex coupling with additional sinusoidal modulation
                coupling = interaction_strength * np.exp(-np.abs(x_normalized[i] - x_normalized[j]) * 
                                                        (3.0 + 0.7 * np.sin(i * 0.5 + j * 0.6)))
                hybrid_term += coupling * (x_normalized[i]**5 + x_normalized[j]**5) * \
                              (1 + 0.25 * np.sin(i * 1.2 + j * 1.1 + x_normalized[i] * x_normalized[j]))
        
        # Combined function with optimized fractal weighting and additional nonlinearity
        return (0.3 * radial_term + 
                0.35 * modulated_term + 
                0.25 * curvature_term +  
                0.18 * chaotic_gradient +  
                0.42 * interference_term +
                0.3 * hybrid_term)