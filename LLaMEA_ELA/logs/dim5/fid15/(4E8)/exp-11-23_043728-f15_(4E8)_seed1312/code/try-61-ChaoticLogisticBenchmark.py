import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # High-dimensional chaotic system with fractal characteristics
        self.r = 3.999
        self.epsilon = 0.2
        self.fractal_dim = 1.7
        
    def f(self, x):
        # Normalize input to [-1, 1] range with adaptive scaling
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Initialize chaotic sequence with fractal dimension coupling
        chaotic_seq = np.zeros(self.dim)
        chaotic_seq[0] = x_norm[0]
        
        # Generate multi-scale chaotic sequence with seventh-order polynomial coupling
        for i in range(1, self.dim):
            # Fractal chaotic dynamics with dynamic coupling and seventh-order nonlinearity
            base_term = self.r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1]**6)
            coupling_term = self.epsilon * (x_norm[i] - chaotic_seq[i-1])
            poly_term = 0.05 * chaotic_seq[i-1]**7
            
            # Dynamic dimension weighting based on fractal characteristics
            weight = np.sin(np.pi * i / self.dim) ** self.fractal_dim
            chaotic_seq[i] = base_term + coupling_term + poly_term + 0.02 * weight * np.sin(10 * chaotic_seq[i-1])
        
        # Ensure boundedness with fractal constraints
        chaotic_seq = np.clip(chaotic_seq, -3, 3)
        
        # Multi-fractal periodic structure with adaptive frequency components
        freq_weights = np.linspace(1, 8, self.dim)
        period_pattern = np.sum(np.sin(freq_weights * np.pi * x_norm) * np.cos(freq_weights * np.pi * x_norm))
        
        # Combined energy landscape with multi-scale interactions
        total_energy = (np.sum(chaotic_seq**2) + 
                       0.5 * period_pattern**2 + 
                       0.2 * np.sum((chaotic_seq[1:] - chaotic_seq[:-1])**2) +
                       0.1 * np.sum(np.diff(chaotic_seq, n=2)**2) +
                       0.05 * np.sum(chaotic_seq**4))
        
        # Add dynamic noise with fractal characteristics
        noise = 0.02 * np.random.rand() * (1 + 0.5 * np.sin(np.pi * self.dim / 10))
        
        return total_energy + noise