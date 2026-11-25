import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.r = 3.995
        self.epsilon = 0.2
        
    def f(self, x):
        x_norm = np.clip(x / 5.0, -1, 1)
        
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = x_norm[0]
        
        for i in range(1, self.dim):
            # Enhanced septic chaos with trigonometric coupling
            chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**7) + \
                            self.epsilon * np.sin(3 * np.pi * (x_norm[i] - chaotic_seq[i-1])) + \
                            0.03 * np.cos(5 * np.pi * chaotic_seq[i-1]) * chaotic_seq[i-1]**8
            
            # Multi-scale adaptive coupling with dimension-dependent weights
            scale_factor = 0.02 * (i / self.dim)**2
            chaotic_seq[i] += scale_factor * (x_norm[i] - x_norm[i-1]) * np.exp(-0.5 * (i / self.dim)**2)
            
            # Cross-dimensional energy interaction
            if i > 1:
                chaotic_seq[i] += 0.01 * (chaotic_seq[i-1] - chaotic_seq[i-2]) * np.sin(2 * np.pi * i / self.dim)
        
        chaotic_seq = np.clip(chaotic_seq, -3, 3)
        
        # Multi-scale periodic modulation with varying frequencies
        period_pattern = np.sum(
            np.sin(9 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) + 
            np.sin(5 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) +
            0.5 * np.sin(11 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm)
        )
        
        # Energy aggregation with multi-component fitness
        total_energy = (
            np.sum(chaotic_seq**3) + 
            0.5 * period_pattern**3 +
            0.2 * np.sum((chaotic_seq[1:] - chaotic_seq[:-1])**3) +
            0.1 * np.sum(np.abs(chaotic_seq[1:] - chaotic_seq[:-1])**1.5) +
            0.05 * np.sum(chaotic_seq**4)
        )
        
        # Add complex noise structure
        noise = 0.02 * np.random.rand() * (1 + 0.5 * np.sin(10 * np.pi * np.sum(x_norm)))
        
        return total_energy + noise