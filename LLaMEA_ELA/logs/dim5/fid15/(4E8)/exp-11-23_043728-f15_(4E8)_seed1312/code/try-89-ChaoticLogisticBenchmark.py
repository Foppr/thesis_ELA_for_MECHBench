import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize logistic map parameters with increased nonlinearity
        self.r = 3.98
        self.epsilon = 0.15
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Initialize chaotic sequence with first dimension
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = x_norm[0]
        
        # Generate coupled chaotic sequence using logistic map with octic nonlinearity
        for i in range(1, self.dim):
            # Coupled logistic maps with octic term and interaction
            chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**7) + \
                            self.epsilon * (x_norm[i] - chaotic_seq[i-1]) + \
                            0.025 * chaotic_seq[i-1]**8
            
            # Add dynamic coupling based on distance to previous values
            if i > 1:
                chaotic_seq[i] += 0.01 * (chaotic_seq[i-1] - chaotic_seq[i-2])**3
        
        # Ensure boundedness and prevent overflow
        chaotic_seq = np.clip(chaotic_seq, -2, 2)
        
        # Create periodic attractor pattern using trigonometric functions with higher frequency
        period_pattern = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Add multi-modal structure with multiple basins of attraction
        basin_structure = np.sum(np.sin(5 * np.pi * chaotic_seq)**2 + 
                               0.5 * np.cos(3 * np.pi * chaotic_seq)**2)
        
        # Combine chaotic dynamics with periodic structure and additional coupling
        total_energy = np.sum(chaotic_seq**2) + 0.4 * period_pattern**2 + \
                      0.15 * np.sum((chaotic_seq[1:] - chaotic_seq[:-1])**2) + \
                      0.2 * basin_structure
        
        # Add small noise to create ruggedness
        noise = 0.01 * np.random.rand()
        
        # Introduce a new fitness structure that penalizes algorithmic bias
        # by incorporating a modified quadratic penalty term based on dimensionality
        penalty = 0.1 * self.dim * np.mean((x_norm - np.mean(x_norm))**2)
        
        # Add adaptive scaling factor based on dimensionality
        adaptive_scale = 1.0 + 0.02 * np.log(self.dim + 1)
        
        # Add interaction terms between distant dimensions to increase complexity
        interaction_term = 0.05 * np.sum((x_norm[::2] - x_norm[1::2])**4)
        
        return adaptive_scale * (total_energy + noise + penalty + interaction_term)