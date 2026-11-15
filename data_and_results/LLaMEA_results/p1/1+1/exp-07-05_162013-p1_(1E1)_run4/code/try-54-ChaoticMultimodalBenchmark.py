import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slightly mutated chaotic constants for increased complexity
        self.r = 3.9  # Increased chaos parameter
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Mutated chaotic sequence with different sinusoidal modulation
        seq = np.zeros(self.dim)
        x = 0.5
        for i in range(self.dim):
            x = self.r * x * (1 - x)
            seq[i] = x + 0.15 * np.cos(i * np.pi / self.dim)  # Changed to cosine modulation
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Mutated chaotic polynomial component with altered exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponents = [3, 4, 5, 6, 7]  # Changed exponents
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            result += chaotic_factor * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2))
            
        # Mutated trigonometric coupling with different frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                amp = 0.4 * (1 + np.cos(4 * phase))  # Changed amplitude modulation
                freq1 = 4 * (1 + np.sin(3 * phase))  # Changed frequencies
                freq2 = 3 * (1 + np.cos(3 * phase))
                result += amp * np.cos(freq1 * x[i] + phase) * np.sin(freq2 * x[j] + phase)
                
        # Mutated adaptive spherical penalty with altered center and radius
        center = np.array([self.chaotic_sequence[i] * 2.5 for i in range(self.dim)])  # Changed center scaling
        radius = 2.0 + 0.3 * np.cos(self.chaotic_sequence[0] * 12)  # Changed radius modulation
        result += 0.5 * np.sum(((x - center) / radius)**2)  # Increased penalty weight
        
        # Mutated multi-frequency chaotic oscillation
        for i in range(self.dim):
            freq = 20 + 8 * self.chaotic_sequence[i]  # Changed base frequency
            amp = 0.2 + 0.08 * np.sin(6 * self.chaotic_sequence[i])  # Changed amplitude
            result += amp * np.cos(freq * x[i])  # Changed to cosine
            
        # Mutated global minimum attractor
        scale = 0.03 + 0.07 * np.cos(self.chaotic_sequence[0] * 25)  # Changed scaling
        result += scale * np.sum(x**2)
        
        # Mutated noise term
        noise = 0.015 * np.sum(np.cos(self.chaotic_sequence * x))  # Changed to cosine noise
        result += noise
        
        return result