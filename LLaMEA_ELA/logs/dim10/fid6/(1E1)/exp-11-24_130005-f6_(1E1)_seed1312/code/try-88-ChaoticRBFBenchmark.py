import numpy as np

class ChaoticRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute logistic map parameters for chaotic behavior
        self.r_values = np.linspace(3.5, 4.0, dim)
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic component using logistic maps
        chaotic_term = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            # Initialize with small random value to ensure chaos
            xi = 0.5 + 0.1 * np.sin(x_scaled[i])
            # Iterate logistic map for several steps to reach chaotic regime
            for _ in range(10):
                xi = r * xi * (1 - xi)
            chaotic_term += xi
        
        # Radial basis function component with varying widths and centers
        rbf_term = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            width = 0.5 + 0.3 * np.sin(i)
            rbf_term += np.exp(-width * (x_scaled[i] - center)**2)
        
        # Quaternion-inspired cross-terms creating multidirectional interactions
        quat_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-terms
                # Create quaternion-like interaction
                q_real = np.cos(x_scaled[i] + x_scaled[j])
                q_imag_i = np.sin(x_scaled[i]) * np.cos(x_scaled[j])
                q_imag_j = np.cos(x_scaled[i]) * np.sin(x_scaled[j])
                quat_term += q_real * q_imag_i * q_imag_j
        
        # Multi-scale sinusoidal modulation with frequency mixing
        multi_freq_term = 0.0
        frequencies = [1.0, 2.0, 3.0, 5.0]
        for i in range(self.dim):
            freq_idx = i % len(frequencies)
            multi_freq_term += np.sin(frequencies[freq_idx] * x_scaled[i]) * \
                              np.cos(0.5 * frequencies[freq_idx] * x_scaled[i]**2) * \
                              np.sin(0.3 * x_scaled[i] * np.cos(x_scaled[i]))
        
        # Combined landscape with dynamic weights
        return 1.2 * chaotic_term + 0.9 * rbf_term + 0.7 * quat_term + 0.8 * multi_freq_term + 3.1