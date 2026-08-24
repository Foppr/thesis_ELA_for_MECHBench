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
            seq[i] = x + 0.15 * np.sin(i * np.pi / self.dim)
        return seq
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Enhanced chaotic polynomial with dynamic exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponents = [2, 3, 4, 5]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            result += chaotic_factor * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2))
            
        # Multi-frequency trigonometric coupling with chaotic amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                amp = 0.4 * (1 + np.sin(4 * phase))
                freq1 = 4 * (1 + np.cos(3 * phase))
                freq2 = 3 * (1 + np.sin(3 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Spherical penalty with chaotic center and variable radius
        center = np.array([self.chaotic_sequence[i] * 2.5 for i in range(self.dim)])
        radius = 1.2 + 0.3 * np.sin(self.chaotic_sequence[0] * 8)
        result += 0.5 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency chaotic oscillation with varying amplitudes
        for i in range(self.dim):
            freq = 12 + 8 * self.chaotic_sequence[i]
            amp = 0.2 + 0.08 * np.cos(4 * self.chaotic_sequence[i])
            result += amp * np.sin(freq * x[i])
            
        # Global minimum attractor with chaotic scaling
        scale = 0.04 + 0.04 * np.sin(self.chaotic_sequence[0] * 18)
        result += scale * np.sum(x**2)
        
        # Chaotic noise term
        noise = 0.015 * np.sum(np.sin(self.chaotic_sequence * x))
        result += noise
        
        # New chaotic modulation with modified coefficient
        modulate = 0.04 * np.sum(np.cos(self.chaotic_sequence * x**2))
        result += modulate
        
        # New chaotic interaction term with different frequency
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 6 * (1 + np.sin(self.chaotic_sequence[i] * 4))
                result += 0.05 * freq * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j])
        
        return result