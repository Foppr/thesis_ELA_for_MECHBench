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
        
        # Dynamic trigonometric couplings with frequency modulation based on dimension
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_mod_i = 1.0 + 0.25 * np.sin(i * np.pi / (self.dim + 2))
                freq_mod_j = 1.0 + 0.25 * np.cos(j * np.pi / (self.dim + 2))
                phase_shift = np.sin(i * np.pi / self.dim) * np.cos(j * np.pi / self.dim)
                trig_coupling += np.sin(freq_mod_i * 3.5 * np.pi * (x_norm[i] + x_norm[j]) + phase_shift) * \
                                np.cos(freq_mod_j * 5.5 * np.pi * (x_norm[i] - x_norm[j]) + phase_shift)
        
        # Enhanced fractal-like irregularities with multi-frequency sinusoidal components
        fractal_irregularity = 0.0
        for i in range(self.dim):
            fractal_irregularity += np.sin(14 * np.pi * x_norm[i]**3) * np.cos(16 * np.pi * x_norm[i]**3) * \
                                  np.sin(20 * np.pi * x_norm[i]**2) * np.cos(22 * np.pi * x_norm[i]**2) * \
                                  np.sin(24 * np.pi * x_norm[i]) * np.cos(26 * np.pi * x_norm[i])
        
        # Enhanced asymmetric saddle with higher-order polynomial and exponential components
        asymmetric_saddle = np.sum(np.exp(-x_norm**4) * (0.6 * x_norm**5 - 0.4 * x_norm**3 + 0.2 * x_norm**2 - 0.1 * x_norm))
        
        # Adaptive chaotic noise with dimension-dependent amplitude and frequency
        noise_amplitude = 0.035 * (1 + 0.18 * np.log(self.dim + 1))
        noise_frequency = 220 * (1 + 0.12 * np.log(self.dim + 1))
        noise = noise_amplitude * np.random.random() * np.sin(noise_frequency * np.pi * np.sum(x_norm**2))
        
        # Dynamic scaling factor with exponential growth and dimension-dependent adjustment
        scale_factor = 1.0 + 0.18 * np.exp(self.dim / 7.5) * (1 + 0.06 * np.log(self.dim + 1))
        
        return scale_factor * (1.8 * exp_basin + 1.6 * trig_coupling + 1.0 * fractal_irregularity + 0.8 * asymmetric_saddle + noise)