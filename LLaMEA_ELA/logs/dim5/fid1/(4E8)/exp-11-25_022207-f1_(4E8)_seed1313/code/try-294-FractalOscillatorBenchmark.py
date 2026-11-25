import numpy as np

class FractalOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal component using self-similar patterns with chaotic modulation
        fractal = 0
        for i in range(self.dim):
            # Create fractal-like behavior with recursive-like terms and chaotic modulation
            base_freq = 2**(i % 4)
            chaotic_mod = np.sin(3.14159 * x_norm[i] * (1 + 0.1 * np.sin(5 * x_norm[i])))
            term = np.sin(base_freq * np.pi * x_norm[i]) * np.cos(base_freq * np.pi * x_norm[i] * chaotic_mod)
            fractal += term / (1.0 + i * 0.05)
        
        # Harmonic oscillator component with time-varying frequencies and phase shifts
        harmonic = 0
        for i in range(self.dim):
            freq = 2**(i % 5)  # Frequencies 1, 2, 4, 8, 16, 1, 2, ...
            phase_shift = np.sin(0.5 * np.pi * x_norm[i])
            damp = 1.0 / (1.0 + 0.2 * i)
            harmonic += damp * np.sin(freq * np.pi * x_norm[i] + phase_shift) * np.cos(freq * np.pi * x_norm[i] + phase_shift)
        
        # Multi-scale interaction terms with chaotic coupling
        interaction = 0
        scales = [1, 3, 5, 7]
        for scale in scales:
            if scale <= self.dim:
                # Grouped interactions with chaotic coupling
                group_sum = np.sum(x_norm[:scale]**2)
                chaotic_coupling = np.sin(2 * np.pi * group_sum) * np.cos(3 * np.pi * group_sum)
                interaction += chaotic_coupling * np.sin(np.pi * group_sum) * np.cos(2 * np.pi * group_sum)
        
        # Asymmetric conditioning terms with multi-exponential weights
        conditioning = 0
        for i in range(self.dim):
            if x_norm[i] >= 0:
                conditioning += (x_norm[i]**3) * np.exp(-0.5 * x_norm[i]**2) + 0.1 * x_norm[i]**4
            else:
                conditioning += (x_norm[i]**5) * np.exp(-0.3 * x_norm[i]**2) + 0.05 * x_norm[i]**6
        
        # Boundary attraction terms with multi-scale penalties
        boundary = 0
        for i in range(self.dim):
            boundary += 15 * (np.abs(x_norm[i]) - 1)**6 + 5 * np.abs(x_norm[i])**3
        
        # Chaotic saddle point terms to introduce extreme landscape complexity
        saddle = 0
        for i in range(self.dim):
            saddle += np.sin(7 * np.pi * x_norm[i]) * np.cos(4 * np.pi * x_norm[i]) * np.tan(0.5 * np.pi * x_norm[i])
        
        # Combined result with adaptive scaling and chaotic mixing
        result = 2.0 * fractal + 1.5 * harmonic + 1.0 * interaction + 0.7 * conditioning + 0.5 * boundary + 0.3 * saddle
        
        return result