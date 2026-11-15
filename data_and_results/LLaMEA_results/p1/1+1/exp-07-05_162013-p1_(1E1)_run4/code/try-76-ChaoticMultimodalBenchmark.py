import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.r = 3.9  # Increased chaos parameter
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
        
        # Nested chaotic polynomial with fractal-like exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponents = [2, 3, 4, 5, 6, 7, 8]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            result += chaotic_factor * (x[i]**exp + 0.1 * np.sin(10 * x[i]))
            
        # Multi-scale trigonometric coupling with fractal frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                amp = 0.5 * (1 + np.sin(5 * phase)) * (1 + np.cos(3 * phase))
                freq1 = 5 * (1 + np.cos(2 * phase)) * (1 + np.sin(3 * phase))
                freq2 = 4 * (1 + np.sin(2 * phase)) * (1 + np.cos(3 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Fractal adaptive spherical penalty with multi-level centers
        centers = []
        for k in range(3):
            center = np.array([self.chaotic_sequence[i] * (2.0 + k * 0.5) for i in range(self.dim)])
            centers.append(center)
        radius = 2.0 + 0.8 * np.sin(self.chaotic_sequence[0] * 15)
        distances = [np.sum(((x - c) / radius)**2) for c in centers]
        result += 0.6 * np.mean(distances)
        
        # Multi-frequency chaotic oscillation with fractal amplitudes
        for i in range(self.dim):
            freq = 20 + 15 * self.chaotic_sequence[i] + 5 * np.sin(7 * self.chaotic_sequence[i])
            amp = 0.2 + 0.1 * np.cos(8 * self.chaotic_sequence[i]) + 0.05 * np.sin(12 * self.chaotic_sequence[i])
            result += amp * np.sin(freq * x[i]) + 0.05 * np.cos(15 * x[i])
            
        # Fractal global minimum attractor with multi-scale scaling
        scale = 0.1 + 0.05 * np.sin(self.chaotic_sequence[0] * 25)
        result += scale * np.sum(x**2)
        
        # Fractal noise term with nested chaotic modulation
        noise = 0.02 * np.sum(np.sin(self.chaotic_sequence * x) + 0.03 * np.cos(self.chaotic_sequence * x**2))
        result += noise
        
        # Additional chaotic modulation with nested fractal structure
        modulate = 0.03 * np.sum(np.cos(self.chaotic_sequence * x**2) + 0.02 * np.sin(self.chaotic_sequence * x**3))
        result += modulate
        
        return result