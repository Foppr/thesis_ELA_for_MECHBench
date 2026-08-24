import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        # Time-varying parameters for dynamic landscape
        self.t = 0.0
        self.freq_base = 0.5
        self.amp_base = 1.0
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        self.t = (self.t + 0.01) % (2 * np.pi)  # Dynamic time parameter
        
        # Base quadratic term
        f = 0.5 * np.sum(x**2)
        
        # Time-varying harmonic potentials
        harmonic_sum = 0
        for i in range(self.dim):
            # Varying frequencies and amplitudes based on time
            freq = self.freq_base * (1.0 + 0.3 * np.sin(self.t + i * 0.5))
            amp = self.amp_base * (1.0 + 0.2 * np.cos(self.t + i * 0.3))
            harmonic_sum += amp * np.sin(freq * x[i])**2
        
        f += 1.5 * harmonic_sum
        
        # Chaotic gradient interactions
        chaotic_sum = 0
        for i in range(self.dim):
            # Use chaotic map for interaction
            chaotic_val = np.sin(x[i] * 3.0 + np.sin(x[i] * 7.0) * np.cos(self.t))
            chaotic_sum += chaotic_val * np.cos(x[i] * 2.0 + np.sin(x[i] * 5.0))
        f += 1.2 * chaotic_sum
        
        # Saddle-point structure with dynamic coupling
        saddle_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling strength based on time
                coupling = 0.8 * (1.0 + 0.4 * np.sin(self.t + i + j))
                saddle_sum += coupling * x[i] * x[j] * np.sin(x[i] + x[j])
        f += 0.9 * saddle_sum
        
        # Multi-scale oscillatory landscape
        multi_scale_sum = 0
        for scale in range(1, 5):
            for i in range(self.dim):
                freq = 2.0 * scale
                multi_scale_sum += np.sin(x[i] * freq + self.t * scale) * np.cos(x[i] * freq * 0.5)
        f += 0.7 * multi_scale_sum
        
        # Time-varying separability
        sep_factor = 0.5 + 0.5 * np.sin(self.t)
        separable_sum = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                separable_sum += (x[i] - x[i+1])**2
        f += sep_factor * separable_sum
        
        # Add noise with chaotic pattern
        noise = 0
        for i in range(self.dim):
            noise += np.sin(x[i] * 8.0 + np.sin(x[i] * 12.0) * np.cos(self.t))
        f += 0.3 * noise
        
        # Add periodic modulation
        period_mod = 0.4 * np.sin(self.t * 2.0)
        f += period_mod * np.sum(np.sin(x)**2)
        
        return f