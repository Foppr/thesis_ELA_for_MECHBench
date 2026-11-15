import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        # Initialize chaotic parameters
        self.t = 0
        self.freq_base = 2.0
        self.amp_base = 1.5
        self.phase_shift = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        self.t += 0.01  # Time progression
        
        # Base quadratic term
        f = 0.5 * np.sum(x**2)
        
        # Time-varying harmonic potentials
        harmonic_sum = 0
        for i in range(self.dim):
            # Adaptive frequency and amplitude based on time
            freq = self.freq_base * (1.0 + 0.3 * np.sin(self.t + i * 0.5))
            amp = self.amp_base * (1.0 + 0.2 * np.cos(self.t * 0.7 + i * 0.3))
            # Harmonic potential with phase shift
            harmonic_sum += amp * np.sin(freq * x[i] + self.phase_shift[i])
            
        f += 1.2 * harmonic_sum
        
        # Chaotic gradient modulation
        chaotic_mod = 0
        for i in range(self.dim):
            # Logistic map for chaotic behavior
            r = 3.8 + 0.1 * np.sin(self.t * 0.5)
            x_log = x[i] * r * (1 - x[i])
            chaotic_mod += np.sin(x_log * 5.0) * np.cos(x[i] * 3.0)
            
        f += 0.8 * chaotic_mod
        
        # Adaptive landscape complexity
        complexity = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying coupling strength
                coupling_strength = 0.5 + 0.3 * np.sin(self.t * 0.3 + i + j)
                complexity += coupling_strength * np.sin(x[i] * x[j] * 0.8)
                
        f += 1.0 * complexity
        
        # Multi-scale oscillatory landscape
        multi_scale = 0
        for scale in range(1, 5):
            for i in range(self.dim):
                freq = scale * 1.5 + 0.5 * np.sin(self.t * 0.2 + i)
                multi_scale += np.sin(x[i] * freq) * np.cos(x[i] * freq * 0.5)
                
        f += 0.6 * multi_scale
        
        # Dynamic noise component
        noise = 0
        for i in range(self.dim):
            # Time-varying noise with chaotic pattern
            noise += np.sin(x[i] * 4.0 + np.sin(self.t * 2.0 + x[i]) * 0.5)
            
        f += 0.3 * noise
        
        # Non-stationary global minimum movement
        global_min_shift = np.array([np.sin(self.t * 0.3), np.cos(self.t * 0.4)])
        if self.dim >= 2:
            diff = x[:2] - global_min_shift
            f += 0.5 * np.sum(diff**2)
            
        return f