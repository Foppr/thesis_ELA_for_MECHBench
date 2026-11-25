import numpy as np

class HarmonicSaddleInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Harmonic pattern parameters
        self.harmonic_freqs = np.linspace(1.0, 8.0, dim) * 1.2
        self.amplitude_scales = np.logspace(0.5, 2.0, dim) * 0.8
        # Adaptive conditioning gradients
        self.conditioning_strengths = np.logspace(0.3, 1.8, dim) * 2.5
        # Saddle-point interference parameters
        self.saddle_amplitudes = np.random.uniform(0.5, 3.0, dim) * 1.5
        self.saddle_frequencies = np.random.uniform(0.8, 4.0, dim) * 1.2
        # Dynamic coupling between dimensions
        self.coupling_matrix = np.random.randn(dim, dim) * 0.3
        # Cluster positioning for optima distribution
        self.cluster_centers = np.random.uniform(-3.0, 3.0, dim) * 1.1
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Periodic harmonic terms with varying frequencies and amplitudes
        harmonic_term = 0.0
        for i in range(self.dim):
            freq = self.harmonic_freqs[i]
            amp = self.amplitude_scales[i]
            # Harmonic components with phase shifts
            phase_shift = 0.5 * np.pi * (i + 1) / self.dim
            harmonic_val = amp * np.sin(freq * x_norm[i] + phase_shift) ** 2
            harmonic_term += harmonic_val
            
        # Adaptive conditioning with gradient modulation
        conditioning_term = 0.0
        for i in range(self.dim):
            cond_strength = self.conditioning_strengths[i]
            # Quadratic conditioning with adaptive scaling
            quad_term = cond_strength * x_norm[i] ** 2
            # Add harmonic modulation to conditioning
            mod_factor = 1.0 + 0.3 * np.sin(2.0 * x_norm[i])
            conditioning_term += quad_term * mod_factor
            
        # Saddle-point interference with dynamic coupling
        saddle_term = 0.0
        for i in range(self.dim):
            amp = self.saddle_amplitudes[i]
            freq = self.saddle_frequencies[i]
            # Saddle point with interference from other dimensions
            saddle_val = amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
            # Coupling effect from other dimensions
            coupling_effect = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_effect += self.coupling_matrix[i, j] * x_norm[j]
            saddle_val *= (1.0 + 0.2 * coupling_effect)
            saddle_term += saddle_val
            
        # Cluster-based optima positioning with harmonic interference
        cluster_term = 0.0
        for i in range(self.dim):
            center = self.cluster_centers[i]
            # Distance from cluster center with periodic modulation
            distance = x_norm[i] - center
            # Polynomial cluster shape with harmonic perturbations
            cluster_val = (distance ** 4) + 0.5 * (distance ** 6) + 0.1 * np.sin(3.0 * distance)
            cluster_term += cluster_val
            
        # Combine all terms with dynamic weights
        result = 1.2 * harmonic_term + 1.0 * conditioning_term + 0.8 * saddle_term + 0.9 * cluster_term
        
        # Add stochastic noise with periodic characteristics
        noise_amplitude = 0.02 * (1.0 + 0.05 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise