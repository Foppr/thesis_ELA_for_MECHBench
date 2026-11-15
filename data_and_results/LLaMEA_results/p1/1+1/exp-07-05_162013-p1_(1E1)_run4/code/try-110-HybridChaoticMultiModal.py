import numpy as np

class HybridChaoticMultiModal:
    def __init__(self, dim):
        self.dim = dim
        self.r = 3.9
        self.chaotic_sequence = self._generate_chaotic_sequence()
        self.global_min = np.zeros(dim)
        
    def _generate_chaotic_sequence(self):
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x
        return seq
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Separable quadratic component
        result = 0.5 * np.sum(x**2)
        
        # Chaotic sinusoidal coupling with dynamic frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 2 * (1 + self.chaotic_sequence[i] * self.chaotic_sequence[j])
                amp = 0.3 * (1 + np.sin(self.chaotic_sequence[i] * 10))
                result += amp * np.sin(freq * (x[i] - x[j])) * np.cos(freq * (x[i] + x[j]))
        
        # Multi-modal structure with chaotic basin boundaries
        for i in range(self.dim):
            # Dynamic basin center controlled by chaotic sequence
            center = 2.5 * self.chaotic_sequence[i]
            # Multi-modal potential with varying depths
            depth = 0.5 + 0.3 * np.sin(self.chaotic_sequence[i] * 15)
            result += depth * (x[i] - center)**2 * (x[i] + center)**2
        
        # Chaotic scaling factor for global structure
        scale_factor = 1.0 + 0.2 * np.sin(self.chaotic_sequence[0] * 20)
        result *= scale_factor
        
        # Add chaotic noise with varying amplitude
        noise_amp = 0.05 * (1 + np.cos(self.chaotic_sequence[1] * 12))
        noise = noise_amp * np.sum(np.sin(self.chaotic_sequence * x))
        result += noise
        
        # Add chaotic oscillation with time-varying frequency
        freq = 10 + 5 * self.chaotic_sequence[0]
        result += 0.1 * np.sin(freq * np.sum(x))
        
        # Add a global chaotic attractor term
        attractor = 0.02 * np.sum((x - self.global_min)**2)
        result += attractor
        
        return result