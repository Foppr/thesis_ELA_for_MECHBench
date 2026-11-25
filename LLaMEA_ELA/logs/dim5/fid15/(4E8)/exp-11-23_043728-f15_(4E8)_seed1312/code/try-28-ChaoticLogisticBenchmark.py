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
        
        # Generate coupled chaotic sequence using logistic map with cubic nonlinearity
        for i in range(1, self.dim):
            # Coupled logistic maps with cubic term and interaction
            chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**2) + \
                            self.epsilon * (x_norm[i] - chaotic_seq[i-1]) + \
                            0.05 * chaotic_seq[i-1]**3
        
        # Ensure boundedness and prevent overflow
        chaotic_seq = np.clip(chaotic_seq, -2, 2)
        
        # Create periodic attractor pattern using trigonometric functions with higher frequency
        period_pattern = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Combine chaotic dynamics with periodic structure and additional coupling
        total_energy = np.sum(chaotic_seq**2) + 0.3 * period_pattern**2 + \
                      0.1 * np.sum((chaotic_seq[1:] - chaotic_seq[:-1])**2)
        
        # Add small noise to create ruggedness
        noise = 0.01 * np.random.rand()
        
        return total_energy + noise