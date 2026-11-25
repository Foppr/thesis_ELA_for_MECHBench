import numpy as np

class ChaoticEllipticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic coupling parameters with fractal sine-wave interactions
        self.fractal_amplitudes = np.logspace(1.2, 3.8, min(15, dim)) * 1.3
        self.fractal_frequencies = np.logspace(0.8, 2.5, min(15, dim)) * 1.5
        # Dynamic conditioning gradients with elliptic curvature modifications
        self.elliptic_curvatures = np.linspace(1.0, 4.0, min(12, dim)) * 1.2
        # Cross-dimensional interaction patterns with increased coupling strength
        self.coupling_strengths = np.random.uniform(1.0, 3.5, min(10, dim)) * 1.4
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Enhanced chaotic coupling with fractal sine-wave interactions
        chaotic_term = 0.0
        for i in range(min(len(self.fractal_amplitudes), self.dim)):
            amp = self.fractal_amplitudes[i]
            freq = self.fractal_frequencies[i]
            # Fractal sine-wave interaction with chaotic modulation
            chaotic_val = amp * np.sin(freq * x_norm[i]) * np.exp(-0.5 * x_norm[i] ** 2) + \
                          0.5 * np.sin(3.0 * freq * x_norm[i]) * np.cos(2.0 * x_norm[i])
            chaotic_term += chaotic_val
            
        # Dynamic conditioning with elliptic curvature modifications
        conditioning_term = 0.0
        for i in range(min(len(self.elliptic_curvatures), self.dim)):
            curvature = self.elliptic_curvatures[i]
            # Enhanced elliptic curvature with exponential and trigonometric modulation
            cond_val = curvature * (x_norm[i] ** 2) * np.exp(-0.3 * x_norm[i] ** 2) + \
                       0.3 * np.sin(2.0 * x_norm[i]) * np.cos(x_norm[i])
            conditioning_term += cond_val
            
        # Cross-dimensional interaction with increased coupling strength
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Enhanced coupling with phase modulation and dynamic strength
                coupling_strength = self.coupling_strengths[i % len(self.coupling_strengths)]
                phase_shift = np.pi * (i * j) / (self.dim + 2)
                interaction_val = coupling_strength * x_norm[i] * x_norm[j] * \
                                 np.sin(phase_shift + 1.5 * x_norm[i] + 0.8 * x_norm[j])
                interaction_term += interaction_val
                
        # Multi-scale clustering with chaotic positioning and irregular spacing
        cluster_term = 0.0
        for i in range(self.dim):
            # Chaotic cluster positioning with irregular separation distances
            cluster_pos = 2.0 * np.sin(0.7 * (i + 1) * np.pi / self.dim) * \
                          np.exp(-0.2 * (i + 1))
            distance = x_norm[i] - cluster_pos
            # Chaotic clustering with higher-order polynomial and exponential terms
            cluster_val = 1.5 * (distance ** 4) + 0.8 * (distance ** 6) + \
                          0.3 * (distance ** 8) + 0.1 * np.exp(-2.0 * distance ** 2)
            cluster_term += cluster_val
            
        # Combined terms with adjusted weights for extreme landscape characteristics
        result = 1.3 * chaotic_term + 1.1 * conditioning_term + 0.9 * interaction_term + 0.8 * cluster_term
        
        # Add enhanced adaptive noise with increased dimensionality-dependent amplitude
        noise_amplitude = 0.05 * (1.0 + 0.12 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise