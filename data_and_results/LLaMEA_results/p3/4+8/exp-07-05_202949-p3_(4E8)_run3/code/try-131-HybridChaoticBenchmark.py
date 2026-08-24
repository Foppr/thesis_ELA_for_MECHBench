import numpy as np

class HybridChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequences for dynamic modulation
        self.chaotic_seq = np.sin(np.arange(dim) * np.pi / 3.0) * 0.5 + 0.5
        self.freq_seq = np.cos(np.arange(dim) * np.pi / 2.5) * 0.3 + 0.7
        self.phase_seq = np.tan(np.arange(dim) * np.pi / 5.0) * 0.2 + 0.8
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin terms with chaotic coefficients
        result = 0.0
        for i in range(self.dim):
            coeff = 1.0 + 0.5 * self.chaotic_seq[i]
            result += coeff * (x[i] - 1.0)**2 + 0.5 * (x[i] + 1.5)**2
        
        # Sinusoidal modulation with adaptive frequency and amplitude
        for i in range(self.dim):
            freq = 2.0 + 3.0 * self.freq_seq[i]
            amp = 0.8 + 0.4 * self.chaotic_seq[i]
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + self.phase_seq[i])
        
        # Radial symmetry term with chaotic scaling
        radial = np.sum(x**2)
        scale = 0.5 + 0.5 * self.chaotic_seq[0] if self.dim > 0 else 1.0
        result += scale * np.sin(5.0 * np.sqrt(radial)) * np.exp(-0.1 * radial)
        
        # Cross-term interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.3 + 0.7 * self.chaotic_seq[i] * self.chaotic_seq[j]
                result += coupling * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        
        # Adaptive noise component
        noise = 0.0
        for i in range(self.dim):
            amp = 0.1 + 0.05 * self.freq_seq[i]
            noise += amp * np.sin(10.0 * x[i] + self.phase_seq[i]) * np.cos(8.0 * x[i])
        result += noise
        
        # Higher-order polynomial terms
        result += 0.001 * np.sum(x**4) + 0.0005 * np.sum(x**6) + 0.0001 * np.sum(x**8)
        
        # Global minimum shift with chaotic transformation
        shift = np.array([0.5 * np.sin(self.chaotic_seq[i] * np.pi) for i in range(self.dim)])
        result += 0.3 * np.sum((x - shift)**2)
        
        return result