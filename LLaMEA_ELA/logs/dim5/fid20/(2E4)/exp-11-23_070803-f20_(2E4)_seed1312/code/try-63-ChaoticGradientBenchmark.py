import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic gradient component with logistic map modulation
        chaotic_term = 0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            # Logistic map for dynamic modulation
            logistic_val = r * x_norm[i] * (1 - x_norm[i])
            chaotic_term += logistic_val * np.sin(10 * x_norm[i]) * np.cos(5 * x_norm[i])
        
        # Composite sinusoidal modulations with frequency mixing
        sin_term = 0
        for i in range(self.dim):
            freq1 = 3 + (i % 7)
            freq2 = 5 + ((i * 2) % 8)
            freq3 = 7 + ((i * 5) % 9)
            sin_term += np.sin(freq1 * x_norm[i]) * np.cos(freq2 * x_norm[i]) * np.sin(freq3 * x_norm[i])
        
        # Adaptive basin structures with dynamic scaling
        basin_term = 0
        for i in range(self.dim):
            scale_factor = 1.5 + 0.5 * np.sin(2 * x_norm[i])
            basin_term += (x_norm[i]**4 - 2 * x_norm[i]**3 + x_norm[i]**2) * scale_factor
        
        # Enhanced cross-dimensional coupling with chaotic interactions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                coupling_strength = 2.0 / (1 + 0.2 * np.abs(i - j))
                # Chaotic interaction term
                chaotic_interaction = np.sin(x_norm[i] + x_norm[j]) * np.cos(x_norm[i] - x_norm[j])
                chaotic_interaction += 0.3 * np.sin(3 * x_norm[i] + 2 * x_norm[j])
                cross_term += coupling_strength * (x_norm[i]**2) * (x_norm[j]**2) * chaotic_interaction
        
        # Modified trigonometric interference with phase modulation
        phase_term = 0
        for i in range(self.dim):
            phase_shift1 = np.pi * (i % 4) / 4
            phase_shift2 = np.pi * ((i * 3) % 5) / 5
            phase_term += np.sin(2 * x_norm[i] + phase_shift1) * np.cos(3 * x_norm[i] + phase_shift2)
        
        # Additional harmonic resonance component
        resonance_term = 0
        for i in range(self.dim):
            resonance_term += (np.sin(4 * x_norm[i]) + 0.5 * np.cos(7 * x_norm[i])) * \
                             (1 + 0.3 * np.sin(2 * x_norm[i]))
        
        # Combine all components with optimized weights
        result = 1.8 * chaotic_term + 1.5 * sin_term + 1.2 * basin_term + 1.4 * cross_term + 0.9 * phase_term + 0.7 * resonance_term
        
        # Add chaotic noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise