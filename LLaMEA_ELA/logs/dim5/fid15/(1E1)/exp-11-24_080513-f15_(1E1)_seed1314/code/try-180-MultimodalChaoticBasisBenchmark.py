import numpy as np

class MultimodalChaoticBasisBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for temporal variation
        self.chaos_seq = np.zeros(100)
        r = 3.9
        x = 0.5
        for i in range(100):
            x = r * x * (1 - x)
            self.chaos_seq[i] = x
            
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic modulation
        rbfs = 0.0
        for i in range(self.dim):
            center = np.sin(i * 0.5) * 0.8
            sigma = 0.3 + 0.2 * np.sin(i * 0.3)
            # Chaotic scaling factor
            chaos_factor = self.chaos_seq[i % len(self.chaos_seq)]
            rbfs += np.exp(-sigma * (x_norm[i] - center)**2) * (1 + 0.2 * chaos_factor)
        
        # Temporal chaos component with phase shifting
        temporal = 0.0
        for i in range(self.dim):
            phase = i * 0.2 + self.chaos_seq[(i*7) % len(self.chaos_seq)]
            temporal += np.sin(x_norm[i] * 10 + phase) * np.cos(x_norm[i] * 7 + phase)
        
        # Semantic symmetry breaking with polynomial interactions
        symmetry_break = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Polynomial interaction with chaotic weight
                poly_weight = 1.0 + 0.3 * self.chaos_seq[(i+j) % len(self.chaos_seq)]
                symmetry_break += poly_weight * (x_norm[i]**2) * (x_norm[j]**3)
        
        # Noise sensitivity component with varying amplitude
        noise_sens = 0.0
        for i in range(self.dim):
            # Add chaotic noise with amplitude modulation
            noise_amp = 0.1 + 0.2 * np.sin(i * 0.4)
            noise_val = np.random.normal(0, noise_amp)
            noise_sens += x_norm[i]**4 + noise_val
            
        # Multi-scale harmonic interference
        harmonic = 0.0
        for i in range(self.dim):
            for k in range(1, 6):
                harmonic += np.sin(k * x_norm[i]) * np.cos(k * x_norm[i] * 0.5) * (1 + 0.1 * self.chaos_seq[k % len(self.chaos_seq)])
        
        # Combined fitness with dynamic weighting
        total = (0.3 * rbfs + 0.25 * temporal + 0.2 * symmetry_break + 
                0.15 * noise_sens + 0.1 * harmonic)
        
        # Add global scaling and offset for better conditioning
        return total * (1.0 + 0.1 * np.sum(x_norm**2))