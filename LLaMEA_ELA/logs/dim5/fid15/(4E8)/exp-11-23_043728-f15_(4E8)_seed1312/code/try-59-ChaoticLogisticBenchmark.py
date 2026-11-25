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
        
        # Generate coupled chaotic sequence using logistic map with septic nonlinearity
        for i in range(1, self.dim):
            # Coupled logistic maps with septic term and adaptive interaction
            chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**6) + \
                            self.epsilon * (x_norm[i] - chaotic_seq[i-1]) + \
                            0.02 * chaotic_seq[i-1]**7
            
            # Adaptive coupling strength based on dimension index
            adaptive_coupling = 0.01 * i / self.dim
            chaotic_seq[i] += adaptive_coupling * (x_norm[i] - x_norm[i-1])
        
        # Ensure boundedness and prevent overflow
        chaotic_seq = np.clip(chaotic_seq, -2, 2)
        
        # Create multi-frequency periodic attractor pattern
        period_pattern = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) + 
                               np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Combine chaotic dynamics with periodic structure and additional coupling
        total_energy = np.sum(chaotic_seq**2) + 0.4 * period_pattern**2 + \
                      0.15 * np.sum((chaotic_seq[1:] - chaotic_seq[:-1])**2) + \
                      0.05 * np.sum(np.abs(chaotic_seq[1:] - chaotic_seq[:-1]))
        
        # Add small noise to create ruggedness
        noise = 0.01 * np.random.rand()
        
        return total_energy + noise