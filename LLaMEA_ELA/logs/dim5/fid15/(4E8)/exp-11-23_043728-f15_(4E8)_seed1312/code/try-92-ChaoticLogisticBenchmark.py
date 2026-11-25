import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Increased nonlinearity with 16th-order terms and enhanced coupling
        self.r = 3.9999
        self.epsilon = 0.35
        self.gamma = 0.12
        self.beta = 0.04
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Initialize chaotic sequence with first dimension
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = x_norm[0]
        
        # Generate coupled chaotic sequence using logistic map with 16th-order nonlinearity and dynamic coupling
        for i in range(1, self.dim):
            # Dynamic coupling with enhanced interaction strength
            coupling_strength = 0.7 + 0.3 * np.sin(0.8 * i + 0.5 * np.cos(1.2 * i))
            chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**15) + \
                            self.epsilon * (x_norm[i] - chaotic_seq[i-1]) * coupling_strength + \
                            self.gamma * np.sin(4 * np.pi * chaotic_seq[i-1]) * (1 - chaotic_seq[i-1]**16) + \
                            self.beta * np.cos(2 * np.pi * chaotic_seq[i-1]) * np.sin(3 * np.pi * chaotic_seq[i-1])
        
        # Ensure boundedness and prevent overflow
        chaotic_seq = np.clip(chaotic_seq, -4, 4)
        
        # Create multi-scale fractal-like attractor pattern using trigonometric functions with varying frequencies
        fractal_pattern = np.sum(np.sin(13 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm)) + \
                         0.6 * np.sum(np.sin(15 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm)) + \
                         0.3 * np.sum(np.sin(17 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm))
        
        # Combine chaotic dynamics with fractal structure and additional coupling
        total_energy = np.sum(chaotic_seq**2) + 0.6 * fractal_pattern**2 + \
                      0.3 * np.sum((chaotic_seq[1:] - chaotic_seq[:-1])**2) + \
                      0.1 * np.sum(np.abs(chaotic_seq[1:] - chaotic_seq[:-1]))
        
        # Add quantum-inspired interference noise
        interference = 0.02 * np.random.rand() * np.prod(np.sin(np.pi * x_norm / 2))
        
        # Introduce enhanced penalty term based on dimensionality and interaction
        penalty = 0.15 * self.dim * np.mean((x_norm - np.mean(x_norm))**2) + \
                 0.1 * np.sum(np.abs(x_norm[1:] - x_norm[:-1])) + \
                 0.08 * np.sum(np.abs(chaotic_seq)**3)
        
        # Add adaptive scaling factor with exponential growth and fractal components
        adaptive_scale = 1.0 + 0.06 * np.log(self.dim + 1) + 0.012 * self.dim**1.7 + \
                        0.005 * np.sum(np.sin(np.pi * x_norm)**2)
        
        # Introduce multiple basins of attraction through hybrid fitness aggregation
        basin_penalty = 0.2 * np.sum(np.abs(chaotic_seq - np.mean(chaotic_seq))**4) + \
                       0.1 * np.sum(np.abs(chaotic_seq - np.median(chaotic_seq))**3)
        
        # Add correlation-based bias correction with fractal dimension
        correlation_bias = 0.03 * np.abs(np.corrcoef(x_norm[:-1], x_norm[1:])[0,1]) + \
                          0.02 * np.std(np.diff(x_norm))
        
        # Add quantum-inspired phase interference term
        phase_term = 0.04 * np.prod(np.cos(np.pi * x_norm / 4)) + \
                    0.03 * np.sum(np.sin(np.pi * x_norm)**2)
        
        return adaptive_scale * (total_energy + interference + penalty + basin_penalty + correlation_bias + phase_term)