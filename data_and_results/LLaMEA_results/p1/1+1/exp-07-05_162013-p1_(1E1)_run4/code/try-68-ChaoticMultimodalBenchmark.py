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
        
        # Nested chaotic polynomial with dynamic exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponents = [2, 3, 4, 5, 6, 7, 8]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            base_term = x[i]**exp
            result += chaotic_factor * (base_term - exp*base_term**(exp-1) + (exp*(exp-1)/2)*base_term**(exp-2))
            
        # Dynamic trigonometric coupling with time-varying frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                amp = 0.4 * (1 + np.sin(4 * phase)) * (1 + np.cos(2 * phase))
                freq1 = 4 * (1 + np.cos(3 * phase))
                freq2 = 3 * (1 + np.sin(3 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Multi-scale adaptive spherical penalty with chaotic center and radius
        center = np.array([self.chaotic_sequence[i] * 4.0 for i in range(self.dim)])
        radius = 2.0 + 0.8 * np.sin(self.chaotic_sequence[0] * 15)
        result += 0.5 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency chaotic oscillation with variable amplitudes and phases
        for i in range(self.dim):
            freq = 20 + 15 * self.chaotic_sequence[i]
            amp = 0.2 + 0.1 * np.cos(7 * self.chaotic_sequence[i])
            phase = 0.5 * np.sin(5 * self.chaotic_sequence[i])
            result += amp * np.sin(freq * x[i] + phase)
            
        # Global minimum attractor with nested chaotic scaling
        scale = 0.08 + 0.04 * np.sin(self.chaotic_sequence[0] * 25)
        result += scale * np.sum(x**2)
        
        # Add chaotic noise with higher frequency components
        noise = 0.02 * np.sum(np.sin(self.chaotic_sequence * x**2) + 0.5 * np.cos(self.chaotic_sequence * x**3))
        result += noise
        
        # Add new chaotic modulation with nested structure
        modulate = 0.03 * np.sum(np.cos(self.chaotic_sequence * x**2) * np.sin(self.chaotic_sequence * x))
        result += modulate
        
        # Add a dynamic hyperbolic penalty term
        hyperbolic_penalty = 0.05 * np.sum(np.log(1 + np.abs(x)) * np.exp(-x**2))
        result += hyperbolic_penalty
        
        # Add a dynamic coupling between all dimensions
        coupling = 0.04 * np.sum(np.sin(self.chaotic_sequence * np.sum(x)) * np.cos(self.chaotic_sequence * np.mean(x)))
        result += coupling
        
        return result