import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize logistic map parameters
        self.r = 3.95
        self.epsilon = 0.1
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Initialize chaotic sequence with first dimension
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = x_norm[0]
        
        # Generate coupled chaotic sequence using logistic map
        for i in range(1, self.dim):
            # Coupled logistic maps with interaction term
            chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]) + \
                            self.epsilon * (x_norm[i] - chaotic_seq[i-1])
        
        # Ensure boundedness and prevent overflow
        chaotic_seq = np.clip(chaotic_seq, -2, 2)
        
        # Create periodic attractor pattern using trigonometric functions
        period_pattern = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Combine chaotic dynamics with periodic structure
        total_energy = np.sum(chaotic_seq**2) + 0.5 * period_pattern**2
        
        # Add small noise to create ruggedness
        noise = 0.01 * np.random.rand()
        
        return total_energy + noise