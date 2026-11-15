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
            seq[i] = x + 0.1 * np.sin(i * np.pi / self.dim) + 0.05 * np.cos(i * np.pi / (self.dim + 1))
        return seq
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Quaternion-inspired chaotic polynomial component
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponents = [2, 3, 4, 5, 6, 7, 8]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            term = chaotic_factor * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2))
            result += term
            
        # Dynamic coupling with fractal frequency scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                amp = 0.4 * (1 + np.sin(3 * phase)) * (1 + 0.1 * np.cos(5 * phase))
                freq1 = 3 * (1 + np.cos(2 * phase)) * (1 + 0.2 * np.sin(4 * phase))
                freq2 = 2 * (1 + np.sin(2 * phase)) * (1 + 0.15 * np.cos(3 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Adaptive spherical penalty with fractal center positioning
        center = np.array([self.chaotic_sequence[i] * 3.0 * (1 + 0.1 * np.sin(i * np.pi / self.dim)) for i in range(self.dim)])
        radius = 1.5 + 0.5 * np.sin(self.chaotic_sequence[0] * 10) * (1 + 0.05 * np.cos(self.dim))
        result += 0.4 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency chaotic oscillation with dynamic amplitude modulation
        for i in range(self.dim):
            freq = 15 + 10 * self.chaotic_sequence[i] * (1 + 0.1 * np.sin(i * np.pi / self.dim))
            amp = 0.15 + 0.05 * np.cos(5 * self.chaotic_sequence[i]) * (1 + 0.02 * np.sin(i * np.pi / (self.dim + 1)))
            result += amp * np.sin(freq * x[i])
            
        # Global minimum attractor with quaternion-like scaling
        scale = 0.05 + 0.05 * np.sin(self.chaotic_sequence[0] * 20) * (1 + 0.03 * np.cos(self.dim))
        result += scale * np.sum(x**2)
        
        # Add chaotic noise with fractal dimensionality
        noise = 0.01 * np.sum(np.sin(self.chaotic_sequence * x) * (1 + 0.05 * np.cos(self.dim * x)))
        result += noise
        
        # Add quaternion-based interaction term
        quat_term = 0.03 * np.sum(np.sin(self.chaotic_sequence * x**2) * np.cos(self.chaotic_sequence * x))
        result += quat_term
        
        # Add fractal scaling component
        fractal_scale = 0.02 * np.sum(np.sin(self.chaotic_sequence * np.log(np.abs(x) + 1)))
        result += fractal_scale
        
        return result