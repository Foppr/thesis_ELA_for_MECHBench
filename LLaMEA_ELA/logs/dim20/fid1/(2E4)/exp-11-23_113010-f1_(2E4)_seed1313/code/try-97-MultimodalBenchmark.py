import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial basin with golden ratio exponents and exponential scaling
        golden_ratio = (1 + np.sqrt(5)) / 2
        poly_basin = np.sum(0.8 * x_norm**(2 * golden_ratio) + 0.6 * x_norm**(3 * golden_ratio) + 0.4 * x_norm**(4 * golden_ratio))
        
        # Sinusoidal modulations with exponentially increasing frequencies and golden ratio coupling
        sin_mod = np.sum(np.sin(2**5 * np.pi * x_norm) * np.cos(2**6 * np.pi * x_norm) * np.sin(2**7 * np.pi * x_norm))
        sin_mod2 = np.sum(np.sin(3**4 * np.pi * x_norm**2) * np.cos(3**5 * np.pi * x_norm**2) * np.sin(3**6 * np.pi * x_norm**2))
        
        # Dynamic cross-dimensional coupling with golden ratio coefficients and exponential interaction
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_coef = (golden_ratio ** (i + j)) / (1 + np.abs(i - j))
                cross_interaction += coupling_coef * (x_norm[i]**5 + x_norm[j]**5) * np.sin(2**4 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Perturbed saddle structure with exponential higher-order terms and golden ratio scaling
        saddle = np.sum(x_norm**(3 * golden_ratio) * np.cos(3 * golden_ratio * np.pi * x_norm) + 
                       0.7 * x_norm**(2 * golden_ratio) * np.sin(2 * golden_ratio * np.pi * x_norm) + 
                       0.5 * x_norm**golden_ratio * np.cos(golden_ratio * np.pi * x_norm))
        
        # Additional harmonic components with exponential complexity and golden ratio phase shifts
        harmonic = np.sum(np.sin(5**3 * np.pi * x_norm**3) * np.cos(5**4 * np.pi * x_norm**3) * np.sin(5**5 * np.pi * x_norm**3))
        
        # Adaptive noise with golden ratio amplitude modulation and dynamic frequency
        noise_amp = 0.05 * (1 + golden_ratio) / (1 + np.log(self.dim + 1))
        noise_freq = 2**8 * (1 + np.sin(np.sum(x_norm**2)))
        noise = noise_amp * np.random.random() * np.sin(noise_freq * np.pi * np.sum(x_norm**2))
        
        # Dynamic scaling factor based on golden ratio and dimensionality
        scale_factor = 1.0 + 0.1 * (golden_ratio - 1) * np.log(self.dim + 1)
        
        return scale_factor * (2.0 * poly_basin + 1.5 * sin_mod + 1.0 * sin_mod2 + 0.8 * cross_interaction + 0.6 * saddle + 0.5 * harmonic + noise)