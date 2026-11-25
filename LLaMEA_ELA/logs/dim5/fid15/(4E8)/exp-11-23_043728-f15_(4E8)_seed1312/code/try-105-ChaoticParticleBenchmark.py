import numpy as np

class ChaoticParticleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.chaos_factor = 3.8
        self.particle_count = max(5, dim // 2)
        self.temporal_freq_base = 2.0
        self.spectral_entropy_weight = 0.7
        self.ruggedness_scaling = 1.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Generate chaotic particle interactions
        particle_positions = np.zeros((self.particle_count, self.dim))
        for i in range(self.particle_count):
            seed = i * 100 + self.dim
            np.random.seed(seed)
            particle_positions[i] = np.random.uniform(-1, 1, self.dim)
        
        # Compute particle-based fitness with chaotic dynamics
        interaction_energy = 0.0
        for i in range(self.particle_count):
            pos_i = particle_positions[i]
            for j in range(i + 1, self.particle_count):
                pos_j = particle_positions[j]
                distance = np.linalg.norm(pos_i - pos_j)
                # Chaotic interaction potential
                interaction_energy += 1.0 / (distance**2 + 0.1) * \
                                    np.sin(self.chaos_factor * distance) * \
                                    np.cos(self.chaos_factor * distance * 0.5)
        
        # Temporal frequency modulation across dimensions
        temporal_modulation = 0.0
        for i in range(self.dim):
            freq = self.temporal_freq_base * (i + 1)
            temporal_modulation += np.sin(freq * x_norm[i]) * \
                                 np.cos(freq * x_norm[i] * 0.7) * \
                                 np.sin(freq * x_norm[i] * 1.3)
        
        # Spectral entropy based on frequency components
        spectral_entropy = 0.0
        for i in range(self.dim):
            # Compute DFT-like features
            freq_components = np.array([np.sin((j + 1) * x_norm[i]) for j in range(8)])
            prob_dist = np.abs(freq_components)**2
            prob_dist = prob_dist / (np.sum(prob_dist) + 1e-8)
            spectral_entropy += -np.sum(prob_dist * np.log(prob_dist + 1e-8))
        
        # Ruggedness scaling based on dimensionality
        ruggedness_factor = self.ruggedness_scaling * np.log(self.dim + 1)
        
        # Combine all components with adaptive weighting
        base_fitness = np.sum(x_norm**4) + temporal_modulation + interaction_energy
        entropy_contribution = self.spectral_entropy_weight * spectral_entropy
        
        # Add dimensionality-dependent penalty and scaling
        dim_penalty = 0.3 * self.dim * np.mean(np.abs(x_norm)**1.5)
        
        return base_fitness * ruggedness_factor + entropy_contribution + dim_penalty