import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize logistic map parameters with increased nonlinearity
        self.r = 3.99
        self.epsilon = 0.15
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Initialize chaotic sequence with first dimension
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = x_norm[0]
        
        # Generate coupled chaotic sequence using logistic map with quintic nonlinearity
        for i in range(1, self.dim):
            # Coupled logistic maps with quintic term and interaction
            chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**4) + \
                            self.epsilon * (x_norm[i] - chaotic_seq[i-1]) + \
                            0.03 * chaotic_seq[i-1]**5
        
        # Ensure boundedness and prevent overflow
        chaotic_seq = np.clip(chaotic_seq, -2, 2)
        
        # Create periodic attractor pattern using trigonometric functions with higher frequency
        period_pattern = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Combine chaotic dynamics with periodic structure and additional coupling
        total_energy = np.sum(chaotic_seq**2) + 0.4 * period_pattern**2 + \
                      0.15 * np.sum((chaotic_seq[1:] - chaotic_seq[:-1])**2)
        
        # Add small noise to create ruggedness
        noise = 0.01 * np.random.rand()
        
        # Introduce a new fitness structure that penalizes algorithmic bias
        # by incorporating a modified quadratic penalty term based on dimensionality
        penalty = 0.08 * self.dim * np.mean((x_norm - np.mean(x_norm))**2)
        
        # Add adaptive scaling factor based on dimensionality
        adaptive_scale = 1.0 + 0.02 * np.log(self.dim + 1)
        
        return adaptive_scale * (total_energy + noise + penalty)