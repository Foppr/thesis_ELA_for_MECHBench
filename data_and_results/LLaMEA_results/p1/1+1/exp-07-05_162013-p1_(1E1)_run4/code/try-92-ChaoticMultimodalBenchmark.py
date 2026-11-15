import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.r = 3.9
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x + 0.15 * np.sin(i * np.pi / self.dim) + 0.05 * np.cos(i * np.pi / (self.dim * 2))
        return seq
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced chaotic polynomial with dynamic exponents and multi-modal peaks
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponents = [2, 3, 4, 5, 6, 7, 8]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            result += chaotic_factor * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2) + 0.1 * np.sin(10 * x[i]))
            
        # Multi-frequency trigonometric coupling with chaotic modulation and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j] + 0.2 * np.cos(x[i] + x[j])
                amp = 0.4 * (1 + np.sin(4 * phase)) * (1 + 0.1 * np.cos(2 * x[i]))
                freq1 = 4 * (1 + np.cos(3 * phase))
                freq2 = 3 * (1 + np.sin(3 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Multi-scale spherical penalty with chaotic radius and offset
        center = np.array([self.chaotic_sequence[i] * 4.0 for i in range(self.dim)])
        radius = 2.0 + 0.8 * np.sin(self.chaotic_sequence[0] * 12)
        result += 0.5 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency chaotic oscillation with amplitude and frequency modulation
        for i in range(self.dim):
            freq = 20 + 15 * self.chaotic_sequence[i]
            amp = 0.2 + 0.1 * np.cos(7 * self.chaotic_sequence[i])
            result += amp * np.sin(freq * x[i]) + 0.05 * np.cos(2 * freq * x[i])
            
        # Global minimum attractor with chaotic scaling and multi-modal distortion
        scale = 0.08 + 0.04 * np.sin(self.chaotic_sequence[0] * 25)
        result += scale * np.sum(x**2) + 0.03 * np.sum(np.sin(5 * x))
        
        # Chaotic noise with higher frequency components
        noise = 0.02 * np.sum(np.sin(self.chaotic_sequence * x**2) + 0.1 * np.cos(3 * self.chaotic_sequence * x))
        result += noise
        
        # New chaotic interaction term with variable coupling strength and frequency
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 9 * (1 + np.sin(self.chaotic_sequence[i] * 7))
                coupling = 0.06 * (1 + np.cos(self.chaotic_sequence[j] * 3))
                result += coupling * freq * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j] + 0.1 * x[i]**2)
        
        # Add a new high-frequency chaotic modulation to increase landscape complexity
        high_freq_mod = 0.05 * np.sum(np.sin(20 * self.chaotic_sequence * x) + 0.1 * np.cos(15 * self.chaotic_sequence * x**2))
        result += high_freq_mod
        
        return result