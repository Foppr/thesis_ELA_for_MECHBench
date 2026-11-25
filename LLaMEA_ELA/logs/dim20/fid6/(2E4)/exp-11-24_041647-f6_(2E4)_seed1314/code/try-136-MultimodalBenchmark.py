import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Radial component with chaotic sine modulation and exponential decay
        radial = np.sum(np.exp(-np.abs(x_normalized)**1.3) * 
                       (1 + 0.6 * np.sin(7 * x_normalized) + 
                        0.3 * np.cos(13 * x_normalized) + 
                        0.2 * np.sin(23 * x_normalized)))
        
        # Multi-frequency oscillatory term with dynamic amplitude and phase
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * 0.4)
            amp = 1.0 / (1.0 + 0.2 * np.exp(-0.5 * i))
            phase = 0.5 * np.cos(i * 0.3 + 0.2 * np.sin(i * 0.7))
            oscillatory += amp * np.sin(freq * x_normalized[i] + phase) * \
                          np.cos(freq * x_normalized[i] * 0.9 + phase)
        
        # Cross-dimensional coupling with fractal-like interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_normalized[i] - x_normalized[j])
                weight = 1.0 / (1.0 + 0.5 * dist**2.5)
                coupling += weight * np.sin(5 * (x_normalized[i]**2 + x_normalized[j]**2)) * \
                           np.cos(3 * x_normalized[i] * x_normalized[j])
        
        # Chaotic gradient component with multi-scale sinusoidal perturbations
        chaotic = 0.0
        for i in range(self.dim):
            base_freq = 5.0 + 3.0 * np.sin(i * 0.6)
            perturb = np.sin(base_freq * x_normalized[i]) * np.cos(base_freq * x_normalized[i] * 0.7)
            scaling = 1.0 / (1.0 + 0.4 * i**1.1)
            chaotic += perturb * scaling
        
        # Fractional power interaction with adaptive weighting
        fractional = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                frac_weight = 1.0 / (1.0 + 0.3 * np.abs(x_normalized[i] - x_normalized[j]))
                fractional += frac_weight * (x_normalized[i]**1.7 + x_normalized[j]**1.7) * \
                             np.sin(4 * (x_normalized[i] + x_normalized[j]))
        
        # Final combined function with balanced contributions
        return (0.3 * radial + 
                0.25 * oscillatory + 
                0.2 * coupling + 
                0.15 * chaotic + 
                0.1 * fractional)