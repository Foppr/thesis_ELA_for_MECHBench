import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize logistic map parameters with increased nonlinearity and dynamic coupling
        self.r = 3.995
        self.epsilon = 0.3
        self.gamma = 0.06
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Initialize chaotic sequence with first dimension
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = x_norm[0]
        
        # Generate coupled chaotic sequence using logistic map with septic nonlinearity and dynamic coupling
        for i in range(1, self.dim):
            # Dynamic coupling with adaptive interaction strength
            coupling_strength = 0.5 + 0.3 * np.cos(0.5 * i)
            chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**6) + \
                            self.epsilon * (x_norm[i] - chaotic_seq[i-1]) * coupling_strength + \
                            self.gamma * np.cos(4 * np.pi * chaotic_seq[i-1]) * (1 - chaotic_seq[i-1]**7)
        
        # Ensure boundedness and prevent overflow
        chaotic_seq = np.clip(chaotic_seq, -2.5, 2.5)
        
        # Create multi-scale periodic attractor pattern using trigonometric functions with varying frequencies
        period_pattern = np.sum(np.cos(8 * np.pi * x_norm) * np.sin(4 * np.pi * x_norm)) + \
                        0.6 * np.sum(np.cos(10 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm))
        
        # Combine chaotic dynamics with periodic structure and additional coupling
        total_energy = np.sum(chaotic_seq**2) + 0.4 * period_pattern**2 + \
                      0.25 * np.sum((chaotic_seq[1:] - chaotic_seq[:-1])**2) + \
                      0.08 * np.sum(np.abs(chaotic_seq[1:] - chaotic_seq[:-1]))
        
        # Add small noise to create ruggedness
        noise = 0.02 * np.random.rand()
        
        # Introduce a new fitness structure that penalizes algorithmic bias
        # by incorporating a modified quadratic penalty term based on dimensionality and interaction
        penalty = 0.12 * self.dim * np.mean((x_norm - np.mean(x_norm))**2) + \
                 0.07 * np.sum(np.abs(x_norm[1:] - x_norm[:-1]))
        
        # Add adaptive scaling factor based on dimensionality with exponential growth
        adaptive_scale = 1.0 + 0.05 * np.log(self.dim + 1) + 0.01 * self.dim**1.4
        
        # Introduce multiple basins of attraction through a hybrid fitness aggregation
        basin_penalty = 0.2 * np.sum(np.abs(chaotic_seq - np.mean(chaotic_seq))**2.5)
        
        # Add correlation-based bias correction term to reduce statistical bias
        correlation_bias = 0.03 * np.abs(np.corrcoef(x_norm[:-1], x_norm[1:])[0,1])
        
        return adaptive_scale * (total_energy + noise + penalty + basin_penalty + correlation_bias)