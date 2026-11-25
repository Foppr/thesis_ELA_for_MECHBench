import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize logistic map parameters with increased nonlinearity and dynamic coupling
        self.r = 3.999
        self.epsilon = 0.2
        self.gamma = 0.05
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Initialize chaotic sequence with first dimension
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = x_norm[0]
        
        # Generate coupled chaotic sequence using logistic map with octic nonlinearity and dynamic coupling
        for i in range(1, self.dim):
            # Dynamic coupling with adaptive interaction strength
            coupling_strength = 0.5 + 0.3 * np.sin(0.5 * i)
            chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**7) + \
                            self.epsilon * (x_norm[i] - chaotic_seq[i-1]) * coupling_strength + \
                            self.gamma * np.sin(3 * np.pi * chaotic_seq[i-1]) * (1 - chaotic_seq[i-1]**8)
        
        # Ensure boundedness and prevent overflow
        chaotic_seq = np.clip(chaotic_seq, -3, 3)
        
        # Create multi-scale periodic attractor pattern using trigonometric functions with varying frequencies
        period_pattern = np.sum(np.sin(9 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm)) + \
                        0.5 * np.sum(np.sin(11 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Combine chaotic dynamics with periodic structure and additional coupling
        total_energy = np.sum(chaotic_seq**2) + 0.5 * period_pattern**2 + \
                      0.2 * np.sum((chaotic_seq[1:] - chaotic_seq[:-1])**2) + \
                      0.05 * np.sum(np.abs(chaotic_seq[1:] - chaotic_seq[:-1]))
        
        # Add small noise to create ruggedness
        noise = 0.02 * np.random.rand()
        
        # Introduce a new fitness structure that penalizes algorithmic bias
        # by incorporating a modified quadratic penalty term based on dimensionality and interaction
        penalty = 0.1 * self.dim * np.mean((x_norm - np.mean(x_norm))**2) + \
                 0.05 * np.sum(np.abs(x_norm[1:] - x_norm[:-1]))
        
        # Add adaptive scaling factor based on dimensionality with exponential growth
        adaptive_scale = 1.0 + 0.03 * np.log(self.dim + 1) + 0.005 * self.dim**1.5
        
        # Introduce multiple basins of attraction through a hybrid fitness aggregation
        basin_penalty = 0.1 * np.sum(np.abs(chaotic_seq - np.mean(chaotic_seq))**3)
        
        return adaptive_scale * (total_energy + noise + penalty + basin_penalty)