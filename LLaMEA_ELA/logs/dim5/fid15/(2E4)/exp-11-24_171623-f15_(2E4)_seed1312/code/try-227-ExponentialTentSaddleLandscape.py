import numpy as np

class ExponentialTentSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute tent map parameters for chaotic behavior with higher diversity
        self.tent_mu = 1.5 + 0.8 * np.random.rand(dim)
        # Precompute exponential radial basis centers and scales with wider range
        self.centers = np.random.uniform(-2, 2, dim)
        self.scales = 0.1 + 2.0 * np.random.rand(dim)
        # Precompute saddle-point coupling weights with stronger interactions
        self.saddle_weights = np.random.uniform(-1.2, 1.2, (dim, dim))
        # Precompute chaotic sequence for dynamic conditioning with higher complexity
        self.chaotic_seq = np.array([self._tent_map(0.5, self.tent_mu[i]) for i in range(dim)])
        # Additional harmonic interference components with more complex patterns
        self.harmonic_amps = 2.0 + 1.5 * np.random.rand(dim)
        self.harmonic_freqs = 1.0 + 5.0 * np.random.rand(dim)
        # Add polynomial barrier coefficients for stronger basin formation
        self.barrier_coeffs = np.random.uniform(-0.5, 0.5, (dim, 4))
        
    def _tent_map(self, x, mu):
        if x < 0.5:
            return mu * x
        else:
            return mu * (1 - x)
        
    def f(self, x):
        # Normalize input to [-2, 2] range for enhanced exploration
        x_norm = x / 2.5
        
        # Exponential radial basis component with dynamic scales and cross-terms
        exp_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.centers[i])**2)
            exp_sum += np.exp(-self.scales[i] * dist) * np.sin(3 * np.pi * dist) * np.cos(2 * np.pi * x_norm[i])
        
        # Chaotic tent map component with enhanced scaling and interaction
        chaotic_sum = 0.0
        for i in range(self.dim):
            x_chaos = self.chaotic_seq[i]
            chaotic_sum += (x_chaos**3 - 0.5 * x_chaos) * np.sin(6 * x_norm[i]) * np.exp(-0.4 * x_norm[i]**2)
        
        # Saddle-point coupling component with gradient-based interactions and higher-order terms
        saddle_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    grad_coupling = self.saddle_weights[i, j] * (x_norm[i] - x_norm[j])
                    saddle_sum += grad_coupling * np.exp(-0.3 * grad_coupling**2) * np.sin(2 * grad_coupling)
        
        # Multi-modal harmonic component with varying amplitudes and frequencies
        harm_sum = 0.0
        for i in range(self.dim):
            amp = self.harmonic_amps[i]
            freq = self.harmonic_freqs[i]
            harm_sum += amp * np.cos(freq * x_norm[i]) * np.exp(-0.15 * x_norm[i]**2) * np.sin(3 * x_norm[i])
        
        # Basin-forming pathway component with polynomial barriers and enhanced nonlinearity
        basin_sum = 0.0
        for i in range(self.dim):
            barrier = 1.0 + 0.5 * np.cos(x_norm[i] * 4) + 0.2 * np.sin(x_norm[i] * 6)
            poly_term = self.barrier_coeffs[i, 0] * x_norm[i]**8 + self.barrier_coeffs[i, 1] * x_norm[i]**6 + \
                       self.barrier_coeffs[i, 2] * x_norm[i]**4 + self.barrier_coeffs[i, 3] * x_norm[i]**2
            basin_sum += barrier * poly_term * np.exp(-0.05 * x_norm[i]**2)
        
        # Interference pattern component with cross-modal coupling and additional harmonic interactions
        interference_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x_norm[i] * x_norm[j]) * np.exp(-0.2 * (x_norm[i] - x_norm[j])**2)
                interference_sum += coupling * (self.harmonic_amps[i] + self.harmonic_amps[j]) * np.cos(0.5 * (x_norm[i] + x_norm[j]))
        
        # Combined landscape with adaptive scaling and additional interaction terms
        result = 0.15 * exp_sum + 0.2 * chaotic_sum + 0.3 * saddle_sum + 0.18 * harm_sum + 0.12 * basin_sum + 0.05 * interference_sum
        
        # Dynamic conditioning factor based on tent map sequence and input magnitude with higher complexity
        condition_factor = 1.0
        for i in range(self.dim):
            chaos_factor = self.chaotic_seq[i] * (1.0 + 0.5 * np.cos(x_norm[i]))
            condition_factor *= (1.0 + 0.6 * np.abs(x_norm[i]) + 0.1 * x_norm[i]**4 + 0.2 * chaos_factor + 0.05 * np.sin(3 * x_norm[i]))
        
        # Final transformation with global scaling and noise modulation
        noise = 0.05 * np.sum(np.sin(x_norm * 9))
        return result * condition_factor + noise + 0.05 * np.sum(x_norm**10) + 0.03 * np.sum(np.abs(x_norm)**4)