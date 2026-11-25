import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.r1 = 3.99
        self.r2 = 3.85
        self.epsilon = 0.2
        self.fractal_dim = 1.7
        
    def f(self, x):
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Hyperchaotic sequence with two coupled logistic maps
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = x_norm[0]
        chaotic_seq[1] = x_norm[1]
        
        for i in range(2, self.dim):
            # Coupled hyperchaotic maps with fractal coupling
            chaotic_seq[i] = (self.r1 * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**2) + 
                             self.r2 * chaotic_seq[i-2] * (1 - chaotic_seq[i-2]**2) +
                             self.epsilon * (x_norm[i] - chaotic_seq[i-1]) +
                             0.03 * np.sin(self.fractal_dim * np.pi * chaotic_seq[i-1]))
        
        # Bounded hyperchaotic sequence
        chaotic_seq = np.clip(chaotic_seq, -3, 3)
        
        # Fractal periodic pattern with multiple frequencies
        period_pattern = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * 
                               np.sin(2 * np.pi * x_norm**3))
        
        # Adaptive scaling with fractal dimensionality
        adaptive_scale = 1.0 + 0.2 * np.log(self.dim + 1) + 0.05 * np.sin(np.pi * self.fractal_dim)
        
        # Multi-scale energy combining chaotic, periodic, and coupling terms
        total_energy = (np.sum(chaotic_seq**3) + 
                       0.4 * period_pattern**2 + 
                       0.15 * np.sum((chaotic_seq[1:] - chaotic_seq[:-1])**3) * adaptive_scale +
                       0.08 * np.sum(np.abs(chaotic_seq)**1.5))
        
        # Add fractal noise with self-similar structure
        noise = 0.02 * np.random.rand() * (1 + 0.1 * np.sin(self.fractal_dim * np.pi * np.sum(x_norm**2)))
        
        # Dimensionally adaptive penalty with hyperbolic scaling
        penalty = 0.002 * self.dim * np.sum(np.abs(x_norm)**(1.3))
        
        # Add global correlation term to increase multimodality
        correlation_term = 0.05 * np.sum((x_norm - np.mean(x_norm))**2)
        
        return total_energy + noise + penalty + correlation_term