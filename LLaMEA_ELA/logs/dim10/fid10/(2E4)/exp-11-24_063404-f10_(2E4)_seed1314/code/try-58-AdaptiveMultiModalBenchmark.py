import numpy as np

class AdaptiveMultiModalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial potential with varying exponents and adaptive weights
        poly_potential = 0.0
        for i in range(self.dim):
            exp_factor = 2 + (i % 5)
            weight = 1.0 / (1.0 + 0.1 * i)
            poly_potential += weight * (x_scaled[i] ** exp_factor)
        
        # Gaussian radial basis functions with adaptive centers and widths
        rbf_sum = 0.0
        num_centers = min(8, self.dim)
        for i in range(num_centers):
            center = np.sin(i * np.pi / num_centers) * 0.8
            width = 0.5 + 0.3 * np.cos(i * np.pi / num_centers)
            rbf_sum += np.exp(-0.5 * ((x_scaled[i % self.dim] - center) / width) ** 2)
        
        # Sinusoidal coupling between dimensions with varying frequencies
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 5 + 3 * np.sin(i * 0.5)
                coupling += np.sin(freq * (x_scaled[i] + x_scaled[j])) * np.cos(freq * (x_scaled[i] - x_scaled[j]))
        
        # Asymmetric hill-climbing corridors with exponential decay
        corridor = 0.0
        for i in range(self.dim):
            if x_scaled[i] > 0:
                corridor += np.exp(-5 * x_scaled[i]) * np.sin(10 * x_scaled[i])
            else:
                corridor += np.exp(-3 * abs(x_scaled[i])) * np.cos(8 * x_scaled[i])
        
        # Adaptive conditioning through dimension-wise scaling
        cond_factor = 0.0
        for i in range(self.dim):
            cond_factor += (1.0 + 0.5 * np.sin(i * 0.3)) * x_scaled[i]**2
        
        # High-frequency oscillation with chaotic modulation
        chaos_osc = 0.0
        for i in range(self.dim):
            freq_mod = 20 + 10 * np.sin(x_scaled[i] * 3)
            chaos_osc += np.sin(freq_mod * x_scaled[i]) * np.cos(freq_mod * x_scaled[i])
        
        # Combine all components with dynamic weights
        return (0.7 * poly_potential + 
                0.5 * rbf_sum + 
                0.3 * coupling + 
                0.2 * corridor + 
                0.1 * cond_factor + 
                0.05 * chaos_osc)