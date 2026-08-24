import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum-inspired chaotic sequence with superposition states
        self.quantum_seq = np.array([0.5])
        for i in range(dim * 20):
            next_val = 4 * self.quantum_seq[-1] * (1 - self.quantum_seq[-1])
            self.quantum_seq = np.append(self.quantum_seq, next_val)
        self.quantum_seq = self.quantum_seq[:dim]
        
        # Precompute dynamic basin boundaries
        self.basin_centers = np.random.uniform(-5.0, 5.0, (dim, 5))
        self.basin_weights = np.random.uniform(0.5, 2.0, 5)
        
        # Adaptive noise parameters
        self.noise_scale = np.random.uniform(0.1, 0.5, dim)
        self.noise_freq = np.random.uniform(1.0, 5.0, dim)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quantum superposition RBFs with phase modulation
        rbf_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.quantum_seq[i])**2)
            phase = np.sin(self.quantum_seq[i] * np.pi * 2)
            weight = np.abs(phase) * 0.5 + 0.5
            rbf_sum += weight * np.exp(-dist / (2 * 0.02**2))
        
        # Dynamic basin landscape with quantum interference
        basin_sum = 0.0
        for i in range(5):
            dists = np.sum((x_norm.reshape(-1, 1) - self.basin_centers[:, i])**2, axis=0)
            basin_sum += self.basin_weights[i] * np.exp(-dists / (2 * 0.1**2))
        
        # Adaptive noise with quantum frequency modulation
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_scale[i] * np.sin(x_norm[i] * self.noise_freq[i] * np.pi) * np.random.random()
        
        # Chaotic polynomial with quantum coupling
        poly_term = 0.0
        for i in range(self.dim):
            x_i = x_norm[i]
            poly_term += (x_i**3 + 0.3 * x_i**5 + 0.05 * x_i**7) * np.sin(self.quantum_seq[i] * np.pi)
        
        # Sharp quantum transition zones
        transition_zones = 0.0
        for i in range(self.dim):
            transition_zones += np.abs(np.sin(x_norm[i] * np.pi * 3)) > 0.8
        
        # Quantum interference pattern
        interference = np.sum(np.sin(x_norm * self.quantum_seq) * np.cos(x_norm * self.quantum_seq))
        
        # Combine all components with quantum weights
        total = 0.25 * rbf_sum + 0.2 * basin_sum + 0.15 * noise + 0.2 * poly_term + 0.1 * transition_zones + 0.1 * interference
        
        # Add quantum scaling factor
        quantum_scale = 1 + 0.3 * np.sin(np.sum(x_norm**3))
        
        return total * quantum_scale