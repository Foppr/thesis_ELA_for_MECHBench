import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay basin with asymmetric polynomial terms
        exp_basin = np.sum(np.exp(-x_norm**2) * (0.8 * x_norm**6 + 0.6 * x_norm**5 + 0.4 * x_norm**4))
        
        # Trigonometric couplings with chaotic phase shifts and varying frequencies
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = np.sin(i * np.pi / self.dim) * np.cos(j * np.pi / self.dim)
                trig_coupling += np.sin(3 * np.pi * (x_norm[i] + x_norm[j]) + phase_shift) * \
                                np.cos(5 * np.pi * (x_norm[i] - x_norm[j]) + phase_shift)
        
        # Fractal-like irregularities with recursive sinusoidal components
        fractal_irregularity = 0.0
        for i in range(self.dim):
            fractal_irregularity += np.sin(11 * np.pi * x_norm[i]**3) * np.cos(13 * np.pi * x_norm[i]**3) * \
                                  np.sin(17 * np.pi * x_norm[i]**2) * np.cos(19 * np.pi * x_norm[i]**2)
        
        # Asymmetric saddle with exponential and polynomial components
        asymmetric_saddle = np.sum(np.exp(-x_norm**4) * (0.5 * x_norm**5 - 0.3 * x_norm**3 + 0.1 * x_norm))
        
        # Chaotic noise with dynamic amplitude modulation based on dimensionality
        noise_amplitude = 0.02 * (1 + 0.1 * np.log(self.dim))
        noise = noise_amplitude * np.random.random() * np.sin(150 * np.pi * np.sum(x_norm**2))
        
        # Dynamic scaling factor with exponential growth
        scale_factor = 1.0 + 0.1 * np.exp(self.dim / 10.0)
        
        return scale_factor * (1.5 * exp_basin + 1.3 * trig_coupling + 0.8 * fractal_irregularity + 0.6 * asymmetric_saddle + noise)