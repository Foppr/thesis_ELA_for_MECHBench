import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay basin with multi-scale polynomial terms
        exp_basin = np.sum(np.exp(-x_norm**2) * (0.9 * x_norm**6 + 0.7 * x_norm**5 + 0.5 * x_norm**4 + 0.3 * x_norm**3))
        
        # Enhanced dynamic trigonometric couplings with modified frequency modulation
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_mod_i = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 2))
                freq_mod_j = 1.0 + 0.3 * np.cos(j * np.pi / (self.dim + 2))
                phase_shift = np.sin(i * np.pi / (self.dim + 1)) * np.cos(j * np.pi / (self.dim + 1))
                trig_coupling += np.sin(freq_mod_i * 4 * np.pi * (x_norm[i] + x_norm[j]) + phase_shift) * \
                                np.cos(freq_mod_j * 6 * np.pi * (x_norm[i] - x_norm[j]) + phase_shift)
        
        # Enhanced fractal-like irregularities with multi-frequency sinusoidal components
        fractal_irregularity = 0.0
        for i in range(self.dim):
            fractal_irregularity += np.sin(13 * np.pi * x_norm[i]**3) * np.cos(15 * np.pi * x_norm[i]**3) * \
                                  np.sin(19 * np.pi * x_norm[i]**2) * np.cos(21 * np.pi * x_norm[i]**2) * \
                                  np.sin(23 * np.pi * x_norm[i]) * np.cos(25 * np.pi * x_norm[i])
        
        # Enhanced asymmetric saddle with higher-order polynomial and exponential components
        asymmetric_saddle = np.sum(np.exp(-x_norm**4) * (0.6 * x_norm**5 - 0.4 * x_norm**3 + 0.2 * x_norm**2 - 0.1 * x_norm))
        
        # New multi-scale Gaussian component for additional landscape complexity
        gaussian_component = 0.0
        for i in range(self.dim):
            gaussian_component += np.exp(-5.0 * (x_norm[i] - 0.3)**2) * np.sin(7 * np.pi * x_norm[i]) * \
                                np.exp(-2.0 * (x_norm[i] + 0.5)**2) * np.cos(9 * np.pi * x_norm[i])
        
        # Adaptive chaotic noise with dimension-dependent amplitude and frequency
        noise_amplitude = 0.03 * (1 + 0.15 * np.log(self.dim + 1))
        noise_frequency = 200 * (1 + 0.1 * np.log(self.dim + 1))
        noise = noise_amplitude * np.random.random() * np.sin(noise_frequency * np.pi * np.sum(x_norm**2))
        
        # Dynamic scaling factor with exponential growth and dimension-dependent adjustment
        scale_factor = 1.0 + 0.15 * np.exp(self.dim / 8.0) * (1 + 0.05 * np.log(self.dim + 1))
        
        return scale_factor * (1.7 * exp_basin + 1.5 * trig_coupling + 0.9 * fractal_irregularity + 0.7 * asymmetric_saddle + 0.3 * gaussian_component + noise)