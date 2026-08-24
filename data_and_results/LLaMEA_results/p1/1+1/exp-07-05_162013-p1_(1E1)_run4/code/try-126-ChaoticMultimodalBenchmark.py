import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic constants with higher complexity
        self.r = 3.95  # Increased chaos parameter
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate complex chaotic sequence using multiple chaotic maps
        seq = np.zeros(self.dim)
        x1, x2 = 0.5, 0.3  # Dual initial values
        for i in range(self.dim):
            x1 = self.r * x1 * (1 - x1)
            x2 = self.r * x2 * (1 - x2)
            seq[i] = 0.5 * x1 + 0.5 * x2 + 0.1 * np.sin(i * np.pi / self.dim) + 0.05 * np.cos(i * np.pi / (self.dim * 2))
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Hyperchaotic polynomial component with nested exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            # Nested variable exponents based on chaotic sequence
            exponents = [2, 3, 4, 5, 6, 7, 8]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            # Add nested chaotic polynomial terms
            result += chaotic_factor * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2) + (exp*(exp-1)*(exp-2)/6)*x[i]**(exp-3))
            
        # Multi-scale trigonometric coupling with dynamic frequencies and amplitudes
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                amp = 0.4 * (1 + np.sin(5 * phase)) * (1 + np.cos(3 * phase))  # Dynamic amplitude
                freq1 = 4 * (1 + np.cos(3 * phase)) * (1 + np.sin(2 * phase))
                freq2 = 3 * (1 + np.sin(4 * phase)) * (1 + np.cos(2 * phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Dynamic spherical penalty with multi-scale chaotic center and variable radius
        center = np.array([self.chaotic_sequence[i] * 4.0 for i in range(self.dim)])
        radius = 1.5 + 1.0 * np.sin(self.chaotic_sequence[0] * 15) * np.cos(self.chaotic_sequence[1] * 10)
        result += 0.5 * np.sum(((x - center) / radius)**2)
        
        # Multi-frequency hyperchaotic oscillation with varying amplitudes and phases
        for i in range(self.dim):
            freq = 20 + 15 * self.chaotic_sequence[i] + 5 * np.sin(self.chaotic_sequence[i] * 12)
            amp = 0.2 + 0.1 * np.cos(7 * self.chaotic_sequence[i]) * np.sin(5 * self.chaotic_sequence[i])
            phase = 0.3 * np.sin(self.chaotic_sequence[i] * 8)
            result += amp * np.sin(freq * x[i] + phase)
            
        # Add global minimum attractor with multi-scale chaotic scaling
        scale = 0.08 + 0.04 * np.sin(self.chaotic_sequence[0] * 25) * np.cos(self.chaotic_sequence[1] * 20)
        result += scale * np.sum(x**2)
        
        # Add complex chaotic noise term with nested modulation
        noise = 0.02 * np.sum(np.sin(self.chaotic_sequence * x) * np.cos(self.chaotic_sequence * x**2))
        result += noise
        
        # Add nested chaotic modulation with higher-order coupling
        modulate = 0.05 * np.sum(np.cos(self.chaotic_sequence * x**2) * np.sin(self.chaotic_sequence * x**3))
        result += modulate
        
        # Add hyperchaotic interaction term with multiple coupling frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq1 = 10 * (1 + np.sin(self.chaotic_sequence[i] * 10))
                freq2 = 8 * (1 + np.cos(self.chaotic_sequence[j] * 8))
                result += 0.06 * freq1 * freq2 * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        # Add hyperchaotic coupling with polynomial interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 6 * (1 + np.sin(self.chaotic_sequence[i] * 6)) * (1 + np.cos(self.chaotic_sequence[j] * 6))
                result += 0.07 * freq * (x[i]**2 + x[j]**2) * np.sin(self.chaotic_sequence[i] * x[j])
        
        # Add multi-scale chaotic polynomial interaction with variable exponents
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp = 3 + int(2 * self.chaotic_sequence[i]) % 4
                result += 0.03 * (x[i]**exp + x[j]**exp) * np.cos(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        # Add nested chaotic sinusoidal coupling with phase modulation
        for i in range(self.dim):
            phase_shift = 0.7 * np.sin(self.chaotic_sequence[i] * 10) + 0.3 * np.cos(self.chaotic_sequence[i] * 15)
            result += 0.04 * np.sin(5 * x[i] + phase_shift) * np.cos(4 * x[i] + phase_shift)
        
        # Add complex hyperchaotic interaction with nested trigonometric terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 9 * (1 + np.sin(self.chaotic_sequence[i] * 9)) * (1 + np.cos(self.chaotic_sequence[j] * 9))
                result += 0.08 * freq * np.sin(x[i] * x[j]) * np.cos(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i]) * np.sin(self.chaotic_sequence[i] * self.chaotic_sequence[j])
        
        return result