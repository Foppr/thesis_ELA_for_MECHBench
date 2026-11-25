import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Chaotic gradient component with modified logistic map modulation
        chaotic_term = 0
        r = 3.8  # Slightly reduced chaos parameter
        for i in range(self.dim):
            # Modified logistic map for dynamic modulation
            logistic_val = r * x_norm[i] * (1 - x_norm[i])
            chaotic_term += logistic_val * np.sin(8 * x_norm[i]) * np.cos(4 * x_norm[i])
        
        # Composite sinusoidal modulations with altered frequencies
        sin_term = 0
        for i in range(self.dim):
            freq1 = 2 + (i % 5)  # Reduced base frequency
            freq2 = 6 + ((i * 3) % 9)
            freq3 = 8 + ((i * 4) % 10)
            sin_term += np.sin(freq1 * x_norm[i]) * np.cos(freq2 * x_norm[i]) * np.sin(freq3 * x_norm[i])
        
        # Adaptive basin structures with modified scaling
        basin_term = 0
        for i in range(self.dim):
            scale_factor = 1.2 + 0.8 * np.sin(3 * x_norm[i])  # Changed scaling function
            basin_term += (x_norm[i]**4 - 2 * x_norm[i]**3 + x_norm[i]**2) * scale_factor
        
        # Enhanced cross-dimensional coupling with modified interactions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Reduced coupling range
                coupling_strength = 1.5 / (1 + 0.3 * np.abs(i - j))
                # Modified chaotic interaction term
                chaotic_interaction = np.sin(x_norm[i] + x_norm[j]) * np.cos(x_norm[i] - x_norm[j])
                chaotic_interaction += 0.2 * np.sin(4 * x_norm[i] + 3 * x_norm[j])
                cross_term += coupling_strength * (x_norm[i]**2) * (x_norm[j]**2) * chaotic_interaction
        
        # Modified trigonometric interference with phase modulation
        phase_term = 0
        for i in range(self.dim):
            phase_shift1 = np.pi * (i % 3) / 3  # Different phase shift pattern
            phase_shift2 = np.pi * ((i * 4) % 6) / 6
            phase_term += np.sin(3 * x_norm[i] + phase_shift1) * np.cos(2 * x_norm[i] + phase_shift2)
        
        # Additional harmonic resonance component with altered weights
        resonance_term = 0
        for i in range(self.dim):
            resonance_term += (np.sin(5 * x_norm[i]) + 0.4 * np.cos(6 * x_norm[i])) * \
                             (1 + 0.2 * np.sin(3 * x_norm[i]))
        
        # Combine all components with modified weights
        result = 2.1 * chaotic_term + 1.3 * sin_term + 1.0 * basin_term + 1.6 * cross_term + 1.1 * phase_term + 0.8 * resonance_term
        
        # Add chaotic noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise