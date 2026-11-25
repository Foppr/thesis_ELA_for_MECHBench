import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize logistic map parameters with increased nonlinearity
        self.r = 4.02
        self.epsilon = 0.18
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Initialize chaotic sequence with first dimension
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = x_norm[0]
        
        # Generate coupled chaotic sequence using logistic map with nonic nonlinearity
        for i in range(1, self.dim):
            # Coupled logistic maps with nonic term and interaction
            chaotic_seq[i] = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**8) + \
                            self.epsilon * (x_norm[i] - chaotic_seq[i-1]) + \
                            0.03 * chaotic_seq[i-1]**9
            
            # Add dynamic coupling based on distance to previous values
            if i > 1:
                chaotic_seq[i] += 0.015 * (chaotic_seq[i-1] - chaotic_seq[i-2])**4
        
        # Ensure boundedness and prevent overflow
        chaotic_seq = np.clip(chaotic_seq, -2, 2)
        
        # Create fractal-like energy distribution using multi-scale sinusoidal patterns
        fractal_energy = np.sum(np.sin(17 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm) + 
                               0.35 * np.sin(34 * np.pi * x_norm)**2)
        
        # Add quantum-inspired interference patterns
        quantum_pattern = np.sum(np.sin(9 * np.pi * chaotic_seq) * np.cos(7 * np.pi * chaotic_seq))
        
        # Create multi-modal structure with multiple basins of attraction using higher-order polynomials
        basin_structure = np.sum(np.sin(6 * np.pi * chaotic_seq)**4 + 
                               0.75 * np.cos(4 * np.pi * chaotic_seq)**3)
        
        # Combine chaotic dynamics with fractal structure and quantum interference
        total_energy = np.sum(chaotic_seq**2) + 0.65 * fractal_energy**2 + \
                      0.28 * np.sum((chaotic_seq[1:] - chaotic_seq[:-1])**2) + \
                      0.32 * basin_structure + 0.12 * quantum_pattern
        
        # Add small noise to create ruggedness
        noise = 0.012 * np.random.rand()
        
        # Introduce a new fitness structure that penalizes algorithmic bias
        # by incorporating a modified quadratic penalty term based on dimensionality
        penalty = 0.18 * self.dim * np.mean((x_norm - np.mean(x_norm))**2)
        
        # Add adaptive scaling factor based on dimensionality
        adaptive_scale = 1.0 + 0.04 * np.log(self.dim + 1)
        
        # Add interaction terms between distant dimensions to increase complexity
        interaction_term = 0.1 * np.sum((x_norm[::2] - x_norm[3::2])**4)
        
        # Add fractal dimension coupling for enhanced multimodality
        fractal_coupling = 0.06 * np.sum(np.sin(14 * np.pi * x_norm[::2]) * np.cos(10 * np.pi * x_norm[1::2]))
        
        return adaptive_scale * (total_energy + noise + penalty + interaction_term + fractal_coupling)