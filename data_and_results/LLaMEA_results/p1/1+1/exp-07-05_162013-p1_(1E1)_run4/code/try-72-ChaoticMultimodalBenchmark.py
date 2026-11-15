import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with nested logistic maps
        self.r1 = 3.95
        self.r2 = 3.82
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate nested chaotic sequence using two logistic maps
        seq = np.zeros(self.dim)
        x1, x2 = 0.5, 0.3
        for i in range(self.dim):
            x1 = self.r1 * x1 * (1 - x1)
            x2 = self.r2 * x2 * (1 - x2)
            seq[i] = 0.5 * x1 + 0.5 * x2 + 0.1 * np.sin(i * np.pi / self.dim) + 0.05 * np.cos(i * np.pi / (self.dim * 2))
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Nested chaotic polynomial component with dynamic exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            # Dynamic exponents based on nested chaotic values
            exponents = [2, 3, 4, 5, 6, 7, 8]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            # Add chaotic modulation to polynomial coefficients
            coeff_mod = 1 + 0.2 * np.sin(10 * chaotic_factor)
            result += coeff_mod * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2))
            
        # Multi-scale trigonometric coupling with dynamic frequencies and phases
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j] + 0.1 * np.cos(5 * (x[i] + x[j]))
                amp = 0.4 * (1 + np.sin(4 * phase)) * (1 + 0.1 * np.cos(3 * chaotic_factor))
                freq1 = 2 + 3 * np.sin(2 * phase)
                freq2 = 1.5 + 2 * np.cos(3 * phase)
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Multi-layered adaptive spherical penalty with chaotic center and dynamic radius
        center = np.array([self.chaotic_sequence[i] * 4.0 + 0.5 * np.sin(10 * i) for i in range(self.dim)])
        radius = 2.0 + 0.8 * np.sin(self.chaotic_sequence[0] * 15)
        # Add multiple penalty layers
        penalty1 = 0.3 * np.sum(((x - center) / radius)**2)
        penalty2 = 0.2 * np.sum(((x - center) / (radius * 0.5))**3)
        result += penalty1 + penalty2
        
        # Multi-frequency chaotic oscillation with variable amplitudes and phases
        for i in range(self.dim):
            freq = 20 + 15 * self.chaotic_sequence[i] + 5 * np.sin(7 * x[i])
            amp = 0.2 + 0.1 * np.cos(8 * self.chaotic_sequence[i]) + 0.05 * np.sin(12 * x[i])
            phase = 0.5 * np.sin(6 * self.chaotic_sequence[i])
            result += amp * np.sin(freq * x[i] + phase)
            
        # Add chaotic attractor dynamics with multiple fixed points
        attractor_center = np.array([np.sin(2 * self.chaotic_sequence[i]) * 2.0 for i in range(self.dim)])
        result += 0.15 * np.sum((x - attractor_center)**2)
        
        # Add chaotic noise with nested structure
        noise = 0.02 * np.sum(np.sin(self.chaotic_sequence * x) * np.cos(2 * self.chaotic_sequence * x))
        result += noise
        
        # Add novel chaotic modulation with nested oscillations
        modulate = 0.03 * np.sum(np.cos(self.chaotic_sequence * x**2) * np.sin(3 * self.chaotic_sequence * x))
        result += modulate
        
        # Add dynamic scaling based on chaotic sequence
        scale = 0.03 + 0.02 * np.sin(self.chaotic_sequence[0] * 25)
        result += scale * np.sum(x**4)
        
        return result