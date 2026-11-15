import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters for greater complexity
        self.r1, self.r2 = 3.95, 3.89
        self.chaotic_sequence = self._generate_chaotic_sequence()
        
    def _generate_chaotic_sequence(self):
        # Generate highly complex chaotic sequence using coupled logistic maps
        seq = np.zeros(self.dim)
        x1, x2 = 0.5, 0.3
        for i in range(self.dim):
            x1 = self.r1 * x1 * (1 - x1)
            x2 = self.r2 * x2 * (1 - x2)
            seq[i] = 0.5 * (x1 + x2) + 0.2 * np.sin(i * np.pi / self.dim) + 0.1 * np.cos(i * np.pi / (self.dim * 2))
        return seq
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Hyperchaotic polynomial component with nested exponents
        for i in range(self.dim):
            chaotic_factor = self.chaotic_sequence[i]
            exponents = [2, 3, 4, 5, 6, 7, 8]
            exp_idx = int(chaotic_factor * len(exponents)) % len(exponents)
            exp = exponents[exp_idx]
            result += chaotic_factor * (x[i]**exp - exp*x[i]**(exp-1) + (exp*(exp-1)/2)*x[i]**(exp-2) - (exp*(exp-1)*(exp-2)/6)*x[i]**(exp-3))
            
        # Nested trigonometric coupling with multiple chaotic frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase = self.chaotic_sequence[i] * self.chaotic_sequence[j]
                amp = 0.4 * (1 + np.sin(5 * phase)) * (1 + np.cos(3 * phase))
                freq1 = 4 * (1 + np.cos(2 * phase)) * (1 + np.sin(phase))
                freq2 = 3 * (1 + np.sin(2 * phase)) * (1 + np.cos(phase))
                result += amp * np.sin(freq1 * x[i] + phase) * np.cos(freq2 * x[j] + phase)
                
        # Dynamic spherical penalty with hyperchaotic center and time-varying radius
        center = np.array([self.chaotic_sequence[i] * 4.0 for i in range(self.dim)])
        radius = 1.5 + 1.0 * np.sin(self.chaotic_sequence[0] * 15) * np.cos(self.chaotic_sequence[1] * 10)
        result += 0.5 * np.sum(((x - center) / radius)**2)
        
        # Multi-scale chaotic oscillation with variable frequencies and amplitudes
        for i in range(self.dim):
            freq = 20 + 15 * self.chaotic_sequence[i] + 5 * np.sin(self.chaotic_sequence[i] * 7)
            amp = 0.2 + 0.1 * np.cos(7 * self.chaotic_sequence[i]) * np.sin(3 * self.chaotic_sequence[i])
            result += amp * np.sin(freq * x[i])
            
        # Global minimum attractor with hyperchaotic scaling and dynamic offset
        scale = 0.07 + 0.03 * np.sin(self.chaotic_sequence[0] * 25) * np.cos(self.chaotic_sequence[1] * 15)
        offset = 0.1 * np.sin(self.chaotic_sequence[2] * 20)
        result += scale * np.sum((x - offset)**2)
        
        # Add a highly complex chaotic noise term
        noise = 0.02 * np.sum(np.sin(self.chaotic_sequence * x) * np.cos(x**2))
        result += noise
        
        # Enhanced chaotic modulation with multi-frequency interaction
        modulate = 0.05 * np.sum(np.cos(self.chaotic_sequence * x**2) * np.sin(x**3))
        result += modulate
        
        # New hyperchaotic interaction with nested coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq = 10 * (1 + np.sin(self.chaotic_sequence[i] * 9)) * (1 + np.cos(self.chaotic_sequence[j] * 8))
                result += 0.06 * freq * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        # Add a new hyperchaotic coupling term with multi-scale frequency modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq1 = 6 * (1 + np.cos(self.chaotic_sequence[i] * 6)) * (1 + np.sin(self.chaotic_sequence[j] * 5))
                freq2 = 4 * (1 + np.sin(self.chaotic_sequence[i] * 4)) * (1 + np.cos(self.chaotic_sequence[j] * 3))
                result += 0.07 * freq1 * freq2 * np.sin(x[i] * x[j]) * np.cos(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        # Add a new chaotic polynomial interaction with higher order terms and variable coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = 0.03 * (1 + np.sin(self.chaotic_sequence[i] * 12)) * (1 + np.cos(self.chaotic_sequence[j] * 10))
                result += coeff * (x[i]**4 + x[j]**4) * np.cos(self.chaotic_sequence[i] * x[j])
        
        # Add a new chaotic sinusoidal coupling with variable phase shifts and multi-scale modulation
        for i in range(self.dim):
            phase_shift = 0.7 * np.sin(self.chaotic_sequence[i] * 10) * np.cos(self.chaotic_sequence[i] * 5)
            result += 0.04 * np.sin(5 * x[i] + phase_shift) * np.cos(4 * x[i] + phase_shift)
        
        # Add a new chaotic interaction with dynamic coupling strength and multi-frequency modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.08 * (1 + np.sin(self.chaotic_sequence[i] * 13)) * (1 + np.cos(self.chaotic_sequence[j] * 11))
                freq = 8 * (1 + np.sin(self.chaotic_sequence[i] * 7)) * (1 + np.cos(self.chaotic_sequence[j] * 6))
                result += coupling_strength * freq * np.sin(x[i] + x[j]) * np.cos(self.chaotic_sequence[i] * x[j] + self.chaotic_sequence[j] * x[i])
        
        return result