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
        
        # Enhanced chaotic polynomial with dynamic exponents and mixed powers
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponents = [2, 3, 4, 5, 6, 7, 8]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            result += chaotic_factor * (x[i]**exp + 0.5 * x[i]**(exp-1) + 0.1 * x[i]**(exp-2))
            
        # Multi-frequency trigonometric coupling with dynamic amplitudes and phases
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j] + 0.2 * np.sin(x[i])
                amp = 0.4 * (1 + np.sin(4 * phase)) * (1 + 0.2 * np.cos(x[j]))
                freq1 = 4 * (1 + np.cos(3 * phase))
                freq2 = 3 * (1 + np.sin(3 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Complex adaptive spherical penalty with time-varying center and radius
        center = np.array([self.chaotic_sequence[i] * 4.0 + 0.5 * np.sin(i) for i in range(self.dim)])
        radius = 2.0 + 0.8 * np.sin(self.chaotic_sequence[0] * 15)
        result += 0.5 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency chaotic oscillation with varying amplitudes and phase shifts
        for i in range(self.dim):
            freq = 20 + 15 * self.chaotic_sequence[i] + 5 * np.sin(x[i])
            amp = 0.2 + 0.1 * np.cos(7 * self.chaotic_sequence[i])
            phase_shift = 0.1 * np.sin(self.chaotic_sequence[i] * 10)
            result += amp * np.sin(freq * x[i] + phase_shift)
            
        # Global minimum attractor with chaotic scaling and additional noise
        scale = 0.07 + 0.03 * np.sin(self.chaotic_sequence[0] * 25)
        result += scale * np.sum(x**2)
        
        # Chaotic noise term with higher frequency modulation
        noise = 0.02 * np.sum(np.sin(self.chaotic_sequence * x**2) * np.cos(x))
        result += noise
        
        # New chaotic modulation with increased complexity and interaction
        modulate = 0.05 * np.sum(np.cos(self.chaotic_sequence * x**3) * np.sin(x))
        result += modulate
        
        # Additional chaotic interaction term with higher coupling strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 10 * (1 + np.sin(self.chaotic_sequence[i] * 7))
                coupling = 0.06 * freq * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j] + 0.3 * np.sin(x[i]))
                result += coupling
                
        # Add a new high-frequency chaotic component
        for i in range(self.dim):
            freq = 25 + 20 * self.chaotic_sequence[i]
            amp = 0.1 * (1 + np.sin(8 * self.chaotic_sequence[i]))
            result += amp * np.sin(freq * x[i] + 0.1 * np.cos(x[i]))
            
        return result