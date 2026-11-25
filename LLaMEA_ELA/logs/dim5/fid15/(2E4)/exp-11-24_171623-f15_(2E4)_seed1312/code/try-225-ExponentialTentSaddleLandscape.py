import numpy as np

class ExponentialTentSaddleLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute tent map parameters for chaotic behavior
        self.tent_mu = 1.8 + 0.4 * np.random.rand(dim)
        # Precompute exponential radial basis centers and scales
        self.centers = np.random.uniform(-1, 1, dim)
        self.scales = 0.3 + 1.2 * np.random.rand(dim)
        # Precompute saddle-point coupling weights with modified interaction strength
        self.saddle_weights = np.random.uniform(-0.7, 0.7, (dim, dim))
        # Precompute chaotic sequence for dynamic conditioning
        self.chaotic_seq = np.array([self._tent_map(0.5, self.tent_mu[i]) for i in range(dim)])
        # Additional harmonic interference components
        self.harmonic_amps = 1.5 + 0.8 * np.random.rand(dim)
        self.harmonic_freqs = 2.0 + 3.0 * np.random.rand(dim)
        
    def _tent_map(self, x, mu):
        if x < 0.5:
            return mu * x
        else:
            return mu * (1 - x)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential radial basis component with dynamic scales
        exp_sum = 0.0
        for i in range(self.dim):
            dist = np.sum((x_norm - self.centers[i])**2)
            exp_sum += np.exp(-self.scales[i] * dist) * np.sin(2 * np.pi * dist)
        
        # Chaotic tent map component with dynamic scaling
        chaotic_sum = 0.0
        for i in range(self.dim):
            x_chaos = self.chaotic_seq[i]
            chaotic_sum += (x_chaos**2 - 0.25) * np.sin(4 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Saddle-point coupling component with gradient-based interactions
        saddle_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    grad_coupling = self.saddle_weights[i, j] * (x_norm[i] - x_norm[j])
                    saddle_sum += grad_coupling * np.exp(-0.5 * grad_coupling**2)
        
        # Multi-modal harmonic component with varying amplitudes and frequencies
        harm_sum = 0.0
        for i in range(self.dim):
            amp = self.harmonic_amps[i]
            freq = self.harmonic_freqs[i]
            harm_sum += amp * np.cos(freq * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # Basin-forming pathway component with polynomial barriers
        basin_sum = 0.0
        for i in range(self.dim):
            barrier = 1.0 + 0.3 * np.cos(x_norm[i] * 3)
            basin_sum += barrier * (x_norm[i]**6 - x_norm[i]**4) * np.exp(-0.1 * x_norm[i]**2)
        
        # Interference pattern component with cross-modal coupling
        interference_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x_norm[i] * x_norm[j]) * np.exp(-0.1 * (x_norm[i] - x_norm[j])**2)
                interference_sum += coupling * (self.harmonic_amps[i] + self.harmonic_amps[j])
        
        # Combined landscape with adaptive scaling
        result = 0.2 * exp_sum + 0.2 * chaotic_sum + 0.25 * saddle_sum + 0.15 * harm_sum + 0.15 * basin_sum + 0.05 * interference_sum
        
        # Dynamic conditioning factor based on tent map sequence and input magnitude
        condition_factor = 1.0
        for i in range(self.dim):
            chaos_factor = self.chaotic_seq[i] * (1.0 + 0.3 * np.cos(x_norm[i]))
            condition_factor *= (1.0 + 0.4 * np.abs(x_norm[i]) + 0.05 * x_norm[i]**4 + 0.15 * chaos_factor)
        
        # Final transformation with global scaling and noise modulation
        noise = 0.03 * np.sum(np.sin(x_norm * 7))
        return result * condition_factor + noise + 0.03 * np.sum(x_norm**8) + 0.02 * np.sum(np.abs(x_norm)**3)