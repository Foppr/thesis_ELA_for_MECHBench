import numpy as np

class ChaoticRotationalSpectralLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic logistic map parameters
        self.logistic_r = 3.95 + 0.1 * np.random.rand(dim)
        # Precompute quaternion rotation components
        self.quat_coeffs = np.random.uniform(-1, 1, (dim, 4))
        # Precompute spectral frequency patterns
        self.spectral_freqs = 1.0 + 4.0 * np.random.rand(dim)
        self.spectral_amps = 0.5 + 2.0 * np.random.rand(dim)
        # Precompute cross-dimensional coupling matrices
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Precompute dynamic conditioning weights
        self.condition_weights = 0.5 + 1.5 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map component with dynamic parameters
        logistic_sum = 0.0
        for i in range(self.dim):
            x_i = x_norm[i]
            r = self.logistic_r[i]
            # Logistic map iteration with initial condition
            x_prev = 0.5 + 0.1 * np.random.rand()
            for _ in range(5):
                x_prev = r * x_prev * (1 - x_prev)
            logistic_sum += x_prev * np.exp(-0.1 * x_i**2)
        
        # Quaternion-based rotational component
        quat_sum = 0.0
        for i in range(self.dim):
            coeffs = self.quat_coeffs[i]
            # Simple quaternion-like rotation effect
            rot_val = coeffs[0] * x_norm[i]**2 + coeffs[1] * x_norm[i] + coeffs[2] * np.sin(x_norm[i]) + coeffs[3] * np.cos(x_norm[i])
            quat_sum += rot_val * np.exp(-0.15 * x_norm[i]**2)
        
        # Spectral frequency interference component
        spectral_sum = 0.0
        for i in range(self.dim):
            freq = self.spectral_freqs[i]
            amp = self.spectral_amps[i]
            spectral_sum += amp * np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * np.exp(-0.05 * x_norm[i]**2)
        
        # Cross-dimensional coupling with matrix operations
        coupling_sum = 0.0
        for i in range(self.dim):
            dot_prod = 0.0
            for j in range(self.dim):
                if i != j:
                    dot_prod += self.coupling_matrix[i, j] * x_norm[j]
            coupling_sum += (x_norm[i] - dot_prod)**2 * np.exp(-0.1 * x_norm[i]**2)
        
        # Dynamic conditioning based on input characteristics
        condition_factor = 1.0
        for i in range(self.dim):
            cond_weight = self.condition_weights[i]
            freq_factor = 1.0 + 0.3 * np.abs(np.sin(self.spectral_freqs[i]))
            mag_factor = 1.0 + 0.1 * np.abs(x_norm[i])
            condition_factor *= (cond_weight + 0.2 * freq_factor + 0.1 * mag_factor)
        
        # Combined landscape with global scaling
        result = 0.25 * logistic_sum + 0.25 * quat_sum + 0.25 * spectral_sum + 0.25 * coupling_sum
        
        # Penalty for large values and global scaling
        penalty = 0.15 * np.sum(np.abs(x_norm)**3)
        return result * condition_factor + penalty + 0.02 * np.sum(x_norm**4)
